from person import Person

class Elevator:
    """
    Class representing a single elevator
    """

    _max_capacity = 1
    _current_floor = 1
    _min_floor = 0
    _max_floor = 1
    _passangers: list[Person] = [] 


    def __init__(self, max_capacity: int, min_floor: int, max_floor:int, current_floor = 1):
        self._max_capacity = max_capacity
        self._current_floor = current_floor
        self._min_floor = min_floor
        self._max_floor = max_floor
        self._input_check()


    def _input_check(self):
        if (self.capacity() > self._max_capacity) or (self._max_capacity < 1):
            raise ValueError(f"Invalid maximum capacity ({self._max_capacity})")
        
        if not (self._min_floor <= self._current_floor <= self._max_floor):
            raise ValueError(f"Invalid floor parameters\nmin: {self._min_floor}\nmax: {self._max_floor}\ncurrent: {self._current_floor}")




    def _move_up(self):
        """
        Moves up the elevator.
        
        Returns:
            New floor of the elevator
        """
        if self._current_floor >= self._max_floor:
            raise ValueError("Already top floor")

        self._current_floor += 1
        return self._current_floor

    
    def _move_down(self):
        """
        Moves down the elevator.
        
        Returns:
            New floor of the elevator
        """
        if self._current_floor <= self._min_floor:
            raise ValueError("Already bottom floor")

        self._current_floor -= 1
        return self._current_floor


    def __str__(self):
        """
        Visualize the elevator
        """
        output = ""
        output += 6*"-" + "\n"
        for i in range((self._max_floor - self._min_floor),-1,-1):
            if (i+1 == self._current_floor):
                output += f"{i+1: <3} X\n"
            output += f"{i+1: <3} |\n"
        output += 6*"-"
        return output


    def capacity(self):
        return len(self._passangers)


    def is_full(self):
        return self._max_capacity == self.capacity()()


    def capacity_left(self):
        return self._max_capacity - self.capacity()

    
    def floor(self):
        return self._current_floor
    

    def enter(self, persons: list[Person]):
        """
        Loads the elevator
        
        Arguments:
            persons: List of Persons
        
        Returns:
            List of oeople NOT boarded into the elevator
        """
        capacity = self.capacity_left()
        amount = len(persons)

        if capacity >= amount:
            self._passangers += persons
            return []
        
        self._passangers += persons[0:capacity]
        return persons[capacity:]


    def leave(self):
        """
        Unloads the elevator.
        Person leaves if the current floor is the desired floor
        
        Returns:
            List of peoples who left the elevator
        """
        leaving = [x for x in self._passangers if x.to == self._current_floor]
        self.passangers = [x for x in self._passangers if x not in leaving]
        return leaving



if __name__ == "__main__":

    person1 = Person(2, 5)
    elev1 = Elevator(2, 1, 6, 1)
    print(elev1)