import os
import shutil
from decimal import getcontext, Decimal
from random import choice
from time import time

from PIL import Image

from glitch_this import ImageGlitcher


def test_image_to_image():
    """
     Example of getting a glitched Image and saving it
     We use glitch_level = 2 in this example
     You may change this to whatever you'd like
    """

    # # All default params(i.e color_offset = False, scan_lines = False)
    glitch_img = glitcher.glitch_image(f"static/images/test1.{fmt}", 2)
    glitch_img.save(f"Collections/glitched_test_default.{fmt}")
    #
    # # Now try with scan_lines set to true
    # glitch_img = glitcher.glitch_image(f"test.{fmt}", 2, scan_lines=True)
    # glitch_img.save(f"Collections/glitched_test_scan.{fmt}")
    #
    # # Now try with color_offset set to true
    # glitch_img = glitcher.glitch_image(f"test.{fmt}", 2, color_offset=True)
    # glitch_img.save(f"Collections/glitched_test_color.{fmt}")
    #
    # # Now try glitching with a seed
    # # This will base the RNG used within the glitching on given seed
    # glitch_img = glitcher.glitch_image(f"test.{fmt}", 2, seed=42)
    # glitch_img.save(f"Collections/glitched_test_seed.{fmt}")

    # How about all of them?
    glitch_img = glitcher.glitch_image(f'static/images/test1.{fmt}', 2, color_offset=True, scan_lines=True, seed=42)
    glitch_img.save(f'Collections/glitched_test_all.{fmt}')
    #
    # # You can also pass an Image object inplace of the path
    # # Applicable in all of the examples above
    # img = Image.open(f"test.{fmt}")
    # glitch_img = glitcher.glitch_image(
    #     img, 2, color_offset=True, scan_lines=True, seed=42
    # )
    # glitch_img.save(f"Collections/glitched_test_all_obj.{fmt}")


if __name__ == "__main__":
    # Create the ImageGlitcher object
    glitcher = ImageGlitcher()
    if os.path.isdir("Collections"):
        shutil.rmtree("Collections")
    os.mkdir("Collections")

    # Start Testing
    # Set format of test image to png (file being used is test.png)
    fmt = "jpg"

    test_image_to_image()
