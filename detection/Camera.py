from picamera import PiCamera

# dynamic load this classes
# https://lextoumbourou.com/blog/posts/dynamically-loading-modules-and-classes-in-python/

class CameraController(object):
    def detect(self, detectConfig):
        self.picamera = PiCamera();
        self.picamera.contrast = 100
        return False
