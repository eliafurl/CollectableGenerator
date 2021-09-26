#Collection of utilities funcitons for collectableGenerator
import cv2 as cv
import json

def stackLayers(background, foreground):
    '''
    This function overlay two RGBA images of the same size, using the 
    alpha composition (https://en.wikipedia.org/wiki/Alpha_compositing).
    '''
    # normalize alpha channels from 0-255 to 0-1
    alpha_background = background[:,:,3] / 255.0
    alpha_foreground = foreground[:,:,3] / 255.0

    # set adjusted colors
    for color in range(0, 3):
        background[:,:,color] = alpha_foreground * foreground[:,:,color] + \
            alpha_background * background[:,:,color] * (1 - alpha_foreground)

    # set adjusted alpha and denormalize back to 0-255
    background[:,:,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255

    return background

def metadataJsonExport(metadata, json_export_file):
    '''
    This function allows to export the metadata dictionary as a json file specified
    by json_export_file
    '''
    with open(json_export_file, 'w') as json_file:
        json.dump(metadata, json_file, indent = 4, sort_keys = False)

def metadataJsonImport(json_import_file):
    '''
    This function returns the metadata dictionary loaded form a json file specified
    by json_import_file
    '''
    with open(json_import_file) as json_file:
        return json.load(json_file)
