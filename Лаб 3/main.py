from ports import Port
from containers import container_factory
from ships import Ship, ShipBuilder

def main():
    # Створення порту
    port = Port(id=1, coordinates=(50.0, 30.0))
    print(f"Port created with ID: {port.id} and coordinates: {port.coordinates}")

    # Створення контейнерів
    container1 = container_factory(1, 'basic', 1960)  # Легкий контейнер
    print(f"Container created: {container1.to_dict()}")

    # Створення судна
    ship_builder = ShipBuilder()
    ship = ship_builder.set_id(101).set_max_weight(10000).build()
    print(f"Ship created with ID: {ship.id} and max weight: {ship.max_weight}")

    # Завантаження контейнера на судно
    ship.load_container(container1)

    # Обчислення загального споживання пального
    total_consumption = ship.total_consumption()
    print(f"Total fuel consumption for the ship: {total_consumption}")

if __name__ == "__main__":
    main()
