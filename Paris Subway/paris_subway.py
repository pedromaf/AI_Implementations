from queue import PriorityQueue

TRAIN_VELOCITY:int = 30
LINE_CHANGE_TIME:int = 4

class station:
    def __init__(self, id:int, lines:list[str]) -> None:
        self.__id:int = id
        self.__lines: list[str] = lines
        self.__distance:int = 0
        self.__previous:station = None
        self.__next:station = None
        self.__visited:bool = False
        self.__neighbors:list[tuple[station, int]] = []

    def set_neighbors(self, list:list[tuple[object, int]]) -> None:
        self.neighbors = list

    def set_distance(self, distance:int) -> None:
        self.__distance = distance

    def get_distance(self) -> int:
        return self.__distance

    def set_next(self, next) -> None:
        self.__next = next
    
    def get_next(self):
        return self.__next

    def set_previous(self, previous) -> None:
        self.__previous = previous
    
    def get_previous(self):
        return self.__previous

    def get_neighbors(self):
        return self.__neighbors

    def get_lines(self) -> list[str]:
        return self.__lines.copy()

    def add_neighbor_station(self, neighbor_station, distance:int) -> None:
            if not self.contains_neighbor(neighbor_station):
                self.__neighbors.append((neighbor_station, distance))

            if not neighbor_station.contains_neighbor(self):
                neighbor_station.add_neighbor_station(self, distance)

    def contains_neighbor(self, neighbor) -> bool:
        if not self.__neighbors:
            return False

        for station in self.__neighbors:
            if station[0].get_id() == neighbor.get_id():
                return True
        
        return False
        
    def set_visited(self, value:bool) -> None:
        self.__visited = value

    def is_visited(self) -> bool:
        return self.__visited
    
    def get_id(self) -> int:
        return self.__id

    def __str__(self) -> str:
        string:str = f"--- Station {self.__id + 1} ---\n"
        
        string += f"Distance to destination: {self.__destination_distance}\n"

        if self.__neighbors:
            string += f"Neighbor stations:\n"
            for station in self.__neighbors:
                string += f"- station {station[0].get_id() + 1} [distance: {station[1]} Km]\n"

        return string

    def __eq__(self, other) -> bool:
        if not other:
            return False

        return self.__distance == other.get_distance()

    def __lt__(self, other) -> bool:
        return self.__distance < other.get_distance()


class solution:
    def __init__(self) -> None:
        self.__route:list[station] = []
        self.__total_time_minutes:float = 0

    def add_station(self, station:station) -> None:
        self.__route.append(station)

    def increase_total_time(self, minutes) -> None:
        self.__total_time_minutes += minutes

    def __str__(self) -> str:
        string:str = ""
    
        if self.__route:
            self.__route.reverse()

            for station in self.__route:
                string += f"Station {station.get_id() + 1}"

                if station.get_next() != None:
                    string += " -> "

            string += f"\nTotal route time: {self.__total_time_minutes} minutes."
        
        return string


