# Copyright (C) 2022 Eli Heuer
# License: GPL version 3
# License URL: https://www.gnu.org/licenses/gpl-3.0.html

# To render this image, install drawbot-skia: https://github.com/justvanrossum/drawbot-skia

# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:

# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image1.py --output documentation/image1.png


# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 2048, 256, 1
UNIT = MARGIN/4
FONT_PATH = "documentation/specimen_fonts/GTL002-Regular.ttf"
FONT_LICENSE = "OFLv1.1"
AUXILIARY_FONT = "documentation/specimen_fonts/Hasubi-Mono[wght].ttf"
AUXILIARY_FONT_SIZE = 48
BIG_TEXT_A = "YOUR DESIRE TO RECEIVE"
BIG_TEXT_B = "“CREDIT” FOR YOUR"
BIG_TEXT_C = "ARTISTIC OUTPUT IS"
BIG_TEXT_D = "DUE TO THE FAULTY"
BIG_TEXT_E = "ASSUMPTIONS THAT "
BIG_TEXT_F = "A."
BIG_TEXT_F2 = "“YOU” “CREATED”"
BIG_TEXT_G = "“SOMETHING” "
BIG_TEXT_H = "B."
BIG_TEXT_H2 = "THAT THE SO-CALLED"
BIG_TEXT_I = "CREDIT IS REDEEMABLE "
BIG_TEXT_J = "FOR ANYTHING THAT "
BIG_TEXT_K = "WILL ACTUALLY "
BIG_TEXT_L = "MAKE YOU HAPPY."
BIG_TEXT_M = ""
BIG_TEXT_N = ""
BIG_TEXT_O = ""
BIG_TEXT_P = ""
BIG_TEXT_FONT_SIZE = 128+32
BIG_TEXT_SIDE_MARGIN = MARGIN * 1
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 5.9
GRID_VIEW = False # Change this to "True" for a grid overlay

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_URL = "https://github.com/eliheuer/GTL002 "
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)
FONT_NAME = FONT_NAME+FONT_VERSION
FONT_NAME = "GTL002 Alpha NFT"
ENS_NAME = "elih.eth"

# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 4, MARGIN / 4
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(25):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(25):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass


# Draw main text
def draw_main_text():
    fill(1)
    stroke(None)
    font(FONT_PATH)
    fontSize(BIG_TEXT_FONT_SIZE)
    fontVariations(wght = 400)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString
    #text(BIG_TEXT, ((WIDTH / 2) - MARGIN * 4.75, (HEIGHT / 2) - MARGIN * 2.5))
    text(BIG_TEXT_A, (BIG_TEXT_SIDE_MARGIN-9, UNIT*26))
    text(BIG_TEXT_B, (BIG_TEXT_SIDE_MARGIN-9, UNIT*24))
    text(BIG_TEXT_C, (BIG_TEXT_SIDE_MARGIN-9, UNIT*22))
    text(BIG_TEXT_D, (BIG_TEXT_SIDE_MARGIN-9, UNIT*20))
    text(BIG_TEXT_E, (BIG_TEXT_SIDE_MARGIN-9, UNIT*18))
    text(BIG_TEXT_F, (BIG_TEXT_SIDE_MARGIN-9, UNIT*16))
    text(BIG_TEXT_F2, (BIG_TEXT_SIDE_MARGIN+130, UNIT*16))
    text(BIG_TEXT_G, (BIG_TEXT_SIDE_MARGIN-9, UNIT*14))
    text(BIG_TEXT_H, (BIG_TEXT_SIDE_MARGIN-9, UNIT*12))
    text(BIG_TEXT_H2, (BIG_TEXT_SIDE_MARGIN+130, UNIT*12))
    text(BIG_TEXT_I, (BIG_TEXT_SIDE_MARGIN-9, UNIT*10))
    text(BIG_TEXT_J, (BIG_TEXT_SIDE_MARGIN-9, UNIT*8))
    text(BIG_TEXT_K, (BIG_TEXT_SIDE_MARGIN-9, UNIT*6))
    text(BIG_TEXT_L, (BIG_TEXT_SIDE_MARGIN-9, UNIT*4))
    text(BIG_TEXT_M, (BIG_TEXT_SIDE_MARGIN-9, UNIT*2))
    #text(BIG_TEXT_D, (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN - MARGIN*2.25))
    #text(BIG_TEXT_E, (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN - MARGIN*3.00))
    #text(BIG_TEXT_F, (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN - MARGIN*3.75))
    #text(BIG_TEXT_G, (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN - MARGIN*4.50))


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
#    draw_divider_lines()
#    draw_auxiliary_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    print("DrawBot: Done")
