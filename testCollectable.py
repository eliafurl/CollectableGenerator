from collectable import Collectable
import cv2 as cv

def main():
    project = 'Test'
    id_number = 3
    attributes_names = ('BG', 'CORE', 'STAR')
    attributes_values = ('GREEN', 'BLU', '1')
    attribute_imgs = ('./TestProject/source_layers/00-BG/BG-GREEN.png',\
                      './TestProject/source_layers/01-CORE/CORE-BLU.png',\
                      './TestProject/source_layers/02-STAR/STAR-1.png')

    new_collectable = Collectable(project, id_number, attributes_names, attributes_values, attribute_imgs)

    print(new_collectable)
    print('Hash = {}'.format(hash(new_collectable)))
    assert(new_collectable.identifier == hash(new_collectable))

    stacking_result = new_collectable.exportCollectable()
    cv.imshow('Test collectable stacking', stacking_result)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__=='__main__':
    main()
    print('DONE!')