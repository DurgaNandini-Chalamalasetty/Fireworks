import turtle
import random
import math
import time
import json

#this loads the colors from json file
def load_colors(filename='colors.json'):
    with open(filename, 'r') as file:
        return json.load(file)

colors = load_colors()

# setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600) 
screen.tracer(0, 0) 

# Function to convert color names to rgb tuples
def color_to_rgb(color_name):
    rgb = colors.get(color_name, [1, 1, 1])
    return tuple(rgb)

# Particle class for firework explosion
class Particle(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.15)

        self.color(color_to_rgb(color))
        self.goto(x, y)
        self.speed(0)
        self.velocity = random.uniform(1, 5)
        self.angle = random.uniform(0, 360)

        self.original_color = color_to_rgb(color) 
        self.fade = 255  
        self.pensize(5)

    def move(self):
        # direction for particle movement
        angle_radians = math.radians(self.angle)
        dx = self.velocity * math.cos(angle_radians)
        dy = self.velocity * math.sin(angle_radians)
        self.goto(self.xcor() + dx, self.ycor() + dy)

        # fading out
        self.fade -= 6
        if self.fade < 0:
            self.hideturtle()
        else:
            fade_color = (self.original_color[0] * (self.fade / 255),
                          self.original_color[1] * (self.fade / 255),
                          self.original_color[2] * (self.fade / 255))
            self.color(fade_color)

# Firework class that simulates the burst
class Firework:
    def __init__(self, x, y):
        self.particles = []
        self.explode(x, y)

    def explode(self, x, y):
        color_names = list(colors.keys())
        particle_color = random.choice(color_names)
        for _ in range(70): 
            particle = Particle(x, y, particle_color)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            particle.move()

# holds different fireworks
fireworks = []

def create_firework():
    x = random.randint(-300, 300)
    y = random.randint(-100, 300)
    firework = Firework(x, y)
    fireworks.append(firework)

def main():
    try:
        while True:
            if random.randint(1, 10) == 1:  
                create_firework()

            for firework in fireworks:
                firework.update()

            screen.update() 
            time.sleep(0.05)  

    except turtle.Terminator:
        print('Window closed')


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        print('Turtle graphics window closed.')