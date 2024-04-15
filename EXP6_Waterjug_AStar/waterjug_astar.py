from queue import PriorityQueue

class State:
    def __init__(self, jugs, parent=None, action=None):
        self.jugs = jugs
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def __eq__(self, other):
        return self.jugs == other.jugs
    
    def __lt__(self, other):
        return self.depth < other.depth
    
    def __hash__(self):
        return hash(tuple(self.jugs))
    
    def is_goal(self, target):
        return target in self.jugs
    
    def successors(self, capacities):
        successors = []
        for i, jug in enumerate(self.jugs):
            # Fill the jug
            if jug < capacities[i]:
                new_jugs = self.jugs[:]
                new_jugs[i] = capacities[i]
                successors.append(State(new_jugs, self, f"Fill jug {i + 1}"))
            # Empty the jug
            if jug > 0:
                new_jugs = self.jugs[:]
                new_jugs[i] = 0
                successors.append(State(new_jugs, self, f"Empty jug {i + 1}"))
            # Pour from one jug to another
            for j, other_jug in enumerate(self.jugs):
                if i != j:
                    amount_to_pour = min(jug, capacities[j] - other_jug)
                    if amount_to_pour > 0:
                        new_jugs = self.jugs[:]
                        new_jugs[i] -= amount_to_pour
                        new_jugs[j] += amount_to_pour
                        successors.append(State(new_jugs, self, f"Pour from jug {i + 1} to jug {j + 1}"))
        return successors

def heuristic(state, target):
    return sum(abs(jug - target[i]) for i, jug in enumerate(state.jugs))

def astar_search(initial, target, capacities):
    frontier = PriorityQueue()
    frontier.put(initial)
    explored = set()
    
    while not frontier.empty():
        current_state = frontier.get()
        if current_state.is_goal(target):
            actions = []
            while current_state.parent:
                actions.append(current_state.action)
                current_state = current_state.parent
            return list(reversed(actions))
        
        explored.add(current_state)
        for successor in current_state.successors(capacities):
            if successor not in explored:
                cost = successor.depth + heuristic(successor, target)
                frontier.put(successor, cost)
    return None

def solve_water_jug_problem(capacities, target):
    initial_state = State([0] * len(capacities))
    actions = astar_search(initial_state, target, capacities)
    if actions:
        print("Solution:")
        for action in actions:
            print(action)
    else:
        print("No solution found.")

# Example usage:
capacities = [5, 3]  # Capacities of the jugs
target = [2, 3]      # Target amounts of water
solve_water_jug_problem(capacities, target)
