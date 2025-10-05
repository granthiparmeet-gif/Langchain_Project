# from pydantic import BaseModel, Field
# from typing import Optional

# # class Verifier(BaseModel):
# #     name: str
# #     age : int = 14

# # person = Verifier(name="Harshjot")
# # print(person)

# # class Address (BaseModel):
# #     city: str
# #     country : str

# # class User (BaseModel):
# #     name : str
# #     address : Address


# # person = User(name = "Parmeet", address={"city" : "Aurangabad", "country" : "India"})

# # print(person.address.city)


# # class Book(BaseModel):
# #     title : str
# #     author : str
# #     pages : int = Field(gt=0, description="Number of pages must be positive")


# # book = Book(title=  "MyBook", author = "harry Potter", pages= -23)
# # print(book.pages)


# class Product(BaseModel):
#     price: Optional[float] = Field(None, regex = "",description="", examples=)

from typing import List, Dict, Tuple, Optional

from pydantic import BaseModel, Field

class Num(BaseModel):
    numbers : List[int] = Field([4,5,6], description="this is a list of numbers")
    person: Dict[str,str]
    cordinates: Tuple[float, float]

number = Num(person= {"Parmeet":"Male", "kaustubh":"Female"}, cordinates=(49.5,86.2))
print(number.cordinates)

