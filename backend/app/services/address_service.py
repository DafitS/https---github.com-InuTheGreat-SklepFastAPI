from sqlalchemy.orm import Session

from app.models.address import Address

from app.repositories.address_repository import (
    AddressRepository
)

from app.schemas.address import (
    AddressCreate,
    AddressUpdate
)

repository = AddressRepository()


class AddressService:

    def create(
        self,
        db: Session,
        address_data: AddressCreate
    ):

        address = Address(
            street=address_data.street,
            house_number=address_data.house_number,
            apartment_number=address_data.apartment_number,
            postal_code=address_data.postal_code,
            city=address_data.city,
            country=address_data.country,
            company_name=address_data.company_name,
            tax_number=address_data.tax_number,
            user_id=address_data.user_id
        )

        return repository.create(
            db,
            address
        )

    def get_all(
        self,
        db: Session
    ):
        return repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        address_id: int
    ):
        return repository.get_by_id(
            db,
            address_id
        )

    def delete_by_id(
        self,
        db: Session,
        address_id: int
    ):
        return repository.delete_by_id(
            db,
            address_id
        )

    def update(
        self,
        db: Session,
        address_id: int,
        address_data: AddressUpdate
    ):
        return repository.update(
            db,
            address_id,
            address_data
        )