from PIL import Image

# Load the original image
image_path = "ascii-pineapple.jpg"
original_image = Image.open(image_path) # Replace with your image file path
img = original_image

# Get image dimensions
image_width, image_height = img.size

# Print the output
print("Image successfully loaded!")
print(f"Image size: {image_width} x {image_height}")

# Define the desired dimensions for the resized image
desired_width = 60 # Adjust this value based on your terminal
aspect_ratio = original_image.width / original_image.height
desired_height = int(desired_width / aspect_ratio)

# Resize the image
resized_image = original_image.resize((desired_width, desired_height))

# Get the pixel data from the resized image
pixel_matrix = list(resized_image.getdata())

# Convert the pixel data from the resiezed image
width, height = resized_image.size
pixel_matrix = [pixel_matrix[i:i+width] for i in range(0, len(pixel_matrix), width)]

for x in range(len(pixel_matrix)):
    for y in range(len(pixel_matrix[x])):
        pixel = pixel_matrix[x][y]
   
# Transform pixel matrix into brightness matrix using the Average method
brightness_matrix = []
for row in pixel_matrix:
    brightness_row = []
    for pixel in row:
        avg_brightness = sum(pixel) // 3 # Using integer division to get a single value
        brightness_row.append(avg_brightness)
    brightness_matrix.append(brightness_row)

# Create ASCII Character set
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Transform brightness matrix into ASCII matrix using character mapping
ascii_matrix =[]
for row in brightness_matrix:
    ascii_row = [ascii_chars[brightness // 4] for brightness in row]
    ascii_matrix.append(ascii_row)


# Print the stretched ASCII art
stretch_factor = 3
for row in ascii_matrix:
    for char in row:
        print (char * stretch_factor, end='') # Repeat the character multiple times
    print() # Move to the next line after each row