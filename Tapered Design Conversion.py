from PIL import Image, ImageDraw

def convert_to_tapered(original_path, output_path, taper_factor=1.5):
    # Open the original image
    original_image = Image.open(original_path)

    # Get image dimensions
    width, height = original_image.size

    # Create a new image for the tapered design
    tapered_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    # Create a drawing object
    draw = ImageDraw.Draw(tapered_image)

    # Calculate the tapering effect based on the specified factor
    tapering_width = int((taper_factor - 1) * width / 2)

    # Iterate through each row of pixels
    for y in range(height):
        # Calculate the tapering effect for the current row
        tapering_offset = int((y / height) * tapering_width)

        # Copy pixels from the original image to the tapered image
        pixels = original_image.crop((tapering_offset, y, width - tapering_offset, y + 1))
        tapered_image.paste(pixels, (tapering_offset, y))

    # Save the tapered design
    tapered_image.save(output_path)

if __name__ == "__main__":
    # Specify the path to the original image
    original_image_path = "pirate_straight_1.png"

    # Specify the output path for the tapered design
    output_image_path = "tapered_design.png"

    # Set the taper factor (adjust as needed)
    taper_factor = 1.5

    # Convert the straight design to a tapered design
    convert_to_tapered(original_image_path, output_image_path, taper_factor)

    print("Tapered design created successfully.")
