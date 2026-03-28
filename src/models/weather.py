"""Modelos de dados para informações climáticas."""

from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import Any

# ---------------------------------------------------------------------------
# Mapeamento WMO → condição em português
# ---------------------------------------------------------------------------
_WMO_CONDITIONS: dict[int, str] = {
    0: "Céu limpo",
    1: "Principalmente limpo",
    2: "Parcialmente nublado",
    3: "Encoberto",
    45: "Neblina",
    48: "Nevoeiro com geada",
    51: "Chuvisco fraco",
    53: "Chuvisco moderado",
    55: "Chuvisco intenso",
    56: "Chuvisco congelante fraco",
    57: "Chuvisco congelante intenso",
    61: "Chuva fraca",
    63: "Chuva moderada",
    65: "Chuva forte",
    66: "Chuva congelante fraca",
    67: "Chuva congelante forte",
    71: "Neve fraca",
    73: "Neve moderada",
    75: "Neve forte",
    77: "Granizo",
    80: "Pancada de chuva fraca",
    81: "Pancada de chuva moderada",
    82: "Pancada de chuva forte",
    85: "Pancada de neve fraca",
    86: "Pancada de neve forte",
    95: "Trovoada",
    96: "Trovoada com granizo",
    99: "Trovoada com granizo intenso",
}

_PT_WEEKDAYS: tuple[str, ...] = (
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
    "Domingo",
)


# ---------------------------------------------------------------------------
# Weather
# ---------------------------------------------------------------------------
@dataclass
class Weather:
    """Condições climáticas em um instante."""

    temperature: float
    windspeed: float
    winddirection: float
    time: str
    humidity: float | None = None
    pressure: float | None = None
    weather_code: int | None = None

    @property
    def condition(self) -> str:
        """Descrição amigável da condição climática baseada no WMO."""
        if self.weather_code is not None:
            return _WMO_CONDITIONS.get(self.weather_code, "Tempo variável")

        # Fallback inteligente baseado em temperatura
        if self.temperature >= 30:
            return "Muito Quente"
        if self.temperature <= 10:
            return "Frio"
        return "Tempo ameno"

    @property
    def feels_like(self) -> float:
        """Calcula a sensação térmica (Wind Chill ou Heat Index)."""
        # Wind Chill (Frio + Vento)
        if self.temperature <= 10 and self.windspeed > 4.8:
            v = self.windspeed**0.16
            return round(
                13.12
                + 0.6215 * self.temperature
                - 11.37 * v
                + 0.3965 * self.temperature * v,
                1,
            )

        # Heat Index simplificado (Calor + Umidade)
        if self.temperature >= 27 and self.humidity and self.humidity > 40:
            return round(self.temperature + 0.05 * self.humidity, 1)

        return round(self.temperature, 1)

    def __str__(self) -> str:
        return f"{self.temperature}°C | {self.condition} | {self.time}"


# ---------------------------------------------------------------------------
# DailyForecast
# ---------------------------------------------------------------------------
@dataclass
class DailyForecast:
    """Previsão para um dia específico."""

    date: str
    max_temp: float | None = None
    min_temp: float | None = None
    sunrise: str | None = None
    sunset: str | None = None
    weather_code: int | None = None

    @property
    def day_name(self) -> str:
        """Retorna 'Hoje', 'Amanhã' ou o dia da semana em PT-BR."""
        try:
            # Garante compatibilidade com formatos de data YYYY-MM-DD
            dt_str = self.date.split("T")[0]
            dt = datetime.strptime(dt_str, "%Y-%m-%d").date()
            today = date.today()

            if dt == today:
                return "Hoje"
            if dt == today + timedelta(days=1):
                return "Amanhã"

            return _PT_WEEKDAYS[dt.weekday()]
        except (ValueError, IndexError, AttributeError):
            return self.date

    @property
    def condition(self) -> str:
        return (
            _WMO_CONDITIONS.get(self.weather_code, "Variável")
            if self.weather_code is not None
            else "---"
        )


# ---------------------------------------------------------------------------
# WeatherForecast
# ---------------------------------------------------------------------------
@dataclass
class WeatherForecast:
    """Previsão completa: condição atual, horária e diária."""

    current: Weather
    hourly: list[dict[str, Any]] = field(default_factory=list)
    daily: list[DailyForecast] = field(default_factory=list)

    def forecast_for(self, date_obj: datetime) -> DailyForecast | None:
        """Busca a previsão diária para uma data específica."""
        target = date_obj.strftime("%Y-%m-%d")
        return next((d for d in self.daily if d.date.startswith(target)), None)

    @property
    def today(self) -> DailyForecast | None:
        return self.forecast_for(datetime.now()) or (
            self.daily[0] if self.daily else None
        )

    @property
    def tomorrow(self) -> DailyForecast | None:
        return self.forecast_for(datetime.now() + timedelta(days=1)) or (
            self.daily[1] if len(self.daily) > 1 else None
        )
