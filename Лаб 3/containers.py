from abc import ABC, abstractmethod
from typing import Dict

class Container(ABC):
    """Abstract base class for containers."""

    def __init__(self, id: int, weight: float) -> None:
        """Initializes a Container instance."""
        self.id = id
        self.weight = weight

    @abstractmethod
    def consumption(self) -> float:
        """Abstract method to calculate fuel consumption."""
        pass

    def to_dict(self) -> Dict:
        """Converts the Container instance to a dictionary representation."""
        return {
            "type": self.__class__.__name__,
            "id": self.id,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Container':
        """Creates a Container instance from a dictionary."""
        # Replace with specific subclasses according to your implementation
        # Sample implementation provided below
        return BasicContainer(data['id'], data['weight'])

class BasicContainer(Container):
    """Class representing a basic container."""
    UNIT_CONSUMPTION = 2.5

    def consumption(self) -> float:
        """Calculates fuel consumption for basic containers."""
        return BasicContainer.UNIT_CONSUMPTION * self.weight

# Define other container types (HeavyContainer, RefrigeratedContainer, LiquidContainer) similarly...

def container_factory(id: int, type_: str, weight: float) -> Container:
    """Factory function to create a container based on its weight and type."""
    if type_ == 'basic':
        return BasicContainer(id, weight)
    # Add logic for other types of containers...
    return BasicContainer(id, weight)  # Default return
