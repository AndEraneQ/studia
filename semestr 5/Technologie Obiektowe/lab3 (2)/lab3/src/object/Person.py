import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from State import IState, SymptomsState, HealtyState, ImmunteState, NoSymptomsState
from Vector import Vector2D
from .MementoPerson import MementoPerson
import random

class Person:
    _IState : IState
    _position : Vector2D
    _velocity : Vector2D
    _onPlane : bool
    _timeNearUnhealthy : int
    _timeNearNoSymptoms : int
    _timeToRecover : int
    _timeSick : int
    _maxwidth : int
    _maxheight : int 
    
    def __init__(self, state : IState, x = 0, y = 0, width = 100, height = 100, velocity = 0, onPlane = True, timeNearUnhealthy = 0, timeNearNoSymptoms = 0, timeToRecover = 0, timeSick = 0 ) -> None:
        self._IState = state
        self._position = Vector2D(x, y)
        if velocity == 0:
            x = (random.uniform(-1, 1)*2.5)/25
            y = (random.uniform(-1, 1)*2.5)/25
            self._velocity = Vector2D(x, y)
        if isinstance(velocity, Vector2D):
            self._velocity = velocity
        self._onPlane = onPlane
        self._timeNearUnhealthy = timeNearUnhealthy
        self._timeNearNoSymptoms = timeNearNoSymptoms
        self._timeSick = timeSick
        if timeToRecover == 0:
            self._timeToRecover = (20 + random.randint(0, 10)) *25
        else:
            self._timeToRecover = timeToRecover
        self._maxwidth = width
        self._maxheight = height
    
        
    
    def setState(self, state: IState):
        self._IState = state
    
    def getColor(self):
        return self._IState.getColor()
    
    def setPosition(self, x, y):
        self._position = Vector2D(x, y)
    
    def getPosition(self):
        return self._position
    
    def getX(self):
        return self._position.getX()
    
    def getY(self):
        return self._position.getY()
    
    def getVelocity(self):
        return self._velocity
    
    def setVelocity(self, x, y):
        self._velocity = Vector2D(x, y)
        
    def getState(self):
        return self._IState

    def setOnPlane(self, onPlane):
        self._onPlane = onPlane

    def setTimeNearUnhealthy(self, timeNearUnhealthy):
        self._timeNearUnhealthy = timeNearUnhealthy

    def setTimeNearNoSymptoms(self, timeNearNoSymptoms):
        self._timeNearNoSymptoms = timeNearNoSymptoms

    def setTimeToRecover(self, timeToRecover):
        self._timeToRecover = timeToRecover

    def setTimeSick(self, timeSick):
        self._timeSick = timeSick

    def setMaxwidth(self, maxwidth):
        self._maxwidth = maxwidth

    def setMaxheight(self, maxheight):
        self._maxheight = maxheight
    
    def move(self):
        if random.random() < 0.01:
            x = (random.uniform(-1, 1)*2.5)/25
            y = (random.uniform(-1, 1)*2.5)/25
            self._velocity = Vector2D(x, y)
        self._position = self._position + self._velocity
    
    def getOnPlane(self):
        if self._position.getX() < 0 or self.getX() > self._maxwidth or self.getY() < 0 or self.getY() > self._maxheight:
            if random.random() < 0.5:
                self._velocity.setX(-self._velocity.getX())
                self._velocity.setY(-self._velocity.getY())            
            else:
                self._onPlane = False
        return self._onPlane
    
    def getTimeNearUnhealthy(self):
        return self._timeNearUnhealthy
    
    def whenNearUnhealthy(self, other: 'Person'):
        if isinstance(self._IState, HealtyState) and (isinstance(other._IState, SymptomsState) or isinstance(other._IState, NoSymptomsState)):
            if isinstance(other._IState, SymptomsState):
                self._timeNearUnhealthy += 1
            if isinstance(other._IState, NoSymptomsState):
                self._timeNearNoSymptoms += 1
            return True
        
    def distance(self, other: 'Person'):
        return self._position.distance(other._position)
    
    def isNear(self, other: 'Person'):
        return self.distance(other) < 3.0
    
    def checkState(self):
        if isinstance(self._IState, HealtyState):
            if self._timeNearUnhealthy > 50:
                if random.random() < 0.5:
                    self._IState = NoSymptomsState()
                    return
                else:
                    self._IState = SymptomsState()
                    return
            elif self._timeNearNoSymptoms > 50:
                if random.random() <= 0.5:
                    if random.random() <= 0.5:
                        self._IState = NoSymptomsState()
                        return
                    else:
                        self._IState = SymptomsState() 
                        return
                else:
                    self._IState = HealtyState()
                    self._timeNearNoSymptoms = 0
    
    def checkRecover(self):
        if isinstance(self._IState, SymptomsState) or isinstance(self._IState, NoSymptomsState):
            self._timeSick += 1
            if self._timeSick > self._timeToRecover:
                self._IState = ImmunteState()
 
    def saveToMemento(self):
        return MementoPerson(self._IState, self._position, self._velocity, self._onPlane, self._timeNearUnhealthy, self._timeNearNoSymptoms, self._timeToRecover, self._maxwidth, self._maxheight)
    
    def restoreFromMemento(self, memento: MementoPerson):
        state_instance = HealtyState()
        if memento.getState() == ImmunteState().getColor():
            state_instance = ImmunteState()
        elif memento.getState() == SymptomsState().getColor():
            state_instance = SymptomsState()
        elif memento.getState() == NoSymptomsState().getColor():
            state_instance = NoSymptomsState()
        self._IState = state_instance
        self._position = memento.getPosition()
        self._velocity = memento.getVelocity()
        self._onPlane = memento.getOnPlane()
        self._timeNearUnhealthy = memento.getTimeNearUnhealthy()
        self._timeNearNoSymptoms = memento.getTimeNearNoSymptoms()
        self._timeToRecover = memento.getTimeToRecover()
        self._maxwidth = memento.getMaxWidth()
        self._maxheight = memento.getMaxHeight()

    