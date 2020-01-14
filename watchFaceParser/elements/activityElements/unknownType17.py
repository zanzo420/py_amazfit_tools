from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand 

class UnknownType17:
    definitions = {
        1: { 'Name': 'KcalProgress', 'Type': CircleScale}, # should be kcal on gts
        3: { 'Name': 'StepsProgress', 'Type': ClockHand}, # gtr - Red flywheel
    }
