import io
from picamera import PiCamera
from PIL import Image

# dynamic load this classes
# https://lextoumbourou.com/blog/posts/dynamically-loading-modules-and-classes-in-python/

class CameraController(object):
    def shoot(self, detectConfig):
        stream = io.BytesIO()
        
        self.picamera = PiCamera();
        self.picamera.contrast = detectConfig.contrast
        self.picamera.resolution = (1280, 720) # Come on we define a fixed size
        if detectConfig.greyscale:
            self.picamera.color_effects = (128, 128) # grayscale
        self.picamera.capture(stream, "jpeg", False, False, 0, quality=detectConfig.quality)
        stream.seek(0) # "Rewind" the stream to the beginning so we can read its content
        image = Image.open(stream)
        return image
