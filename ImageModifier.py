from PIL import Image, ImageChops, ImageOps, ImageDraw, ImageEnhance

if(False):
    # Load image
    image = Image.open('Cephalon Cy.png')

    # Convert image to grayscale
    image = image.convert('L')

    # Get image size
    width, height = image.size

    # Create a new image for the negative version
    negative = Image.new('RGB', (width, height), color=(255, 255, 255))

    # Iterate over each pixel and modify its brightness
    for x in range(width):
        for y in range(height):
            # Get the brightness of the pixel
            brightness = image.getpixel((x, y))

            # Calculate the new brightness for the negative image
            negative_brightness = 255 - brightness

            # Blend the original and negative images by 50%
            blended_brightness = (brightness + negative_brightness) // 2

            # Set the new brightness of the pixel
            negative.putpixel((x, y), (blended_brightness, blended_brightness, blended_brightness))

    # Convert the negative image to grayscale
    negative = negative.convert('L')

    # Blend the original and negative images by 50%
    blended = Image.blend(image, negative, 0.5)

    # Save the modified image
    blended.save('output_image.png')
    
# Load images
positive = Image.open('Cephalon Cy.png').convert("RGBA")
negative = Image.open('Reverse Cephalon Cy.png').convert("RGBA")
#final = Image.open('inverted.png').convert("RGB")

img = Image.open('blended.png')
threshold_rgb = (235, 235, 235)

def apply_threshold(pixel, threshold_rgb):
    if sum(pixel[:3]) // 3 >= sum(threshold_rgb) // 3:
        return (0, 0, 0, 255)
    else:
        return pixel

final = Image.new('RGBA', img.size)
for x in range(img.width):
    for y in range(img.height):
        pixel = img.getpixel((x, y))
        final.putpixel((x, y), apply_threshold(pixel, threshold_rgb))

final.save("final1.png")
