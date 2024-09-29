import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Visualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.heart_rate_data = []
        self.line, = self.ax.plot(self.heart_rate_data)

    def update_graph(self, heart_rate):
        self.heart_rate_data.append(heart_rate)
        if len(self.heart_rate_data) > 100:
            self.heart_rate_data.pop(0)

    def animate(self, i):
        self.line.set_ydata(self.heart_rate_data)
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,

    def start_visualization(self):
        ani = FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()