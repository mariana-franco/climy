import pytest
from src.models.weather import Weather, DailyForecast, WeatherForecast


def test_weather_model_init():
    """Valida a criação do objeto de clima atual."""
    w = Weather(
        temperature=25.5,
        windspeed=10.0,
        winddirection=180,
        time="2026-03-26T12:00",
        weather_code=0,
        humidity=60,
    )
    assert w.temperature == 25.5
    assert isinstance(w.time, str)


def test_daily_forecast_model():
    """Valida a estrutura da previsão diária."""
    df = DailyForecast(
        date="2026-03-27",
        max_temp=30.0,
        min_temp=20.0,
        sunrise="06:00",
        sunset="18:00",
        weather_code=1,
    )
    assert df.max_temp > df.min_temp
