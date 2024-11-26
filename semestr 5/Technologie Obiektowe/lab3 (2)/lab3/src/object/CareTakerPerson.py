from .Person import Person
import xml.etree.ElementTree as ET
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from State import IState, SymptomsState, HealtyState, ImmunteState, NoSymptomsState
from Vector import Vector2D
from .MementoPerson import MementoPerson

class CareTakerPerson:
    def __init__(self) -> None:
        self.mementos = []
    
    def backup(self, listPerson: list[Person]):
        self.mementos = []
        for person in listPerson:
            self.mementos.append(person.saveToMemento())

    def save(self):
        root = ET.Element('root')
        root.tail = '\n'
        for memento in self.mementos:
            person = ET.SubElement(root, 'person')
            state_element = ET.SubElement(person, 'state')
            state_element.text = str(memento.getState())
            position_element = ET.SubElement(person, 'position_x')
            position_element.text = str(memento.getPosition().getX())
            position_element = ET.SubElement(person, 'position_y')
            position_element.text = str(memento.getPosition().getY())
            velocity_element = ET.SubElement(person, 'velocity_x')
            velocity_element.text = str(memento.getVelocity().getX())
            velocity_element = ET.SubElement(person, 'velocity_y')
            velocity_element.text = str(memento.getVelocity().getY())
            onPlane_element = ET.SubElement(person, 'onPlane')
            onPlane_element.text = str(memento.getOnPlane())
            timeNearUnhealthy_element = ET.SubElement(person, 'timeNearUnhealthy')
            timeNearUnhealthy_element.text = str(memento.getTimeNearUnhealthy())
            timeNearNoSymptoms_element = ET.SubElement(person, 'timeNearNoSymptoms')
            timeNearNoSymptoms_element.text = str(memento.getTimeNearNoSymptoms())
            timeToRecover_element = ET.SubElement(person, 'timeToRecover')
            timeToRecover_element.text = str(memento.getTimeToRecover())
            maxwidth_element = ET.SubElement(person, 'maxwidth')
            maxwidth_element.text = str(memento.getMaxWidth())
            maxheight_element = ET.SubElement(person, 'maxheight')
            maxheight_element.text = str(memento.getMaxHeight())
            person.tail = '\n'
        tree = ET.ElementTree(root)
        tree.write('backup_population.xml', encoding='utf-8', xml_declaration=True)

    def restore(self):
        tree = ET.parse('backup_population.xml')
        root = tree.getroot()
        self.mementos = []
        for person in root.findall('person'):
            state = person.find('state').text
            position_x = float(person.find('position_x').text)
            position_y = float(person.find('position_y').text)
            velocity_x = float(person.find('velocity_x').text)
            velocity_y = float(person.find('velocity_y').text)
            onPlane = bool(person.find('onPlane').text)
            timeNearUnhealthy = int(person.find('timeNearUnhealthy').text)
            timeNearNoSymptoms = int(person.find('timeNearNoSymptoms').text)
            timeToRecover = int(person.find('timeToRecover').text)
            maxwidth = float(person.find('maxwidth').text)
            maxheight = float(person.find('maxheight').text)

            state_instance: IState
            if state == "green":
                state_instance = HealtyState()
            elif state == "blue":
                state_instance = ImmunteState()
            elif state == "red":
                state_instance = SymptomsState()
            elif state == "yellow":
                state_instance = NoSymptomsState()

            position = Vector2D(position_x, position_y)
            velocity = Vector2D(velocity_x, velocity_y)
            
            memento = MementoPerson(state_instance, position, velocity, onPlane, timeNearUnhealthy, timeNearNoSymptoms, timeToRecover, maxwidth, maxheight)

            self.mementos.append(memento)

    def getMementos(self):
        return self.mementos

        



    