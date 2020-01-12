from watchFaceParser.elements.activityElements.formattedNumber import FormattedNumber
from watchFaceParser.elements.activityElements.distance import Distance
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.activityElements.unknownType import UnknownType
from watchFaceParser.elements.activityElements.unknownType18 import UnknownType18
from watchFaceParser.elements.basicElements.iconSet import IconSet

class Activity:
    definitions = {
        2: { 'Name': 'Calories', 'Type': Number},
        3: { 'Name': 'Pulse', 'Type': Number},
        4: { 'Name': 'Distance', 'Type': Distance},
        5: { 'Name': 'Steps', 'Type': FormattedNumber},
        7: { 'Name': 'StarImage', 'Type': Image}, #gtr
        8: { 'Name': 'CaloriesIcon', 'Type': Image}, #gts - Chiba petals_60247
        9: { 'Name': 'CircleRange', 'Type': Image}, # verge
        11: { 'Name': 'PulseMeter', 'Type': CircleScale}, # gts circle.bin
        12: { 'Name': 'ColouredSquares', 'Type': IconSet}, # gts - Classic number_101759
        13: { 'Name': 'NoDataImageIndex', 'Type': 'long'}, # verge
        14: { 'Name': 'Unknown14', 'Type': 'long'}, # gts - Digital watch
        15: { 'Name': 'CaloriesTextualIcon', 'Type': 'long'}, # gts - Classic number_101759
        17: { 'Name': 'Unknown17', 'Type': UnknownType}, # gts circle.bin
        1: { 'Name': 'KcalProgress', 'Type': CircleScale}, # should be kcal on gts
		18: { 'Name': 'Unknown18', 'Type': UnknownType18}, # gts fluorescence
    }

