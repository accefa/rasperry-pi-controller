from picamera import PiCamera

# dynamic load this classes
# https://lextoumbourou.com/blog/posts/dynamically-loading-modules-and-classes-in-python/

class CameraController(object):
    def shoot(self, detectConfig):
        self.picamera = PiCamera();
        self.picamera.contrast = detectConfig.contrast
        # self.picamera.zoom = (0.0, 0.0, 1.0, 1.0) # x y w h
        if detectConfig.greyscale:
            self.picamera.color_effects = (256)
        self.picamera.capture("filename.jpeg", "jpeg", False, False, 0, quality=detectConfig.quality)
        return False
