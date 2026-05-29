from dataclasses import dataclass
from enum import Enum
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    operating_system: OperatingSystem


laptops = [
    Laptop(1, "Dell", "XPS", OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", OperatingSystem.MACOS),
]


name = input("Name: ")

try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age", file=sys.stderr)
    sys.exit(1)

os_input = input(
    "Operating System (Ubuntu, Arch Linux, macOS): "
)

os_map = {
    "Ubuntu": OperatingSystem.UBUNTU,
    "Arch Linux": OperatingSystem.ARCH,
    "macOS": OperatingSystem.MACOS,
}

if os_input not in os_map:
    print("Invalid operating system", file=sys.stderr)
    sys.exit(1)

preferred_os = os_map[os_input]

person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_os
)

matching_laptops = [
    laptop
    for laptop in laptops
    if laptop.operating_system == preferred_os
]

print(
    f"There are {len(matching_laptops)} laptops "
    f"available for {preferred_os.value}"
)

counts: dict[OperatingSystem, int] = {}

for laptop in laptops:
    counts[laptop.operating_system] = (
        counts.get(laptop.operating_system, 0) + 1
    )

best_os = max(counts, key=lambda os: counts[os])


if best_os != preferred_os:
    print(
        f"If you're willing to accept "
        f"{best_os.value}, there are "
        f"{counts[best_os]} laptops available."
    )
