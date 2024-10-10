from containers import Container
from typing import List, Dict

class Ship:
    """Class representing a ship that carries containers."""

    def __init__(self, id: int, max_weight: float) -> None:
        """Initializes a Ship instance."""
        self.id = id
        self.max_weight = max_weight
        self.containers: List[Container] = []

    def load_container(self, container: Container) -> None:
        """Loads a container onto the ship if the weight limit allows."""
        total_weight = sum(c.weight for c in self.containers) + container.weight
        if total_weight <= self.max_weight:
            self.containers.append(container)
            print(f"Container {container.id} loaded into Ship {self.id}.")
        else:
            print(f"Cannot load container {container.id}: exceeds weight limit.")

    def unload_container(self, container: Container) -> None:
        """Unloads a container from the ship."""
        if container in self.containers:
            self.containers.remove(container)
            print(f"Container {container.id} unloaded from Ship {self.id}.")
        else:
            print(f"Container {container.id} not found on Ship {self.id}.")

    def total_consumption(self) -> float:
        """Calculates the total fuel consumption based on the containers on board."""
        return sum(container.consumption() for container in self.containers)

    def to_dict(self) -> Dict:
        """Converts the Ship instance to a dictionary representation."""
        return {
            "id": self.id,
            "max_weight": self.max_weight,
            "containers": [container.to_dict() for container in self.containers]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Ship':
        """Creates a Ship instance from a dictionary."""
        ship = Ship(data['id'], data['max_weight'])
        ship.containers = [Container.from_dict(c) for c in data['containers']]
        return ship

class ShipBuilder:
    """Builder class to construct Ship instances with specific attributes."""

    def __init__(self):
        """Initializes the ShipBuilder with a default Ship instance."""
        self._ship = Ship(id=0, max_weight=0)

    def set_id(self, id: int) -> 'ShipBuilder':
        """Sets the ID for the ship."""
        self._ship.id = id
        return self

    def set_max_weight(self, max_weight: float) -> 'ShipBuilder':
        """Sets the maximum weight capacity for the ship."""
        self._ship.max_weight = max_weight
        return self

    def build(self) -> Ship:
        """Finalizes and returns the constructed Ship instance."""
        return self._ship
