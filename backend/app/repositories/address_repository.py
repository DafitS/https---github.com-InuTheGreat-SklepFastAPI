from sqlalchemy.orm import Session

from app.models.address import Address
from app.schemas.address import AddressUpdate

class AddressRepository:

    def create(
            self,
            db: Session,
            address: Address
    ):
        db.add(address)
        db.commit()
        db.refresh(address)

        return address

    def get_all(
            self,
            db: Session
    ):
        return db.query(Address).all()

    def get_by_id(
            self,
            db: Session,
            address_id: int
    ):
        return (
            db.query(Address)
            .filter(Address.id == address_id)
            .first()
        )

    def delete_by_id(
            self,
            db: Session,
            address_id: int 
    ):
        found_address = self.get_by_id(db, address_id)

        if found_address is None:
            return False

        db.delete(found_address)
        db.commit()

        return True

    def update(
        self,
        db: Session,
        address_id: int,
        address_data: AddressUpdate
    ):
        address = self.get_by_id(
            db,
            address_id
        )

        if address is None:
            return None

        address.street = address_data.street
        address.house_number = address_data.house_number
        address.apartment_number = address_data.apartment_number
        address.postal_code = address_data.postal_code
        address.city = address_data.city
        address.country = address_data.country
        address.company_name = address_data.company_name
        address.tax_number = address_data.tax_number

        db.commit()
        db.refresh(address)

        return address    