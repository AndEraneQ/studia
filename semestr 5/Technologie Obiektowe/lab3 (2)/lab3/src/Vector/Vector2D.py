from .IVector import IVector


class Vector2D(IVector):
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y
        
    def getComponents(self) -> list[float]:
        return [self.getX(), self.getY()]
    
    def abs(self) -> float:
        return (self.getX()**2 + self.getY()**2)**0.5
    
    def cdot(self, other: 'Vector2D') -> float:
        return self.getX()*other.getX() + self.getY()*other.getY()
    
    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
    def setX(self, x: float):
        self.x = x
        
    def setY(self, y: float):
        self.y = y
    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.getX() + other.getX(), self.getY() + other.getY())
    
    def distance(self, other: 'Vector2D') -> float:
        return ((self.getX() - other.getX())**2 + (self.getY() - other.getY())**2)**0.5

