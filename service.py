import base64
import io
from PIL import Image
from pyzbar.pyzbar import decode
def decode_image_data(image_data):
    # Split the base64 string on the comma
    header, base64_str = image_data.split(',')

    # Decode the base64 string
    image_bytes = base64.b64decode(base64_str)

    # Create a byte stream from the image bytes
    byte_stream = io.BytesIO(image_bytes)

    # Create an image from the byte stream
    image = Image.open(byte_stream)

    return image

def decode_barcode(image_data):
    # image is  data:image/jpeg;base64,/9j/4VQpRXhpZgAATU0AKg
    # Decode the barcode from the image
    image = decode_image_data(image_data)
    decoded_objects = decode(image)
    # Print the results
    return [obj.data for obj in decoded_objects]
