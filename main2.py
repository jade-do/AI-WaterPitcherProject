from queue import PriorityQueue

class PitcherState:
    def __init__(self, pitchers, infinite_capacity, target):
        self.pitchers = pitchers
        self.infinite_capacity = infinite_capacity
        self.target = target

    def __eq__(self, other):
        return self.pitchers == other.pitchers

    def __hash__(self):
        return hash(tuple(self.pitchers))

    def is_goal(self):
        print("target: " + str(self.target))
        print("pitchers: ")
        print(self.pitchers)
        return self.target in self.pitchers

    def successors(self):
        successors = []

        for i in range(len(self.pitchers)):
            for j in range(len(self.pitchers)):
                if i != j:
                    # Pour water from pitcher i to pitcher j
                    new_pitchers = self.pitchers.copy()
                    transfer_amount = min(new_pitchers[i], self.pitchers[j] - new_pitchers[j])
                    new_pitchers[i] -= transfer_amount
                    new_pitchers[j] += transfer_amount
                    successors.append(PitcherState(new_pitchers, self.infinite_capacity, self.target))

                    # Pour water from infinite pitcher to pitcher j
                    if self.pitchers[i] != 0 and new_pitchers[j] != self.pitchers[j]:
                        new_pitchers = self.pitchers.copy()
                        transfer_amount = min(new_pitchers[i], self.infinite_capacity - new_pitchers[j])
                        new_pitchers[i] -= transfer_amount
                        new_pitchers[j] += transfer_amount
                        successors.append(PitcherState(new_pitchers, self.infinite_capacity, self.target))

        return successors

    def heuristic(self):
        # We can use a simple heuristic: the difference between the target and the current maximum pitcher
        return abs(max(self.pitchers) - self.target)

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state.is_goal():
            # Reconstruct path
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = came_from[current_state]
            path.append(initial_state)
            path.reverse()
            return len(path) - 1  # Number of steps excluding the initial state

        for next_state in current_state.successors():
            new_cost = cost_so_far[current_state] + 1
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + next_state.heuristic()
                frontier.put((priority, next_state))
                came_from[next_state] = current_state

    # If no path is found
    return -1

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        capacities = list(map(int, lines[0].strip().split(',')))
        infinite_capacity = max(capacities)  # Capacity of the virtual infinite pitcher
        target = int(lines[1].strip())
        # print("capacity: ")
        # print(capacities)
        # print("infinite_capacity: " + str(infinite_capacity))
        # print("target: " + str(target))
    return capacities, infinite_capacity, target

def main():
    file_path = 'input/input3.txt'  # Adjust this to your file path
    capacities, infinite_capacity, target = read_input_file(file_path)
    initial_state = PitcherState([0] * len(capacities), infinite_capacity, target)
    steps = a_star_search(initial_state)
    print(steps)

if __name__ == "__main__":
    main()
