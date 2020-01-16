class Config:
    _is_gtr = False
    _is_gts = False
    _image_size = (360, 360)
    _preview_size = (210, 210)
    _autodetect = True

    _size_gtr_47 = (454, 454)
    _size_gtr_42 = (390, 390)
    _size_gts = (348,442)

    @staticmethod
    def getAutodetect():
	    return Config._autodetect
	
    @staticmethod
    def autodetect(size):
        print ("Autodetect device")
        if size == Config._size_gtr_47:
            print("Detected GTR (47mm)")
            Config.setGtrMode(47)
        elif size == Config._size_gtr_42:
            print("Detected GTR (42mm)")
            Config.setGtrMode(42)
        elif size == Config._size_gts:
            print("Detected GTS")
            Config.setGtsMode(True)
        else:
            Config._autodetect = False
            print("default_verge")

    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr == 47:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_47
            Config._preview_size = (266, 266)
        if Config._is_gtr == 42:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_42
            Config._preview_size = (266, 266)

    @staticmethod
    def isGtrMode():
        return Config._is_gtr

    @staticmethod
    def setGtsMode(gts):
        if gts:
            Config._autodetect = False
            Config._is_gts = 40
            Config._image_size = Config._size_gts
            Config._preview_size = (242,304)

    @staticmethod
    def isGtsMode():
        return Config._is_gts

    @staticmethod
    def getImageSize():
        return Config._image_size


    @staticmethod
    def getImageSizeHalf():
        return (int(Config._image_size[0] / 2),int(Config._image_size[1] / 2))


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

