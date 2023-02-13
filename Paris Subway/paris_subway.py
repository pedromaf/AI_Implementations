class station:
    def __init__(self, id:int, lines:list[str]) -> None:
        self.__id:int = id
        self.__lines: list[str] = lines
        self.__visited:bool = False
        self.__neighbors:list[tuple[station, int]] = []

    def get_neighbors(self) -> list[tuple[object, int]]:
        return self.__neighbors

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
        
        if self.__neighbors:
            string += f"Neighbor stations:\n"
            for station in self.__neighbors:
                string += f"- station {station[0].get_id() + 1} [distance: {station[1]} Km]\n"

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

def main() -> None:
    subway:list[station] = build_subway()

    print_subway(subway)

if __name__ == "__main__":
    main()
