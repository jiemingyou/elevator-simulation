class Elevator:
    """
    Class representing a single elevator
    """

    _current_capacity = 0
    _max_capacity = 1
    _current_floor = 1


    def __init__(self, max_capacity: int, current_capacity = 0, current_floor = 1):
        self._max_capacity = max_capacity
        self._current_floor = current_floor
        self._capacity_check(current_capacity)
        self._current_capacity = current_capacity


    def _capacity_check(self, current):
        if (current > self._max_capacity) or (self._max_capacity < 1):
            raise ValueError(f"Invalid maximum capacity ({self._max_capacity})")


    def is_full(self):
        return self._max_capacity == self._current_capacity


    def capacity_left(self):
        return self._max_capacity - self._current_capacity


    def enter(self, amount = 1):
        """
        Loads the elevator
        
        Arguments:
            amount: Amount of passangers loading into the elevator
        
        Returns:
            The amount of passangers loaded into the elevator
        """
        capacity = self.capacity_left()

        if capacity >= amount:
            self._current_capacity += amount
            return amount
        
        self._current_capacity += capacity
        return capacity


    def leave(self, amount = 1):
        """
        Unloads the elevator.
        Empties the elevator if amount > current_capacity
        
        Arguments:
            amount: Amount of passangers leaving from the elevator
        
        Returns:
            Capacity left in the elevator
        """
        capacity = self.capacity_left()

        if amount >= capacity:
            self._current_capacity = 0
            return 0

        self._current_capacity -= amount
        return self.capacity_left()

    


if __name__ == "__main__":

    elev1 = Elevator(2, 1)
    print("done!")