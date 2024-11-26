from .IState import IState

class NoSymptomsState(IState):
    def getColor(self):
        return "yellow"
    
class SymptomsState(IState):
    def getColor(self):
        return "red"
    
class ImmunteState(IState):
    def getColor(self):
        return "blue"
    
class HealtyState(IState):
    def getColor(self):
        return "green"