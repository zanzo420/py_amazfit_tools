from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.batteryElements.unknownType4 import UnknownType4

class DaysProgress:
    definitions = {
		1: { 'Name': 'AnalogMonth', 'Type': ClockHand},
		2: { 'Name': 'UnknownField2', 'Type': UnknownType4},
		3: { 'Name': 'AnalogDOW', 'Type': ClockHand},
    }

