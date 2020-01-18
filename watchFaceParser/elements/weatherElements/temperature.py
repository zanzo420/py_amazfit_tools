from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.weatherElements.today import Today
from watchFaceParser.elements.weatherElements.symbols import Symbols
from watchFaceParser.elements.basicElements.circleScale import CircleScale

class Temperature:
    definitions = {
        1: { 'Name': 'Current', 'Type': Number},
        2: { 'Name': 'Today', 'Type': Today},
        3: { 'Name': 'Symbols', 'Type': Symbols},
        4: { 'Name': 'TemperatureMeter', 'Type': CircleScale}, #gts- Fluorescence
    }

