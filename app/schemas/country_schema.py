from pydantic import BaseModel

class CountryResponse(BaseModel):
    name: str
    capital: str
    region: str
    population: int

    class Config:
        orm_mode = True
