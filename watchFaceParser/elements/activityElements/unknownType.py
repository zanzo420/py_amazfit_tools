from watchFaceParser.models.parameterFlags import ParameterFlags

class UnknownType:
    definitions = {
        3: { 'Name': 'EnableThirdGoal', 'Type': ParameterFlags},
        4: { 'Name': 'EnableEnhanchedGoal', 'Type': ParameterFlags},
        7: { 'Name': 'EnableUnknown', 'Type': ParameterFlags}, #gts - Fluorescence
    }
