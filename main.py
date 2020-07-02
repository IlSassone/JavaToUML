from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys
import os
from creator import ImageCreator
import networkx as nx
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np


p = sys.argv[1]
print(p)

c = ImageCreator(p)

nome = p.replace(".java", ".png")

c.im.save(nome)




