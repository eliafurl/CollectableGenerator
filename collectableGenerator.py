# Implementation of the CollectableGenerator class
from collectable import Collectable
from utilities import *
import os
from os.path import isdir, join
import random

class CollectableGenerator:
    def __init__(self, project, project_folder):
        # Dictionary containing all the collectables objects and their identifier as key
        self.collectables = {}
        # String of the project name
        self.project = project
        # String of the path to the main folder of the project
        self.project_folder = project_folder
        attributes_path = join(project_folder, 'source_layers')
        # dictionary for storing all the layers and its attributes name and location
        self.attributes = {}
        self.attributes_names = -1
        self.loadAttributes(attributes_path)

    def loadAttributes(self,attributes_path):
        '''
        Function for loading all the attributes as dictionary as follows: e.g. layer 00
        self.attributes = { '00' : ('BG', attribute_dictionary)}
        attribute_dictionary = {'GREEN', 'absolute/path/to/png'}
        '''
        # find all the layers folders
        attributes_dir = os.listdir(attributes_path)
        # store in a dictionary an item for each layer with:
        # key = layer_number
        # value = (attribute_name, attribute_dictionary)
        attribute_names = []
        for attribute_dir in sorted(attributes_dir):

            if isdir(join(attributes_path, attribute_dir)):

                temp = attribute_dir.split('-')
                layer_number = temp[0] # key
                attribute_name = temp[1]
                attribute_names.append(attribute_name)
                attribute_dictionary = {}

                for attribute in os.listdir(join(attributes_path, attribute_dir)):

                    temp = attribute.split('-')
                    key = temp[1][:-4]
                    value = join(attributes_path, attribute_dir, attribute)
                    attribute_dictionary[key] = value

                attribute_layer = attribute_dir.split('-')[0]
                self.attributes[layer_number] = (attribute_name, attribute_dictionary)

        self.attributes_names = tuple(attribute_names)

    def createCollectable(self, method):
        '''
        This function create a new collectable. 

        TODO: implement more sophysticated methods for attribute selection
        '''
        id_number = len(self.collectables) + 1
        # TODO: decide how to choose the attributes
        attributes_values = []
        attributes_imgs = []
        # choose the attributes randomly all with the same probability
        if method == 'random_uniform':
            for layer in self.attributes.keys():
                # choose randomly between the attributes of the attribute dictionary
                choosen_attribute = random.choice(list(self.attributes[layer][1]))
                choosen_attribute_img = self.attributes[layer][1][choosen_attribute]
                attributes_values.append(choosen_attribute)
                attributes_imgs.append(choosen_attribute_img)
        
        new_collectable = Collectable(self.project, id_number, self.attributes_names, attributes_values, attributes_imgs)
        # add the new collectable to the collection only if it is not already available 
        if not new_collectable.identifier in self.collectables:
            self.collectables[new_collectable.identifier] = new_collectable
        else:
            print('[WARNING]\n{}\nalready in current collectables collection.\n\n'.format(new_collectable))



    def __str__(self):
        return 'Collectable generator of {} project.\nActual number of collectables = {}\n'.format(self.project, len(self.collectables))



        '''
        Attributes:
            ---------------------
            layer-0: BG
                * BG-GREEN.png
                * BG-NO.png
            ---------------------
            layer-1: CORE
                * CORE-BLU.png
                * CORE-GREEN.png
            ---------------------
            layer-2: STAR
                * STAR-1.png
                * STAR-2.png
                * STAR-3.png
                * STAR-4.png
            ---------------------
        '''
