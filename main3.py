from queue import PriorityQueue

class PitcherState:
    def __init__(self, pitchers, infinite_pitcher):
        self.pitchers = pitchers
        self.infinite_pitcher = infinite_pitcher
        # self.g_n = g_n  # g(n) cost to go from previous state to current state

    def __lt__(self, other):
        return (sum(self.pitchers) + self.infinite_pitcher) > (sum(other.pitchers) + other.infinite_pitcher)

    def __eq__(self, other):
        return self.pitchers == other.pitchers and self.infinite_pitcher == other.infinite_pitcher

    def __hash__(self):
        hashObj = self.pitchers.copy()
        hashObj.append(self.infinite_pitcher)
        return hash(tuple(hashObj))
        #return hash(tuple(self.pitchers))

    # def __str__(self):
    #     return str(self.pitchers) + '  infinite_pitcher: ' + str(self.infinite_pitcher) + ' heuristic: ' + str(self.heuristic())

    def is_goal(self):
        print("infinite_pitcher: " + str(self.infinite_pitcher))
        print("pitchers: ")
        print(self.pitchers)
        return self.infinite_pitcher == target

    def heuristic(self):
        # We can use a simple heuristic: the difference between the target and the current maximum pitcher
        # Alternative:
        # if sum(self.pitchers) + self.infinite_pitcher == 0:
        #     return target
        # else:
        #     return abs(target - self.infinite_pitcher) / (sum(self.pitchers) + self.infinite_pitcher)
        return abs(target - self.infinite_pitcher)

    def successors(self):
        successors = []

        for i in range(len(self.pitchers)):
            # Fill jug i
            new_pitchers = self.pitchers.copy()
            new_pitchers[i] = capacities[i]
            # Empty jug i into infinite_pitcher
            self.infinite_pitcher += self.pitchers[i]
            self.pitchers[i] = 0
            successors.append(PitcherState(new_pitchers, self.infinite_pitcher))

        return successors

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}

    loop_count = 0

    while not frontier.empty():
        _, current_state = frontier.get()
        loop_count += 1
        print("Loop #: " + str(loop_count))
        print("Current_state: " )
        print(current_state)
        print("Cost: ")
        print(cost_so_far[current_state])

        if current_state.is_goal():
            # Reconstruct path
            # print("goal: " + str(current_state.infinite_pitcher))
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = came_from[current_state]
            path.append(initial_state)
            path.reverse()
            return len(path) - 1  # Number of steps excluding the initial state


        for next_state in current_state.successors():

            if current_state not in cost_so_far:
                print("=================================================")
                print("Error: Current State Not In Cost So Far")
                print(current_state)
                print(cost_so_far)
                print("=================================================")

            # new_cost = cost_so_far[current_state] + next_state.g_n + next_state.heuristic()
            new_cost = cost_so_far[current_state] + 1

            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                # cost_so_far.update({next_state: new_cost})
                cost_so_far[next_state] = new_cost
                frontier.put((new_cost, next_state))
                came_from[next_state] = current_state

    return -1

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        capacities = list(map(int, lines[0].strip().split(',')))
        target = int(lines[1].strip())
    return capacities, target

def main():
    global capacities
    global target
    file_path = 'input/input5.txt'  # Adjust this to your file path

    capacities, target = read_input_file(file_path)
    initial_state = PitcherState([0] * len(capacities), 0)
    steps = a_star_search(initial_state)
    print(steps)

if __name__ == "__main__":
    main()
