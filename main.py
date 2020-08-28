from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
import os
from creator import ImageCreator


p = sys.argv[1]
print(p)

c = ImageCreator(p)

nome = p.replace(".java", ".png")

c.im.save(nome)




