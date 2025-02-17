from fastapi import APIRouter, HTTPException, Query
from schemas.country_schema import CountryResponse

from services.country_service import (
    get_all_countries,
    get_country_by_name,
    get_countries_by_region,
)

router = APIRouter()

@router.get("/countries", response_model=list[CountryResponse])
async def read_all_countries():
    try:
        return get_all_countries()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/countries/{country_name}", response_model=CountryResponse)
async def read_country(country_name: str):
    try:
        return get_country_by_name(country_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/countries/region/{region}", response_model=list[CountryResponse])
async def read_countries_by_region(region: str):
    try:
        return get_countries_by_region(region)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