def build_subway() -> list[station]:
    distances = get_distances_table()
    stations: list[station] = []

    stations.append(station(0, ["Blue"]))
    stations.append(station(1, ["Blue", "Yellow"]))
    stations.append(station(2, ["Blue", "Red"]))
    stations.append(station(3, ["Blue", "Green"]))
    stations.append(station(4, ["Blue", "Yellow"]))
    stations.append(station(5, ["Blue"]))
    stations.append(station(6, ["Yellow"]))
    stations.append(station(7, ["Yellow", "Green"]))
    stations.append(station(8, ["Yellow", "Red"]))
    stations.append(station(9, ["Yellow"]))
    stations.append(station(10, ["Red"]))
    stations.append(station(11, ["Green"]))
    stations.append(station(12, ["Green", "Red"]))
    stations.append(station(13, ["Green"]))
    
    stations[0].add_neighbor_station(stations[1], distances[0][1])

    stations[1].add_neighbor_station(stations[2], distances[1][2])
    stations[1].add_neighbor_station(stations[8], distances[1][8])
    stations[1].add_neighbor_station(stations[9], distances[1][9])
    
    stations[2].add_neighbor_station(stations[3], distances[2][3])
    stations[2].add_neighbor_station(stations[8], distances[2][8])
    stations[2].add_neighbor_station(stations[12], distances[2][12])

    stations[3].add_neighbor_station(stations[4], distances[3][4])
    stations[3].add_neighbor_station(stations[7], distances[3][7])
    stations[3].add_neighbor_station(stations[12], distances[3][12])

    stations[4].add_neighbor_station(stations[5], distances[4][5])
    stations[4].add_neighbor_station(stations[6], distances[4][6])
    stations[4].add_neighbor_station(stations[7], distances[4][7])

    stations[7].add_neighbor_station(stations[8], distances[7][8])
    stations[7].add_neighbor_station(stations[11], distances[7][11])

    stations[8].add_neighbor_station(stations[10], distances[8][10])

    stations[12].add_neighbor_station(stations[13], distances[12][13])

    return stations

def print_subway(subway:list[station]) -> None:
    for station in subway:
        print(station)

def get_distances_table() -> list[list[int]]:
    return [[0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
    [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
    [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
    [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
    [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],
    [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20,],
    [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17],
    [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30],
    [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28],
    [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23],
    [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39],
    [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37],
    [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5],
    [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0]]

def get_common_line(station1:station, station2:station) -> str:
    station1_lines:list[str] = station1.get_lines()
    station2_lines:list[str] = station2.get_lines()

    for line_s1 in station1_lines:
        for line_s2 in station2_lines:
            if line_s1 == line_s2:
                return line_s1
    
    return None

def build_solution(final_station:station) -> solution:
    distances = get_distances_table()
    new_solution: solution = solution()
    current:station = final_station
    previous:station = None
    current_line:str = None

    final_station_lines:list[str] = final_station.get_lines()

    if len(final_station_lines) == 1:
        current_line = final_station_lines.pop()
    else:
        previous = final_station.get_previous()

        if previous != None:
            current_line = get_common_line(previous, final_station)
            previous = None
    
    if current_line == None:
        return None

    while current != None:
        new_solution.add_station(current)
        previous = current.get_previous()

        if previous != None:
            previous.set_next(current)
            new_solution.increase_total_time((distances[previous.get_id()][current.get_id()] / TRAIN_VELOCITY) * 60)
            
            previous_lines = previous.get_lines()

            if current_line not in previous_lines:
                new_solution.increase_total_time(LINE_CHANGE_TIME)

                current_line = get_common_line(current, previous)

        current = previous

    return new_solution

def generate_children(current:station, destination_id:int) -> list[station]:
    neighbors:list[tuple[station, int]] = current.get_neighbors()
    distances = get_distances_table()
    children:list[station] = []

    for neighbor in neighbors:
        if neighbor[0].is_visited():
            continue

        neighbor[0].set_distance(neighbor[1] + distances[neighbor[0].get_id()][destination_id])
        neighbor[0].set_previous(current)
        children.append(neighbor[0])

    return children

def find_best_route(subway:list[station], starting_station_id:int, destination_station_id:int) -> solution:
    pqueue = PriorityQueue()
    children:list[station] = None
    current:station = None

    pqueue.put(subway[starting_station_id])

    while not pqueue.empty():
        current = pqueue.get()
        current.set_visited(True)

        if current.get_id() == destination_station_id:
            return build_solution(current)
        
        children = generate_children(current, destination_station_id)

        for child in children:
            pqueue.put(child)
    
    return None

def main() -> None:
    subway:list[station] = build_subway()
    best_route:solution = None
    starting_station_id:int = 4
    destination_station_id:int = 13

    best_route = find_best_route(subway, starting_station_id, destination_station_id)

    print(best_route)

if __name__ == "__main__":
    main()
