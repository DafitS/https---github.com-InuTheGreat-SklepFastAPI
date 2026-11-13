from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.address import (
    AddressCreate,
    AddressUpdate,
    AddressResponse
)

from app.services.address_service import (
    AddressService
)

router = APIRouter(
    prefix="/addresses",
    tags=["Addresses"]
)

service = AddressService()


@router.post("/", response_model=AddressResponse)
def create_address(
    address: AddressCreate,
    db: Session = Depends(get_db)
):
    return service.create(
        db,
        address
    )


@router.get("/", response_model=list[AddressResponse])
def get_addresses(
    db: Session = Depends(get_db)
):
    return service.get_all(db)


@router.get(
    "/{address_id}",
    response_model=AddressResponse
)
def get_address(
    address_id: int,
    db: Session = Depends(get_db)
):
    address = service.get_by_id(
        db,
        address_id
    )

    if not address:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    return address


@router.put(
    "/{address_id}",
    response_model=AddressResponse
)
def update_address(
    address_id: int,
    address_data: AddressUpdate,
    db: Session = Depends(get_db)
):
    address = service.update(
        db,
        address_id,
        address_data
    )

    if not address:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    return address


@router.delete("/{address_id}")
def delete_address(
    address_id: int,
    db: Session = Depends(get_db)
):
    result = service.delete_by_id(
        db,
        address_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    return {
        "message": "Address deleted"
    }