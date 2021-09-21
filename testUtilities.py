from utilities import *
import cv2 as cv
import pdb

def main():
    bg_layer_path = 'TestProject/images/BG/BG-GREEN.png'
    core_layer_path = 'TestProject/images/CORE/CORE-BLU.png'
    
    bg_layer = cv.imread(bg_layer_path, cv.IMREAD_COLOR)
    core_layer = cv.imread(core_layer_path, cv.IMREAD_COLOR)

    result = stackLayers(bg_layer, core_layer)

    to_display_img = [bg_layer, core_layer, result]
    to_display_names = [bg_layer_path, core_layer_path, 'Result']
    for i in range(3):
        cv.imshow(to_display_names[i], to_display_img[i])
        cv.waitKey(0)
        cv.destroyAllWindows()




if __name__ == '__main__':
    main()

    print('DONE!')