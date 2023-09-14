from PIL import Image
import math

# Load the PNG image
image = Image.open('Blue.png')

# Get the dimensions of the image
width, height = image.size

# Calculate the coordinates of the center pixel
center_x = width // 2
center_y = height // 2

# Get the RGB color of the center pixel
center_pixel_color = image.getpixel((center_x, center_y))

# Define the RGB values for blue and red
blue_color = (0, 0, 255)
red_color = (255, 0, 0)

# Calculate the Euclidean distance between the center pixel color and blue/red
def euclidean_distance(color1, color2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(color1, color2)))

distance_to_blue = euclidean_distance(center_pixel_color, blue_color)
distance_to_red = euclidean_distance(center_pixel_color, red_color)

# Determine which color is closer
if distance_to_blue < distance_to_red:
    print("The centermost pixel is closer to blue (0, 0, 255)")
elif distance_to_red < distance_to_blue:
    print("The centermost pixel is closer to red (255, 0, 0)")
else:
    print("The centermost pixel is equidistant from blue and red.")
