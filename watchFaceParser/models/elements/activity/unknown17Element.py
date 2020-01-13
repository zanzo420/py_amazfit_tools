import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class Unknown17Element(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._step = None
        self._circularCalories = None
        super(Unknown17Element, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStep(self):
        return self._step

    def getCircularCalories(self):
        return self._circularCalories

    def draw3(self, drawer, resources, state):

        if self.getCircularCalories():
            self.getCircularCalories().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.activity.circularCaloriesElement import CircularCaloriesElement
            self._circularCalories = CircularCaloriesElement(parameter = parameter, parent = self, name = '_circularCalories')
        else:
            super(Unknown17Element, self).createChildForParameter(parameter)
