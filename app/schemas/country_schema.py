from pydantic import BaseModel

class CountryResponse(BaseModel):
    name: str
    capital: str
    region: str
    population: int

    class Config:
        orm_mode = True

        """_summary_
        ORM (Object-Relational Mapping) is a programming technique used to map data between a relational database 
        (like MySQL, PostgreSQL, or SQLite) and an object-oriented programming language 
        (like Python, Java, or Ruby). The primary goal of ORM is to abstract database operations 
        so developers can interact with the database using objects and methods rather than writing raw SQL queries.
        """