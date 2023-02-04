# Missionaries and Cannibals Problem
# Code by Pedro Marinho dos Anjos Feitosa

class state:
    def __init__(self, left_missionaries: int, left_cannibals: int, right_missionaries: int, right_cannibals: int, boat_position: str):
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.right_missionaries = right_missionaries
        self.right_cannibals = right_cannibals
        self.boat_position = boat_position
        self.next_possible_states: list[state] = []
        self.previous_state: state = None
        self.depth = 0

    def is_valid_state(self) -> bool:
        if ((self.left_missionaries < 0) or (self.left_cannibals < 0) or
            (self.right_missionaries < 0) or (self.right_cannibals < 0)):
            return False

        return ((self.left_missionaries == 0 or self.left_missionaries >= self.left_cannibals) and
                (self.right_missionaries == 0 or self.right_missionaries >= self.right_cannibals))

    def generate_next_possible_states(self):
        new_boat_position = "Left" if self.boat_position == "Right" else "Right"

        valid_movements = [
            {'missionaries': 2, 'cannibals': 0},
            {'missionaries': 1, 'cannibals': 0},
            {'missionaries': 1, 'cannibals': 1},
            {'missionaries': 0, 'cannibals': 1},
            {'missionaries': 0, 'cannibals': 2}
        ]

        for movement in valid_movements:
            if self.boat_position == "Left":
                    new_left_missionaries = self.left_missionaries - movement['missionaries']
                    new_left_cannibals = self.left_cannibals - movement['cannibals']
                    new_right_missionaries = self.right_missionaries + movement['missionaries']
                    new_right_cannibals = self.right_cannibals + movement['cannibals']
            else:
                    new_left_missionaries = self.left_missionaries + movement['missionaries']
                    new_left_cannibals = self.left_cannibals + movement['cannibals']
                    new_right_missionaries = self.right_missionaries - movement['missionaries']
                    new_right_cannibals = self.right_cannibals - movement['cannibals']

            new_state = state(new_left_missionaries, new_left_cannibals, new_right_missionaries, new_right_cannibals, new_boat_position)
            new_state.previous_state = self
            new_state.depth = self.depth + 1

            if new_state.is_valid_state():
                self.next_possible_states.append(new_state)

    def is_solution(self):
        if self.left_missionaries == self.left_cannibals == 0:
            return True
        else:
            return False 

    def __str__(self):

        return f"Step: {self.depth} | " \
                f"Boat position: {self.boat_position} | " \
                f"Left missionaries: {self.left_missionaries} | " \
                f"Left cannibals: {self.left_cannibals} | " \
                f"Right missionaries: {self.right_missionaries} | " \
                f"Right cannibals: {self.right_cannibals}"

def generate_solution(final_state) -> list[state]:
    solution_steps: list[state] = []
    current_state: state = final_state

    solution_steps.append(current_state)

    while current_state.previous_state:
        current_state = current_state.previous_state
        solution_steps.append(current_state)
    
    solution_steps.reverse()

    return solution_steps

def print_solution(solution):
    print("-------- SOLUTION --------")
    
    if not solution:
        print("Error: An error has occurred while computing the solution.")
    else:
        for step in solution:
            print(step)
            print("-" * 120)

def main():
    initial_state: state = state(3, 3, 0, 0, "Left")
    frontier: list[state] = []
    solution: list[state] = []
    frontier.append(initial_state)

    while frontier:
        current_state = frontier.pop(0)
        
        if current_state.is_solution():
            solution = generate_solution(current_state)
            break

        current_state.generate_next_possible_states()

        frontier.extend(current_state.next_possible_states)

    print_solution(solution)

if __name__ == "__main__":
    main()
