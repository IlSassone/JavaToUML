from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
from creator import ImageCreator



c = ImageCreator("Impiegato.java")

c.im.save("output.png")

