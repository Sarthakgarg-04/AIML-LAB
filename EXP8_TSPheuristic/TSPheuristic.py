import tkinter as tk
import random
import math

class TSPGUI:
    def __init__(self, master, cities):
        self.master = master
        self.master.title("Traveling Salesman Problem")
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()

        self.cities = cities
        self.route = []
        self.total_distance = 0

        self.draw_cities()
        self.nearest_neighbor()
        self.draw_route()

    def draw_cities(self):
        for city in self.cities:
            x, y = city
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

    def draw_route(self):
        for i in range(len(self.route) - 1):
            city1 = self.cities[self.route[i]]
            city2 = self.cities[self.route[i + 1]]
            self.canvas.create_line(city1[0], city1[1], city2[0], city2[1], fill="blue")

    def nearest_neighbor(self):
        unvisited = set(range(len(self.cities)))
        current_city = random.choice(list(unvisited))
        unvisited.remove(current_city)
        self.route.append(current_city)

        while unvisited:
            nearest_city = min(unvisited, key=lambda city: self.distance(current_city, city))
            self.route.append(nearest_city)
            unvisited.remove(nearest_city)
            current_city = nearest_city

        self.total_distance = sum(self.distance(self.route[i], self.route[i + 1]) for i in range(len(self.route) - 1))
        self.route.append(self.route[0])  # Complete the cycle

    def distance(self, city1, city2):
        x1, y1 = self.cities[city1]
        x2, y2 = self.cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == "__main__":
    cities = [(100, 100), (200, 200), (300, 100), (400, 300), (500, 200)]

    root = tk.Tk()
    app = TSPGUI(root, cities)
    root.mainloop()
