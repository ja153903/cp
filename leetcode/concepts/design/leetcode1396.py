from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        """
        Keep track of where a customer currently is within a hashmap
        """
        self._users = defaultdict()
        self._trips = defaultdict()

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        self._users[id] = {"id": id, "station_name": station_name, "t": t}

    def checkOut(self, id: int, station_name: str, t: int) -> None:
        start = self._users[id]
        key = (start["station_name"], station_name)
        prev = self._trips.get(key)
        time_spent = t - start["t"]
        if prev:
            self._trips[key] = (prev[0] + time_spent, prev[1] + 1)
        else:
            self._trips[key] = (time_spent, 1)

        del self._users[id]

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        key = (start_station, end_station)
        if key not in self._trips:
            return 0.0

        sum, count = self._trips[key]
        return sum / count
