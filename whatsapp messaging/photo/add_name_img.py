import os
import csv
from PIL import Image, ImageDraw, ImageFont
import pandas as pd



def get_names_from_excel(contacts_file):
    with open(contacts_file, newline='') as csvfile:
        contacts_reader = csv.DictReader(csvfile)
        for row in contacts_reader:
            # print(row['First Name'])
            # print(row['Last Name'])
            name = row['First Name'] + ' ' + row['Last Name']
            output_path = './updated/' + row['Phone 1 - Value'] + '.jpeg'
            add_text_to_image('./template.jpeg', name , output_path )

# Function to add text to image
def add_text_to_image(image_path, name, output_path):

    # Open the image
    image = Image.open(image_path)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Load a font (you can specify a path to a TTF file, like Arial)
    font = ImageFont.truetype("./GlacialIndifference-Bold.otf", 82)  # Cha3nge path if necessary
    
    _, _, w, h = draw.textbbox((0, 0), name, font=font)

    width = 2047
    height = 2560

    # Define text position and color
    text_position = ((width-w)/2, (height-h)/4)  # Adjust as needed
    text_color = (255, 255, 255)  # Update text colour as required


    # Add text to the image
    draw.text(text_position, name, fill=text_color, font=font)
    
    # Save the image with the text added
    image.save(output_path)
    print(f"Image saved to {output_path}")

# Define the input image path and output folder
input_image_path = './template.jpeg'  # Path to the original image
output_folder = './updated/'  # Folder to save output images

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


if __name__ == "__main__":

    contacts_file = 'contacts.csv'
    # contacts_file = 'test.csv'
    get_names_from_excel(contacts_file)
