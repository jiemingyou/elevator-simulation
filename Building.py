from Person import Person
import random

class Building:
    """
    Class representing a building with floors and customers
    waiting for the elevator

    Floor numbering starts from 1
    """

    def __init__(self, max_floors):
        self.max_floors = max_floors
        self._init_floors()

    def __repr__(self):
        output = "\n"
        for i in range(1, self.max_floors+1):
            output += f"Floor {i}:\t{len(self.floors[i]) * '*'}\n"
        return output
    
    floors = {}

    def _init_floors(self):
        for i in range(self.max_floors):
            self.floors[i+1] = []

    def wait_times(self) -> list[float]:
        """
        Returns a list of all the wait times
        """
        times = []
        for floor in self.floors.values():
            for person in floor:
                times.append(person.time())
        return times


    def add_person(self, floor=-1, n=1, to=-2):
        """
        Adds persons to a specified floor.
        Default: random parameters
        """
        if floor > self.max_floors or to > self.max_floors or floor == to:
            raise ValueError("Invalid floors!")

        if floor < 1:
            floor = random.randint(1, self.max_floors)

        if to < 1:
            available = list(range(1, self.max_floors+1))
            available.pop(floor-1)
            floor = random.choice(available)
            
        for _ in range(n):
            self.floors[floor].append(Person(floor, to))



if __name__ == "__main__":

    building = Building(4)
    for _ in range(10):
        building.add_person()
    print(building.wait_times())
    print(building)