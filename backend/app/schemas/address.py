from pydantic import BaseModel


class AddressCreate(BaseModel):
    street: str
    house_number: str
    apartment_number: str | None = None
    postal_code: str
    city: str
    country: str

    company_name: str | None = None
    tax_number: str | None = None

    user_id: int


class AddressResponse(BaseModel):
    id: int

    street: str
    house_number: str
    apartment_number: str | None

    postal_code: str
    city: str
    country: str

    company_name: str | None
    tax_number: str | None

    user_id: int

    class Config:
        from_attributes = True

class AddressUpdate(BaseModel):
    street: str
    house_number: str
    apartment_number: str | None = None
    postal_code: str
    city: str
    country: str

    company_name: str | None = None
    tax_number: str | None = None