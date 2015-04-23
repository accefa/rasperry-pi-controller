import io
from picamera import PiCamera
from PIL import Image

def shoot(detectConfig):
        stream = io.BytesIO()
        try:
            picamera = PiCamera()
            picamera.contrast = detectConfig.contrast
            picamera.resolution = (1280, 720) # Come on we define a fixed size
            if detectConfig.greyscale:
                picamera.color_effects = (128, 128) # grayscale
            picamera.capture(stream, "jpeg", False, False, 0, quality=detectConfig.quality)
            stream.seek(0) # "Rewind" the stream to the beginning so we can read its content
            image = Image.open(stream)
            return image
        finally:
            picamera.close()