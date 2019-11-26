from watchFaceParser.models.elements.common.numberElement import NumberElement
from watchFaceParser.utils.parametersConverter import uint2int


class TemperatureElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        self._temperature = None
        super(TemperatureElement, self).__init__(parameter, parent, name)

    def getTemperature(self):
        return self._temperature

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        temperature = self._parent
		
        images = self.getTemperature().getImagesForNumber(resources, 27, 2) #fixed temperature for now....

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self.getTemperature().getSpacing()), self.getTemperature().getAlignment(), self.getTemperature().getBox())

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            print ("TemperatureElement: (CURRENT_TEMPERATURE) supported", parameterId)
            #from watchFaceParser.models.elements.weather.temperature.oneLineTemperatureElement import OneLineTemperatureElement
            #self._oneLine = OneLineTemperatureElement(parameter = parameter, parent = self, name = 'OneLineTemperatureElement')
            #return self._oneLine
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._temperature = NumberElement(parameter = parameter, parent = self, name = 'Temperature')
            print ("DEBUG",self._temperature)
            return self._temperature
        elif parameterId == 3:
            print ("TemperatureElement: unsupported", parameterId)
            pass
        else:
            return super(TemperatureElement, self).createChildForParameter(parameter)
