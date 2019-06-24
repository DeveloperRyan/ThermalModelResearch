# -*- coding: utf-8 -*-

# TODO : Use a more accurate temperature formula that accounts for emissivity - Complete?
# Change equation to account for temperature range rather than having to re-calculate a formula
# Allow a user to click a point for the color rather than instantly taking what is under the cursor
# Add averaging and rounding since colors not always bnw due to low quality rasterization
# GUI ?
# Area Selection

import pyautogui
import math

# Get the color of the pixel the mouse cursor is over and correlate this to a temperature in Celsius
def run():
    # Correlates to temperature range of the color scale
    MIN_TEMP = 15
    MAX_TEMP = 40
    range = abs(MAX_TEMP - MIN_TEMP) # Gets the total range the temperatures span

    # Take the screenshot of of the screen & then get the color of the pixel under the mouse pointer
    img = pyautogui.screenshot()
    color = img.getpixel(pyautogui.position()) # Outputs a tuple of rgb()

    if not (color[0] == color[1] == color[2]):
        print("Color was not grayscale, run the program again over a grayscale image.")

    else:
        color = color[0] # Get the first value in the tuple (They should all be identical)


        # Function to calculate color distribution based on temperature range.
        # 255 is for 255 color range in grayscale (0-255)
        # Original function : f(x, y, z) = (((|z-y|)/255)*x)+y x:color, y: min, z: max

        # Equation calculted using camera calibration measurement data - See PixelTemp.xlsx
        temp = 0.1094 * color + 17.381
        temp = round(temp, 5) # Round the temperature to 2 decimal decimal places
        print("Color: {}\nTemperature: {} \xb0C".format(color, temp)) # Output the formatted temperature


if __name__ == "__main__":
    run()
