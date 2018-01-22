from PIL import Image
import io
def convert_image(imageBytes, to_width, to_height):
    #Read image from bytes
    image = Image.open(io.BytesIO(imageBytes.read()))
    
    #Current width
    height, width = image.size

    #Resize image
    if height != to_height or width != to_width:
        image = image.resize((to_width, to_height))
    
    return image
