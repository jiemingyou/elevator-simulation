from person import Person

class Elevator:
    """
    Class representing a single elevator.
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


    def _log_time(self):
        for p in self._passangers:
            p.add_elevator_time()




    def __str__(self):
        """
        Visualize the elevator
        """
        output = ""
        output += 6*"-" + "\n"
        for i in range((self._max_floor - self._min_floor),-1,-1):
            if (i+1 == self._current_floor):
                output += f"{i+1: <3} {self.capacity()}\n"
            else:
                output += f"{i+1: <3} |\n"
        output += 6*"-"
        return output


    # Passanger count
    def capacity(self):
        return len(self._passangers)


    def is_full(self):
        return self._max_capacity == self.capacity()()


    def capacity_left(self):
        return self._max_capacity - self.capacity()

    
    # Current floor
    def floor(self):
        return self._current_floor

    def is_min_floor(self):
        return self._current_floor == self._min_floor

    def is_max_floor(self):
        return self._current_floor == self._max_floor
    

    def move_up(self, log=True, error=True):
        """
        Moves up the elevator.
        Logs passanger travel time.
        
        Returns:
            New floor of the elevator
        """
        if log:
            self._log_time()

        if self._current_floor >= self._max_floor:
            if error:
                raise ValueError("Already top floor")
            else:
                return

        self._current_floor += 1
        return self._current_floor

    
    def move_down(self, log=True, error=True):
        """
        Moves down the elevator.
        Logs passanger travel time.
        
        Returns:
            New floor of the elevator
        """
        if log:
            self._log_time()

        if self._current_floor <= self._min_floor:
            if error:
                raise ValueError("Already bottom floor")
            else:
                return

        self._current_floor -= 1
        return self._current_floor


    def enter(self, persons: list[Person]):
        """
        Loads the elevator
        
        Arguments:
            persons: List of Persons
        
        Returns:
            List of people boarded into the elevator
        """
        capacity = self.capacity_left()
        amount = len(persons)

        if capacity >= amount:
            self._passangers += persons
            return persons
        
        self._passangers += persons[0:capacity]
        return persons[0:capacity]


    def leave(self):
        """
        Unloads the elevator.
        Person leaves if the current floor is the desired floor
        
        Returns:
            List of peoples who left the elevator
        """
        leaving = [x for x in self._passangers if x.to() == self._current_floor]
        self._passangers = [x for x in self._passangers if x not in leaving]
        return leaving

    def enter_leave(self, persons: list[Person] = [], log=True):
        """
        Combines the enter and leave functions.

        Returns:
            A tuple of people who left the elevator and people boarded into the elevator
        """
        if log:
            self._log_time()

        left = self.leave()
        enter = self.enter(persons)

        return (left, enter)

if __name__ == "__main__":

    # Setting up the elevator
    person1 = Person(2, 5)
    elevator1 = Elevator(max_capacity=2, min_floor=1, max_floor=6, current_floor=1)
    print(elevator1)

    # Move up to floor 2
    elevator1.move_up()
    print(elevator1)

    # Enter the passanger
    elevator1.enter_leave([person1])
    print(elevator1)

    # Move up to floor 5
    for i in range(3):
        elevator1.move_up()
    print(elevator1)

    # Leave the passanger
    elevator1.enter_leave()
    print(elevator1)

    # Print the total travel time
    print(person1.time())