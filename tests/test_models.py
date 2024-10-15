"""Test to ensure models are correct."""

import unittest
from sales.models import Customer
import pydantic_core


class TestModels(unittest.TestCase):
    """Test for model initialization and validation."""

    def test_customer(self):
        """Validate Customer dataclass."""
        with self.assertRaises(pydantic_core._pydantic_core.ValidationError):
            Customer(customer_id="Wendell Fish", location_id="10")


if __name__ == "__main__":
    unittest.main()
