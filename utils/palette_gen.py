#!/usr/bin/python

# usage: turpentine <path/to/image> <paletteName>

import sys
import argparse
from colorthief import ColorThief

parser = argparse.ArgumentParser(description='Create a palette from an image')
parser.add_argument('--image', dest='image', help='Set the image to turpentine', type=argparse.FileType('r'))
parser.add_argument('--palette', dest='palette_file', help='Set the palette name')
args = parser.parse_args()


def generate_palette(Image):
    color_thief = ColorThief(Image)
    palette = color_thief.get_palette()
    return palette

def write_palette(palette):

    if args.palette_file:
        file = open( args.palette_file + ".gpl", "w")
        file.write("GIMP Palette\n")
        file.write("Name: %s palette\n" % (args.palette_file))
    else:
        file = open( "palette.gpl", "w")
        file.write("GIMP Palette\n")
        file.write("Name: %s palette\n" % (args.palette_file))

    file.write("#\n")
    file.write("\n")

    for color in palette:

        hex = '#%02x%02x%02x' % color
        file.write("%s %s %s %s\n" % (color[0], color[1], color[2], hex))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    gen_palette = generate_palette(args.image)
    write_palette(gen_palette)
