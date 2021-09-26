from utilities import *
import cv2 as cv
import pdb

# pdb.set_trace() for DEBUGGING

def test_stackLayers():
    bg_layer_path = 'TestProject/images/BG/BG-GREEN.png'
    core_layer_path = 'TestProject/images/CORE/CORE-BLU.png'

    bg_layer = cv.imread(bg_layer_path, cv.IMREAD_UNCHANGED)
    core_layer = cv.imread(core_layer_path, cv.IMREAD_UNCHANGED)

    result = stackLayers(bg_layer, core_layer)

    cv.imwrite('TestProject/testOutputs/stackLayers_result.png', result)

    to_display_img = [bg_layer, core_layer, result]
    to_display_names = [bg_layer_path, core_layer_path, 'Result']
    for i in range(3):
        cv.imshow(to_display_names[i], to_display_img[i])
        cv.waitKey(0)
        cv.destroyAllWindows()

def test_metadataJsonExport():
    metadata = { 'name': 'testName',\
                 'project': 'TestProject',\
                 'numberID': '01',\
                 'hashID': '',\
                 'image': 'IPFS URI',\
                 'attributes': ["BG-GREEN", "CORE-BLU", "STAR-1"],\
                 'author': 'me',
               }
    print(metadata)
    json_export_file = 'TestProject/testOutputs/metadataTest_export.json'
    metadataJsonExport(metadata, json_export_file)

def test_metadataJsonImport():
    json_import_file = 'TestProject/testOutputs/metadataTest_export.json'
    metadata = metadataJsonImport(json_import_file)
    print(metadata)
    for key in metadata.keys():
        print('\n{} = {}'.format(key, metadata[key]))

def main():
    # test_stackLayers()
    print('------------------test_metadataJsonExport----------------')
    test_metadataJsonExport()
    print('---------------------------------------------------------\n')
    print('------------------test_metadataJsonExport----------------')
    test_metadataJsonImport()
    print('---------------------------------------------------------\n')




if __name__ == '__main__':
    main()

    print('\n\nDONE!\n\n')