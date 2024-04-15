from collections import deque
import matplotlib.pyplot as plt

def jug_diagram_visualize(a, b, jug1, jug2):
    finalx = jug1 - a
    finaly = jug2 - b
    key = ['Jug 1', 'Jug 2']
    list1 = [a, b]
    list2 = [finalx, finaly]
    plt.bar(key, list1, color=['blue', 'green'])
    plt.bar(key, list2, bottom=list1, color=['white', 'white'],edgecolor='black')
    plt.xlabel("Jugs")
    plt.ylabel("Amount of Water (in L)")
    plt.title("Water Jug Problem")
    plt.show()
    
def water_jug_solver_visualize_bfs(jug1, jug2, goal):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        current_state = queue.popleft()
        jug_diagram_visualize(current_state[0], current_state[1], jug1,jug2)
        if current_state[0] == goal or current_state[1] == goal:
            print("Goal achieved!")
            break
        visited.add(current_state)
        next_states = [

(jug1, current_state[1]), 
(current_state[0], jug2), 
(0, current_state[1]), 
(current_state[0], 0), 
(max(0, current_state[0] - (jug2 - current_state[1])),
min(jug2, current_state[1] + current_state[0])), # Pour Jug1 to Jug2
(min(jug1, current_state[0] + current_state[1]), 
 max(0, current_state[1] - (jug1 - current_state[0])))]
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)


if __name__ == "__main__":
    try:
        jug1_capacity = int(input("Enter capacity of Jug 1: "))
        jug2_capacity = int(input("Enter capacity of Jug 2: "))
        goal_amount = int(input("Enter the desired amount to measure:"))
        if jug1_capacity <= 0 or jug2_capacity <= 0 or goal_amount < 0:
            raise ValueError("Capacity and goal must be positive integers.")
        print("\nSteps:")
        water_jug_solver_visualize_bfs(jug1_capacity, jug2_capacity,goal_amount)
    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")    
