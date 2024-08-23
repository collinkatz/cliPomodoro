import argparse
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input HEIC file", required=True)
parser.add_argument("-o", "--output", help="Output JPEG file", required=True)
args = parser.parse_args()

image = Image.open(args.input)
image.save(args.output, format='jpeg')