from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.weatherElements.temperatureImages import TemperatureImages

class Temperature:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        3: { 'Name': 'TemperatureImages', 'Type': TemperatureImages},
    }

