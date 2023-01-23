class Person:
    """
    A person that travels from a floor to another
    """

    _at = 0
    _to = 1
    _waiting_time = 0
    _time_in_elevator = 0

    def __init__(self, at: int, to: int):
        self._at = at
        self._to = to
    
    def _add_wait_time(self):
        self._waiting_time += 1
    
    def _add_elevator_time(self):
        self._time_in_elevator += 1

    def at(self):
        return self._at

    def to(self):
        return self._to


    