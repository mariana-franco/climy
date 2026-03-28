"""
Aplicação principal Streamlit para Climy.
Responsável pela interface de busca e exibição do dashboard meteorológico.
"""

import html
import logging
import os
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components
import pytz

from services.weather_api import (
    WeatherAPIError,
    get_complete_forecast,
    get_rain_forecast,
    get_weather,
    search_cities,
)
from src.config import CACHE_TTL

tz = pytz.timezone("America/Sao_Paulo")
now_dt = datetime.now(tz)

# --- Configuração da página ---
st.set_page_config(
    page_title="Climy",
    page_icon="🌤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

logging.basicConfig(level=logging.ERROR)


# --- Constantes (PEP 8: Maiúsculas para escopo global) ---
PT_ABR = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
WDIRS = ["N", "NE", "L", "SE", "S", "SO", "O", "NO"]
DIAS_NOMES = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
MESES_NOMES = [
    "Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun",
    "Jul",
    "Ago",
    "Set",
    "Out",
    "Nov",
    "Dez",
]

WMO_EMOJIS: dict[int, str] = {
    0: "☀️",
    1: "🌤️",
    2: "⛅",
    3: "☁️",
    45: "🌫️",
    48: "🌫️",
    51: "🌦️",
    53: "🌦️",
    55: "🌧️",
    61: "🌧️",
    63: "🌧️",
    65: "🌧️",
    80: "🌦️",
    81: "🌧️",
    82: "⛈️",
    95: "⛈️",
    96: "⛈️",
    99: "⛈️",
}


# --- CSS Loader ---
def load_css(file_name):
    """Carrega o arquivo CSS externo com encoding definido."""
    if os.path.exists(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"Arquivo CSS não encontrado em {file_name}")


load_css("assets/style.css")


# --- Helpers ---
def safe(val):
    """Escapa strings para evitar problemas com HTML."""
    return html.escape(str(val)) if val is not None else ""


def get_weather_emoji(code):
    """Retorna o emoji correspondente ao código WMO."""
    return WMO_EMOJIS.get(code, "🌡️") if code is not None else "🌡️"


def get_wind_direction(degree):
    """Converte graus em direção de vento (N, S, L, O)."""
    try:
        return WDIRS[int((float(degree) / 45) % 8)]
    except (ValueError, TypeError, ZeroDivisionError):
        return "—"


def format_population(n):
    """Formata números grandes de população (ex: 1.2M, 50k)."""
    try:
        if n >= 1_000_000:
            return f"{n/1_000_000:.1f}M hab."
        if n >= 1_000:
            return f"{n/1_000:.0f}k hab."
        return f"{n} hab."
    except (ValueError, TypeError):
        return ""


def format_location_label(city_data):
    """Gera o texto de localização (Estado, País)."""
    return ", ".join(p for p in (city_data.get("state"), city_data.get("country")) if p)


def get_weekday_abbr(iso_date):
    """Retorna a abreviação do dia da semana a partir de uma data ISO."""
    try:
        return PT_ABR[datetime.fromisoformat(iso_date).weekday()]
    except (ValueError, TypeError):
        return "—"


def get_temp_icon(t):
    """Retorna um ícone dinâmico baseado na temperatura atual."""
    try:
        if t < 15:
            return "❄️"
        if t < 25:
            return "🍃"
        if t < 30:
            return "☀️"
        return "🔥"
    except (ValueError, TypeError):
        return "🌡️"


# --- Inicialização do Estado (Session State) ---
for state_key, default_val in [
    ("city", None),
    ("res", []),
    ("weather", None),
    ("forecast", None),
]:
    if state_key not in st.session_state:
        st.session_state[state_key] = default_val


# --- Header ---
st.markdown(
    '<div class="c-title"><h1>🌤️ Climy</h1><p>Sua previsão do tempo sempre atualizada!</p></div>',
    unsafe_allow_html=True,
)


# --- Busca ---
def format_city_label(item: dict) -> str:
    if not item:
        return ""
    location_parts = [item.get("state"), item.get("country")]
    location_str = ", ".join(filter(None, location_parts))
    pop = item.get("population", 0)
    pop_str = f" · {pop:,} hab.".replace(",", ".") if pop and pop > 0 else ""
    label = f"📍 {item.get('name', 'Desconhecido')}"
    if location_str:
        label += f" — {location_str}"
    label += pop_str
    return label


search_area = st.empty()

# 1. ESTADO DE BUSCA: Se não há cidade, mostra o campo e o botão
if not st.session_state.get("city"):
    with search_area.container():
        col1, col2 = st.columns([7, 3])
        with col1:
            query = st.text_input(
                "Busca",
                placeholder="Digite o nome da cidade...",
                label_visibility="collapsed",
                key="main_search",
            )
        with col2:
            btn_buscar = st.button("Buscar 🔍", use_container_width=True)

        if btn_buscar or (query and len(query) >= 3):
            results = search_cities(query)  # Sua função de API
            if results:
                for item in results:
                    if st.button(
                        format_city_label(item),
                        key=f"btn_{item['lat']}_{item['lon']}",
                        use_container_width=True,
                    ):
                        st.session_state.city = item
                        st.rerun()


# --- Dashboard ---
if st.session_state.city:
    curr_city = st.session_state.city
    now_dt = datetime.now()

    # Expiração de cache
    if st.session_state.weather:
        if (now_dt - st.session_state.weather["at"]).seconds > CACHE_TTL:
            st.session_state.weather = None

    if st.session_state.weather is None:
        with st.spinner(f"Carregando {safe(curr_city['name'])}..."):
            try:
                w_data = get_weather(
                    curr_city["lat"], curr_city["lon"], cache_ttl=CACHE_TTL
                )
                rn_data = get_rain_forecast(curr_city["lat"], curr_city["lon"])
                fc_data = get_complete_forecast(curr_city["lat"], curr_city["lon"])

                st.session_state.weather = {"d": w_data, "rain": rn_data, "at": now_dt}
                st.session_state.forecast = fc_data
            except WeatherAPIError:
                logging.exception("Erro ao carregar dados")
                st.error("Erro ao carregar dados.")
                st.session_state.city = None
                st.rerun()

    w = st.session_state.weather.get("d")
    rn = st.session_state.weather.get("rain")
    fc = st.session_state.forecast

    hum = getattr(w, "humidity", 0) or 0
    temp = getattr(w, "temperature", 0) or 0
    feels = getattr(w, "feels_like", 0) or 0
    cond_str = safe(getattr(w, "condition", "Desconhecido"))
    w_code = getattr(w, "weather_code", 0)

    rv = rn if isinstance(rn, (int, float)) else 0
    rcl_class = " rain-hi" if rv > 30 else ""
    dyn_icon = get_temp_icon(temp)

    label_hoje = (
        f"{DIAS_NOMES[now_dt.weekday()]}, {now_dt.day} {MESES_NOMES[now_dt.month-1]}"
    )

    t_max, t_min = temp, temp
    if fc and getattr(fc, "daily", None) and len(fc.daily) > 0:
        t_max = getattr(fc.daily[0], "max_temp", temp)
        t_min = getattr(fc.daily[0], "min_temp", temp)

    wxe = get_weather_emoji(w_code)

    # HERO HTML
    hero_html = f"""
<div class="hero">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
        <div class="hero-loc">{safe(format_location_label(curr_city))}</div>
        <div class="hero-loc">{label_hoje}</div>
    </div>
    <div class="hero-city" style="font-size: 1.4rem; margin-bottom: 10px;">{safe(curr_city["name"])}</div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
        <div>
            <span class="hero-temp">{temp:.0f}</span>
            <span class="hero-unit">°</span>
        </div>
        <div class="hero-wx" style="font-size: 4.5rem !important;">{wxe}</div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div class="hero-feels">Sensação térmica de {feels:.0f}°</div>
        <div class="hero-min-max" style="font-weight: 700;">
            <span style="color:var(--blue)">↓{t_min:.0f}°</span>
            <span style="margin: 0 5px; opacity: 0.1;">|</span>
            <span style="color:var(--orange)">↑{t_max:.0f}°</span>
        </div>
    </div>
    <div class="hero-cond">{cond_str}</div>
    <div class="hero-div"></div>
    <div class="hero-mets">
        <div class="hm">
            <div class="hm-ico">💨</div>
            <div class="hm-val">{getattr(w, 'windspeed', 0) or 0:.0f} <span class="hm-unit">km/h</span></div>
            <div class="hm-lbl">Vento</div>
        </div>
        <div class="hm">
            <div class="hm-ico">💧</div>
            <div class="hm-val{rcl_class}">{hum:.0f} <span class="hm-unit">%</span></div>
            <div class="hm-lbl">Umidade</div>
        </div>
        <div class="hm">
            <div class="hm-ico">🌧️</div>
            <div class="hm-val{rcl_class}">{rv:.0f} <span class="hm-unit">%</span></div>
            <div class="hm-lbl">Chuva</div>
        </div>
    </div>
</div>
"""
    st.markdown(hero_html, unsafe_allow_html=True)

    # PRÓXIMAS 24 HORAS
    if fc and getattr(fc, "hourly", None):
        st.markdown(
            f'<div class="sec">{dyn_icon}  Próximas 24 horas</div>',
            unsafe_allow_html=True,
        )

        now_h = now_dt.hour
        h_html_list = ""

        for i, h_item in enumerate(fc.hourly[:24]):
            try:
                dt_obj = datetime.fromisoformat(h_item["time"])
                is_now = dt_obj.hour == now_h and i < 2

                bg, col, col3, bdr = (
                    ("#3b9edd", "white", "rgba(255,255,255,.85)", "#3b9edd")
                    if is_now
                    else ("white", "#1e3a5f", "#8ba8c2", "#dde8f2")
                )

                temp_h = h_item.get("temperature") or 0
                rain_h = h_item.get("rain_probability", 0) or 0

                h_html_list += (
                    f'<div style="flex-shrink:0;min-width:72px;background:{bg};border:1.5px solid {bdr};'
                    f'border-radius:16px;padding:.65rem .55rem;text-align:center;box-shadow:0 1px 1px rgba(30,58,95,.07);">'
                    f'<div style="font-size:.8rem;font-weight:600;color:{col3};">'
                    f'{"agora" if is_now else dt_obj.strftime("%Hh")}</div>'
                    f'<div style="font-size:1.5rem;margin:.2rem 0">{get_weather_emoji(h_item.get("weather_code"))}</div>'
                    f'<div style="font-size:1rem;font-weight:800;color:{col};">{temp_h:.0f}°</div>'
                    f'<div style="font-size:.7rem;font-weight:600;color:{col3};"><span style="margin-right:2px;">🌧️</span>{rain_h:.0f}%</div></div>'
                )
            except (ValueError, TypeError, KeyError):
                continue

        components.html(
            f'<div style="display:flex;gap:.5rem;overflow-x:auto;padding:.25rem;font-family:sans-serif;">'
            f"{h_html_list}</div>",
            height=145,
        )

    # PRÓXIMOS 7 DIAS
    if fc and getattr(fc, "daily", None):
        st.markdown('<div class="sec">📅 Próximos 7 dias</div>', unsafe_allow_html=True)
        d_html_list = ""

        for d_item in fc.daily[:7]:
            try:
                is_today = str(d_item.date).strip() == now_dt.strftime("%Y-%m-%d")
                bg, col, col3, bdr = (
                    ("#3b9edd", "white", "rgba(255,255,255,.85)", "#3b9edd")
                    if is_today
                    else ("white", "#1e3a5f", "#8ba8c2", "#dde8f2")
                )

                d_html_list += (
                    f'<div style="flex-shrink:0;min-width:72px;background:{bg};border:1.5px solid {bdr};'
                    f'border-radius:16px;padding:.75rem .55rem;text-align:center;box-shadow:0 1px 1px rgba(30,58,95,.07);">'
                    f'<div style="font-size:.7rem;font-weight:600;color:{col3};text-transform:uppercase;">'
                    f'{"Hoje" if is_today else get_weekday_abbr(d_item.date)}</div>'
                    f'<div style="font-size:1.5rem;margin:.2rem 0">{get_weather_emoji(getattr(d_item, "weather_code", None))}</div>'
                    f'<div style="font-size:1rem;font-weight:800;color:{col}">{getattr(d_item, "max_temp", 0):.0f}°<span style="font-size:.6rem;font-weight:300;"> máx</span></div>'
                    f'<div style="font-size:.6rem;font-weight:600;color:{col3};">{getattr(d_item, "min_temp", 0):.0f}°<span style="font-size:.6rem;font-weight:300;"> mín</span></div></div>'
                )
            except (ValueError, TypeError, AttributeError):
                continue

        components.html(
            f'<div style="display:flex;gap:.5rem;overflow-x:auto;padding:.25rem;font-family:sans-serif;">'
            f"{d_html_list}</div>",
            height=155,
        )

    # Botões de Ação
    st.markdown("<br>", unsafe_allow_html=True)
    ca, cb = st.columns(2)

    with ca:
        if st.button("🔄 Atualizar", use_container_width=True):
            st.session_state.weather = None
            st.rerun()

    with cb:
        if st.button("🌍 Outra cidade", use_container_width=True):
            st.session_state.city, st.session_state.res = None, []
            st.rerun()

    # Footer
    st.markdown(
        f'<div class="foot"><span>Climy © {now_dt.year}</span>'
        f'<span>Dados via <a href="https://open-meteo.com/" target="_blank">Open-Meteo</a></span></div>',
        unsafe_allow_html=True,
    )
