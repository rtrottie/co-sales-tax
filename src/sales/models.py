"""Pydantic models common to multiple processes."""

from pydantic import Field, field_validator, BaseModel


class Customer(BaseModel):
    """Contains Necessary information to define a customer for tax purposes."""

    customer_id: str
    location_id: str = Field(None, min_length=6, max_length=6)

    @field_validator("location_id")
    @classmethod
    def location_id_must_be_digit(cls, customer_id: str) -> str:
        """Location ID is a 6-digit number."""
        if not customer_id.isdigit():
            raise ValueError("Must be all digits")
        return customer_id
