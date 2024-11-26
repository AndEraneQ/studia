import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from State import IState
from Vector import Vector2D

class MementoPerson:
    _IState : IState
    _position : Vector2D
    _velocity : Vector2D
    _onPlane : bool
    _timeNearUnhealthy : int
    _timeNearNoSymptoms : int
    _timeToRecover : int
    _timeSick : int
    _maxwidth = float
    _maxheight = float

    def __init__(self, IState, position, velocity, onPlane, timeNearUnhealthy, timeNearNoSymptoms, timeToRecover, maxwidth, maxheight) -> None:
        self._IState = IState
        self._position = position
        self._velocity = velocity
        self._onPlane = onPlane
        self._timeNearUnhealthy = timeNearUnhealthy
        self._timeNearNoSymptoms = timeNearNoSymptoms
        self._timeToRecover = timeToRecover
        self._maxwidth = maxwidth
        self._maxheight = maxheight

    def getState(self):
        return self._IState.getColor()
    
    def getPosition(self):
        return self._position
    
    def getVelocity(self):
        return self._velocity
    
    def getOnPlane(self):
        return self._onPlane
    
    def getTimeNearUnhealthy(self):
        return self._timeNearUnhealthy
    
    def getTimeNearNoSymptoms(self):
        return self._timeNearNoSymptoms
    
    def getTimeToRecover(self):
        return self._timeToRecover
    
    def getMaxWidth(self):
        return self._maxwidth
    
    def getMaxHeight(self):
        return self._maxheight
    
    