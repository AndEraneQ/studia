import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import numpy as np
from object import Person, CareTakerPerson
from Vector import Vector2D
from State import HealtyState, ImmunteState, NoSymptomsState, SymptomsState, IState
import random


class Simulation:
    maxx = 100
    maxy = 100
    numofpeople = 100
    withImmute = True
    persons = []
    xdata, ydata, colors = [], [], []
    last_time = 0
    
    def __init__(self, maxx, maxy, numofpeople, withImmute) -> None:
        self.maxx = maxx
        self.maxy = maxy
        self.numofpeople = numofpeople
        self.withImmute = withImmute
        self.fig, self.ax = plt.subplots()
        self.points, = self.ax.plot([], [], 'o')
        self.xdata, self.ydata = [], []
        self.ani = FuncAnimation(self.fig, self.update, frames=np.arange(0, 10000, 1),
                                 init_func=self.init, blit=True, interval=40)
        
    def init(self):
        self.ax.set_xlim(0, self.maxx)
        self.ax.set_ylim(0, self.maxy)
        return self.points,
    
    
    def update(self, frame):
        if len(self.persons) < self.numofpeople:
            for i in range(self.numofpeople - len(self.persons)):
                self.addPerson()
        for person in self.persons:
            person.move()
            if not person.getOnPlane():
                self.persons.remove(person)
                self.addPerson()
        for person in self.persons:
            for another in self.persons:
                if person.isNear(another) and person != another:
                    if person.whenNearUnhealthy(another):
                        break
            person.checkState()
            person.checkRecover()
        self.xdata.clear()
        self.ydata.clear()
        self.colors.clear()
        for person in self.persons:
            if isinstance(person, Person):
                self.xdata.append(person.getX())
                self.ydata.append(person.getY())
                self.colors.append(person.getColor())
        self.points = self.ax.scatter(self.xdata, self.ydata, c=self.colors)
        return self.points,
    

    def show_animation(self):
        
        plt.subplots_adjust(bottom=0.2)
        button_ax1 = plt.axes([0.7, 0.05, 0.1, 0.075])
        button1 = Button(button_ax1, 'save')
        button_ax2 = plt.axes([0.81, 0.05, 0.1, 0.075])
        button2 = Button(button_ax2, 'restore')

        def on_button1_clicked(event):
            careTaker = CareTakerPerson()
            careTaker.backup(self.persons)
            careTaker.save()

        def on_button2_clicked(event):
            careTaker = CareTakerPerson()
            careTaker.restore()
            self.persons.clear()
            mementos = careTaker.getMementos()
            for memento in mementos:
                p = Person(NoSymptomsState())
                p.restoreFromMemento(memento)
                self.persons.append(p)
        

            
        button1.on_clicked(on_button1_clicked)
        button2.on_clicked(on_button2_clicked) 
        plt.show()

    def generatePopulation(self, n):
        for i in range(n):
            x = random.randint(0, self.maxx)
            y = random.randint(0, self.maxy)
            p = Person(HealtyState(), x, y, self.maxx, self.maxy)
            self.persons.append(p)
            self.xdata.append(x)
            self.ydata.append(y)
            self.colors.append(p.getColor())
            
    def addPerson(self):
        x : int
        y : int
        p : Person
        propability = random.random()
        if propability < 0.25:
            x = 0
            y = random.randint(0, self.maxy)
        elif propability < 0.5:
            x = random.randint(0, self.maxx)
            y = 0
        elif propability < 0.75:
            x = self.maxx
            y = random.randint(0, self.maxy)
        else:
            x = random.randint(0, self.maxx)
            y = self.maxy    
        if self.withImmute: 
            if random.random() < 0.1:
                a = random.random()
                if a < 0.3:
                    p = Person(NoSymptomsState(), x, y, self.maxx, self.maxy)
                elif a < 0.6:
                    p = Person(ImmunteState(), x, y, self.maxx, self.maxy)
                else:
                    p = Person(SymptomsState(), x, y, self.maxx, self.maxy)
            else:
                p = Person(HealtyState(), x, y, self.maxx, self.maxy)
        else:
            if random.random() < 0.1:
                a = random.random()
                if a < 0.5:
                    p = Person(NoSymptomsState(), x, y, self.maxx, self.maxy)
                else:
                    p = Person(SymptomsState(), x, y, self.maxx, self.maxy)
            else:
                p = Person(HealtyState(), x, y, self.maxx, self.maxy)

        self.persons.append(p)
        
          
    
if __name__ == "__main__":
    sim = Simulation(10, 10, 40, True)
    sim.generatePopulation(10)
    sim.show_animation()


    