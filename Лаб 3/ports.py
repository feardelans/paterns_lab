import json
from typing import Tuple, List, Dict

class Port:
    """Class representing a port where ships dock and unload containers."""

    def __init__(self, id: int, coordinates: Tuple[float, float]):
        """Initializes a Port instance."""
        self.id = id
        self.coordinates: Tuple[float, float] = coordinates
        self.containers: List = []  # Changed to a generic list
        self.ships: List = []
        self.history: List = []

    def incoming_ship(self, ship):
        """Registers an incoming ship at the port."""
        self.ships.append(ship)
        print(f"Ship {ship.id} has arrived at Port {self.id}.")

    def outgoing_ship(self, ship) -> None:
        """Registers an outgoing ship from the port."""
        if ship in self.ships:
            self.ships.remove(ship)
            self.history.append(ship)
            print(f"Ship {ship.id} has left Port {self.id}.")
        else:
            print(f"Ship {ship.id} is not in Port {self.id}.")

    def save_to_json(self, filename: str) -> None:
        """Saves the port's data to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'Port':
        """Loads a Port instance from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return Port.from_dict(data)

    def to_dict(self) -> Dict:
        """Converts the Port instance to a dictionary representation."""
        return {
            "id": self.id,
            "coordinates": self.coordinates,
            "containers": [],  # Adjust based on your logic
            "ships": [ship.id for ship in self.ships],
            "history": [ship.id for ship in self.history],
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Port':
        """Creates a Port instance from a dictionary."""
        port = Port(data['id'], tuple(data['coordinates']))
        return port
