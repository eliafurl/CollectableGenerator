#Collection of utilities funcitons for collectableGenerator
import cv2 as cv

def stackLayers(underlay_layer, overlay_layer):
    # Create a ROI on the underlay image
    rows,cols,channels = overlay_layer.shape
    roi = underlay_layer[0:rows, 0:cols]

    # Create a mask and its inverse of the overlay image
    img2gray = cv.cvtColor(overlay_layer, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 1, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)

    # Black-out the area of the non-black overlay layer in ROI
    target_underlay_layer = cv.bitwise_and(roi, roi, mask = mask_inv)

    # Take only region of not-black pixels from overlay layer
    target_overlay_layer = cv.bitwise_and(overlay_layer, overlay_layer, mask = mask)

    # Put overlay in ROI and modify the main layer
    stacked_layer = cv.add(target_underlay_layer, target_overlay_layer)

    #underlay_layer[0:rows, 0:cols] = stacked_layer #Needed if the overlay layer has different dimension

    return stacked_layer