import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    check_file_extension(input_name)
    check_file_extension(output_name)

    if get_file_extension(input_name) != get_file_extension(output_name):
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_name) as input_img, Image.open("shirt.png") as shirt_img:
            # Rize and crop to match shirt
            size = shirt_img.size
            input_img = ImageOps.fit(input_img, size)
            # overlay the shirt with Image.paste
            input_img.paste(shirt_img, shirt_img)
            input_img.save(output_name)

    except FileNotFoundError:
        sys.exit("File not found")

def get_file_extension(file_name):
    return file_name.split(".")[-1].lower()

def check_file_extension(file_name):
    file_extension = get_file_extension(file_name)
    if file_extension != "png" and file_extension != "jpeg" and file_extension != "jpg":
        sys.exit(file_name + " is not a valid image file (PNG or JPEG)")

main()
