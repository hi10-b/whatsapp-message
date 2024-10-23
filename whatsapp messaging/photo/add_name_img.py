from PIL import Image, ImageDraw, ImageFont
import os

# Function to add text to image
def add_text_to_image(image_path, text, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Load a font (you can specify a path to a TTF file, like Arial)
    font = ImageFont.truetype("arial.ttf", 40)  # Change path if necessary
    
    # Define text position and color
    text_position = (50, 50)  # Adjust as needed
    text_color = (0, 0, 0)  # Update text colour as required

    # Add text to the image
    draw.text(text_position, text, fill=text_color, font=font)
    
    # Save the image with the text added
    image.save(output_path)
    print(f"Image saved to {output_path}")

# List of custom texts to add
texts = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Define the input image path and output folder
input_image_path = './sample.png'  # Path to the original image
output_folder = './updated/'  # Folder to save output images

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through the list of texts and add them to the image
for text in texts:
    # Create the output file path with the text as the filename
    output_path = os.path.join(output_folder, f"{text}.png")
    add_text_to_image(input_image_path, text, output_path)
