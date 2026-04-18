from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

# Usage
user = User(
    name="John",
    age=25,
    address={
        "city": "Pune",
        "pincode": 411001
    }
)

print(user)