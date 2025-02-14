from dataclasses import dataclass, field
from datetime import date
from typing import List
import copy

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zip_code: str

@dataclass(frozen=True)
class Employee:
    name: str
    Id: str
    dateOfJoining: date
    addresses: List[Address] = field(default_factory=list)

    def __post_init__(self):
      
        object.__setattr__(self, "addresses", tuple(copy.deepcopy(self.addresses)))

address1 = Address("123 Main St", "New York", "NY", "10001")
address2 = Address("456 Maple Rd", "Los Angeles", "CA", "90001")

employee = Employee(name="John Doe", Id="E12345", dateOfJoining=date(2020, 5, 15), addresses=[address1, address2])

print(employee)


