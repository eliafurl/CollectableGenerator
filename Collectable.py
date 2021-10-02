from cv2 import imread
from utilities import *

class Collectable:
    def __init__(self, project, id_number, attributes_names, attributes_values, attributes_imgs):
        # string containing the name of the project the collectable is part of
        self.project = project
        # unique number identiying the collectable inside the collection
        self.id = id_number
        # collectable name
        self.name = '{}-{}'.format(self.project, self.id)
        # tuple containing all the attributes names
        self.attributes_names = tuple(attributes_names)
        # tuple containing all the attributes values
        self.attributes_values = tuple(attributes_values)
        # tuple containing the path of the attributes images 
        self.attributes_imgs = tuple(attributes_imgs)
        # Hash which identify the collectable inside all the possible collectables from its attributes
        self.identifier = hash(self)

    def __str__(self):
        collectable_information = 'Collectable ({}) #{} of {} project.\nAttributes: {}\nAttributes values: {}\n'\
        .format(self.identifier, self.id, self.project, self.attributes_names, self.attributes_values)
        return collectable_information

    def __hash__(self):
        return hash((self.attributes_names, self.attributes_values))

    def exportCollectable(self):
        '''
        This function returns the stacked image of the collectable, composed of all attributes layers.
        '''
        background_path = self.attributes_imgs[0]
        background = imread(background_path, cv.IMREAD_UNCHANGED)
        for i in range(1,len(self.attributes_imgs)):
            foreground_path = self.attributes_imgs[i]
            foreground = imread(foreground_path, cv.IMREAD_UNCHANGED)
            background = stackLayers(background, foreground)
        return background

    def exportMetadata(self, json_export_file):
        '''
        This function export the collectable metadata as json file.

        TODO:
        - create IPFS URI
        - author
        '''
        metadata = { 'name': '{}-{}'.format(self.project, self.id),\
                     'project': self.project,\
                     'numberID': self.id,\
                     'hashID': self.identifier,\
                     'image': 'IPFS URI',\
                     'attributes': list(self.attributes_values),\
                     'author': 'me',
                    }
        metadataJsonExport(metadata, json_export_file)