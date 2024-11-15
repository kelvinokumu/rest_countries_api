import requests
from app.schemas.country_schema import CountryResponse

REST_COUNTRIES_URL = "https://restcountries.com/v3.1"

def get_all_countries() -> list[CountryResponse]:
    response = requests.get(f"{REST_COUNTRIES_URL}/all")
    response.raise_for_status()
    countries = response.json()
    return [
        CountryResponse(
            name=country["name"]["common"],
            capital=country.get("capital", ["N/A"])[0],
            region=country.get("region", "Unknown"),
            population=country.get("population", 0),
        )
        for country in countries
    ]

def get_country_by_name(country_name: str) -> CountryResponse:
    response = requests.get(f"{REST_COUNTRIES_URL}/name/{country_name}")
    response.raise_for_status()
    countries = response.json()
    if countries:
        country = countries[0]
        return CountryResponse(
            name=country["name"]["common"],
            capital=country.get("capital", ["N/A"])[0],
            region=country.get("region", "Unknown"),
            population=country.get("population", 0),
        )
    else:
        raise ValueError("Country not found")

def get_countries_by_region(region: str) -> list[CountryResponse]:
    response = requests.get(f"{REST_COUNTRIES_URL}/region/{region}")
    response.raise_for_status()
    countries = response.json()
    return [
        CountryResponse(
            name=country["name"]["common"],
            capital=country.get("capital", ["N/A"])[0],
            region=country.get("region", "Unknown"),
            population=country.get("population", 0),
        )
        for country in countries
    ]

