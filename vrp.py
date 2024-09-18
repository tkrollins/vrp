import math
from dataclasses import dataclass, field
import argparse
from typing import List


@dataclass
class Waypoint:
    x: float
    y: float

    def distance(self, point: "Waypoint") -> float:
        return math.hypot(point.x - self.x, point.y - self.y)


DEPOT = Waypoint(0.0, 0.0)


@dataclass
class Load:
    id: str
    pickup: Waypoint
    dropoff: Waypoint


@dataclass
class Driver:
    loads: List[Load] = field(default_factory=list)

    @property
    def stops(self) -> List[Waypoint]:
        stops = [DEPOT]
        for load in self.loads:
            stops.append(load.pickup)
            stops.append(load.dropoff)
        stops.append(DEPOT)
        return stops

    def total_time(self) -> float:
        """Total time to complete the driver's route"""
        total_time = 0.0
        for i in range(len(self.stops) - 1):
            total_time += self.stops[i].distance(self.stops[i + 1])
        return total_time


def read_loads(filename: str) -> List[Load]:
    loads = []
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines[1:]:
        parts = line.strip().split()
        if not parts:
            continue
        id_, pickup_str, dropoff_str = parts
        pickup_coords = eval(pickup_str)
        dropoff_coords = eval(dropoff_str)
        loads.append(Load(id_, Waypoint(*pickup_coords), Waypoint(*dropoff_coords)))
    return loads


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the problem txt file")
    args = parser.parse_args()

    unassigned_loads = read_loads(args.filename)
    drivers: List[Driver] = []

    while unassigned_loads:
        driver = Driver()
        current_location = DEPOT
        while True:
            # Find the nearest load pickup to the current location
            nearest_load = min(
                unassigned_loads,
                key=lambda load: current_location.distance(load.pickup),
                default=None,
            )
            if nearest_load is None:
                break
            # Tentatively add the load to the driver's route
            driver.loads.append(nearest_load)
            if driver.total_time() <= 720.0:
                unassigned_loads.remove(nearest_load)
                current_location = nearest_load.dropoff
            else:
                # If over time limit, remove the load and end the driver's route
                driver.loads.pop()
                break
        drivers.append(driver)

    # Print solution
    for driver in drivers:
        load_ids = [load.id for load in driver.loads]
        print("[" + ",".join(load_ids) + "]")


if __name__ == "__main__":
    main()
