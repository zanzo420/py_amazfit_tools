import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class Unknown18Element(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        self._unknown4 = None
        super(Unknown18Element, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def getPulseClockHand(self):
        return self._unknown4

    def draw3(self, drawer, resources, state):

        if self.getPulseClockHand():
            self.getPulseClockHand().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 2:
            from watchFaceParser.models.elements.activity.pulseClockHandElement import PulseClockHandElement # must must be own. fix it!!
            self._unknown4 = PulseClockHandElement(parameter = parameter, parent = self, name = 'Unknown2')
            return self._unknown4
        else:
            super(Unknown18Element, self).createChildForParameter(parameter)
