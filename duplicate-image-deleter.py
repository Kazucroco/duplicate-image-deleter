import os
from PIL import Image

# Directory containing all images.
directory = "images/"

# Stores all images recognized, and checked against for duplicates.
image_bank = []

# Loops over every image in the directory.
for file in os.listdir(directory):

    # Skips the instruction file.
    if(file == "place_image_files_here.txt"):
        continue
    
    # Ensures the program doesn't crash when trying to open an invalid file.
    try:
        # Opens an image and stores the bytes in current_image
        current_image = Image.open(f"./{directory}{file}").tobytes()

    except:
        print(f"Failed to open file: {directory}{file}")

    # Checks current image data against ALL previous images.
    for stored_image in image_bank:

        # Delete the image if it has already been added to the image bank.
        if(current_image == stored_image):
            os.remove(f"./{directory}{file}")
            break

    # Adds the current image to the bank if no identical images were found.
    image_bank.append(current_image)


