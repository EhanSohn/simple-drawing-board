import numpy as np
import cv2 as cv

global font, bgrTrack, mouseState, canvas
font = cv.FONT_ITALIC
bgrTrack = {'B': 0, 'G': 0, 'R': 0}
mouseState = [False, (-1, -1)]

# Prepare canvas and instantiate a window
canvas = np.full((480, 640, 3), 255, dtype=np.uint8)
windowName = "DRAWING BOARD"
cv.namedWindow(windowName)

# Update value of 'R'
def updateRValue(x):
    bgrTrack['R'] = x

# Update value of 'G'
def updateGValue(x):
    bgrTrack['G'] = x

# Update value of 'B'
def updateBValue(x):
    bgrTrack['B'] = x

# just pass
def passing(x):
    pass

# Change 'mouse_state' (given as 'param') according to the mouse 'event
def mouseEventHandler(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
        # Draw a point with circle
        cv.circle(canvas, (x, y), cv.getTrackbarPos("Brush Size", windowName),
                       (cv.getTrackbarPos("B", windowName),
                        cv.getTrackbarPos("G", windowName),
                        cv.getTrackbarPos("R", windowName)),
                        -1)
    elif event == cv.EVENT_MOUSEMOVE and param[0]:
        param[1] = (x, y)
        # Draw a point with circle
        cv.circle(canvas, (x, y), cv.getTrackbarPos("Brush Size", windowName),
                    (cv.getTrackbarPos("B", windowName),
                     cv.getTrackbarPos("G", windowName),
                     cv.getTrackbarPos("R", windowName)),
                     -1)

# Show on canvas
cv.createTrackbar("Brush Size", windowName, 1, 10, passing)
cv.createTrackbar("R", windowName, 0 ,255, updateRValue)
cv.createTrackbar("G", windowName, 0, 255, updateGValue)
cv.createTrackbar("B", windowName, 0, 255, updateBValue)
cv.setMouseCallback(windowName, mouseEventHandler, mouseState)

while(1):
    cv.imshow(windowName, canvas)
    # esc to exit
    key = cv.waitKey(1)
    if key == 27: # ESC
        break

cv.destroyAllWindows()