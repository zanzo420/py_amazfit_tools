from watchFaceParser.models.elements.watchFace import WatchFace
from watchFaceParser.config import Config

class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image, ImageDraw

        if Config.getAutodetect():
            Config.autodetect(resources[0].getBitmap().size)
        elif resources[0].getBitmap().size != Config.getImageSize():
            print ("WARNING - Configured watch display size is different from extracted image1 size")

        # graphics = Image.new('RGBA', (360, 360))
        graphics = Image.new('RGBA', Config.getImageSize())
        watchFace.draw3(graphics, resources, state)
        return graphics
