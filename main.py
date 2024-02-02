from queue import PriorityQueue

class PitcherState:
    def __init__(self, pitchers, parent, g, h):
        self.pitchers = pitchers
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __lt__(self, other):
        # return (sum(self.pitchers) + self.infinite_pitcher) > (sum(other.pitchers) + other.infinite_pitcher)
        return self.f < other.f

    def __eq__(self, other):
        # return self.pitchers == other.pitchers and self.infinite_pitcher == other.infinite_pitcher
        return self.f == other.f

    def __hash__(self):
        return hash(tuple(self.pitchers))

    def __str__(self):
        return str(self.pitchers) +  ' heuristic: ' + str(self.heuristic(self.pitchers))

    def is_goal(self):
        return self.pitchers[-1] == target

    def heuristic(self):
        return abs(target - self.pitchers[-1])

    def heuristic(self, new_pitchers):
        return abs(target - new_pitchers[-1])

    def successors(self):
        successors = []

        # Option 1: Fill water in 1 jug then transfer to infinite pitcher

        for i in range(len(self.pitchers)-1):
            # Fill jug i
            new_pitchers = self.pitchers.copy()
            if new_pitchers[i] == 0:
                new_pitchers[i] = capacities[i]
                pitcher_state_parent = PitcherState(new_pitchers, self, 1, self.heuristic(new_pitchers))
                #print("1. pitcher_state_parent")
                #print(pitcher_state_parent)
                successors.append(pitcher_state_parent)
                #print_path(successors)

                new_pitchers[-1] += new_pitchers[i]
                new_pitchers[i] = 0
                pitcher_state_child = PitcherState(new_pitchers, pitcher_state_parent, 1, self.heuristic(new_pitchers))
                #print("2. pitcher_state_child")
                #print(pitcher_state_child)
                #print(pitcher_state_child.parent)
                successors.append(pitcher_state_child)
                #print_path(successors)

        # for i in range(len(self.pitchers)-1):
        #     # Empty jug i into infinite_pitcher
        #     new_pitchers = self.pitchers.copy()
        #     if new_pitchers[i] != 0:
        #         new_pitchers[-1] += new_pitchers[i]
        #         new_pitchers[i] = 0
        #         successors.append(PitcherState(new_pitchers, self, 1, self.heuristic()))

        # Option 2: Fill water in 1 jug
        #           then transfer from bigger jug to smaller jug
        #           then transfer water to infinite pitcher

        # Transfer water from jug y to jug x
        # x = 0 (jug x is empty)
        # y > x (jug y currently holds more water than jug x)
        # jug y only fills 1 jug x at the moment
        # will develop algo to fill iteratively more jug x
        #   e.g. 2, 3, 4, 5, .. y - 1
        # for y in range(len(self.pitchers)-2, -1, -1):
        #     # Fill jug y
        #     if new_pitchers[y] == 0:
        #         new_pitchers = self.pitchers.copy()
        #         new_pitchers[y] = capacities[y]
        #         successors.append(PitcherState(new_pitchers, self, 1, self.heuristic(new_pitchers)))
        #
        #         for x in range(y):
        #             # water transfer algorithm
        #             if new_pitchers[y] > capacities[x]:
        #                 new_pitchers[x] = capacities[x]
        #                 new_pitchers[y] = new_pitchers[y] - new_pitchers[x]
        #                 break
        #             successors.append(PitcherState(new_pitchers, self, 1, self.heuristic(new_pitchers)))
        #
        # for i in range(len(self.pitchers)-1):
        #     # Empty jug i into infinite_pitcher
        #     new_pitchers = self.pitchers.copy()
        #     if new_pitchers[i] != 0:
        #         new_pitchers[-1] += new_pitchers[i]
        #         new_pitchers[i] = 0
        #         successors.append(PitcherState(new_pitchers, self, 1, self.heuristic()))

        return successors

def print_path(path):

    for p in path:
        print(p)
        print("->")

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}

    loop_count = 0

    while not frontier.empty():
        _, current_state = frontier.get()
        print("Current state: ")
        print(current_state)

        if current_state.is_goal():
            # Reconstruct path
            # print("goal: " + str(current_state.infinite_pitcher))
            print("Found goal! \n Path is: \n")
            path = []
            while current_state != initial_state:
                path.append(current_state)
                current_state = came_from[current_state]
                # current_state = current_state.parent
            path.append(initial_state)
            path.reverse()
            print_path(path)
            return len(path) - 1  # Number of steps excluding the initial state


        for next_state in current_state.successors():
            print("Next_state: ")
            print(next_state)

            new_cost = cost_so_far[current_state] + next_state.f

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
    print(capacities)
    print(target)
    capacities = sorted(capacities)
    initial_state = PitcherState([0] * (len(capacities) + 1), None, 0, target)
    steps = a_star_search(initial_state)
    print(steps)

if __name__ == "__main__":
    main()
