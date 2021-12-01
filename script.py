import cv2
import pyautogui

def load_bw_img(filename):
    original = cv2.imread(filename)
    grayImage = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    _ ,blackAndWhiteImage = cv2.threshold(grayImage, 85, 255, cv2.THRESH_BINARY)
    #cv2.imshow("viewer", grayImage)
    return blackAndWhiteImage

# Pixel by Pixel B/W
def draw_slow(bw, x_coord, y_coord):
    pyautogui.moveTo(x_coord, y_coord)
    y = y_coord
    for col in bw:
        x = x_coord  
        y += 1
        for i in col:
            x += 1
            if i != 255:
                pyautogui.moveTo(x, y)
                pyautogui.click()

# Pixel by pixel in color
def draw_color(img, x_coord, y_coord):
    last_color = None
    pyautogui.moveTo(x_coord, y_coord)
    y = y_coord
    for col in img:
        x = x_coord  
        y += 1
        for i in col:
            b, g, r = (i)
            x += 1
            if last_color == None or [last_color[0]//10, last_color[1]//10, last_color[2]//10] != [r//10, g//10, b//10]:
                last_color = [r, g, b]
                change_color(r, g, b)
            if [r, g, b] != [255, 255, 255]:
                pyautogui.moveTo(x, y)
                pyautogui.click()

# Draws as lines in black and white
def draw_faster(bw, x_coord, y_coord):
    pyautogui.moveTo(x_coord, y_coord)
    y = y_coord
    for col in bw:
        x = x_coord  
        y += 1
        is_black = False
        f_black = None
        for i in col:
            if i == 255:
                if is_black:
                    pyautogui.moveTo(f_black)
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(x, y)
                    pyautogui.mouseUp(button='left')
                    is_black = False
                    f_black = None
            else:
                if not is_black:
                    is_black = True
                    f_black = (x, y)
            x += 1

# Function to change color
def change_color(r, g, b):
    edit_color = (1000, 75) # Revise with coordinates for edit_colors button for your machine
    r_value = (1158, 595) # Revise with coordinates for R field for your machine
    pyautogui.click(edit_color)
    pyautogui.doubleClick(r_value)
    pyautogui.write(str(r))
    pyautogui.press('tab')
    pyautogui.write(str(g))
    pyautogui.press('tab')
    pyautogui.write(str(b))
    pyautogui.press('enter')


if __name__ == "__main__":
    x = 30 # Change depending on X/Y coordinates of your machine for where to start drawing
    y = 170
    #bw_img = load_bw_img("baldski.jpg")
    img = cv2.imread("baldski.jpg", cv2.IMREAD_UNCHANGED)
    
	# while True:
	#       print(pyautogui.position()) # Uncomment this to find coordinates

    #draw_slow(bw_img, x, y)
    #draw_faster(bw_img, x, y)
    draw_color(img, x, y)
