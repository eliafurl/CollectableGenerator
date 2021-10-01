# Implementation of the CollectableGenerator class
from collectable import Collectable
from utilities import *
import os
from os.path import isdir, join
import random
from cv2 import imwrite

class CollectableGenerator:
    def __init__(self, project, project_folder):
        # sictionary containing all the collectables objects and their identifier as key
        self.collectables = {}
        # string of the project name
        self.project = project
        # string of the path to the main folder of the project
        self.project_folder = project_folder
        # export directory for the collectables inside the project collection
        self.export_folder = join(project_folder, 'exported_collectables')
        # dictionary for storing all the layers and its attributes name and location
        self.attributes = {}
        self.attributes_names = -1
        self.total_possible_collectables = -1
        attributes_path = join(project_folder, 'source_layers')
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
        self.total_possible_collectables = 1
        current_layer_attributes = 0
        attribute_names = []
        for attribute_dir in sorted(attributes_dir):

            if isdir(join(attributes_path, attribute_dir)):

                temp = attribute_dir.split('-')
                layer_number = temp[0] # key
                attribute_name = temp[1]
                attribute_names.append(attribute_name)
                attribute_dictionary = {}

                for attribute in os.listdir(join(attributes_path, attribute_dir)):

                    current_layer_attributes += 1
                    temp = attribute.split('-')
                    key = temp[1][:-4]
                    value = join(attributes_path, attribute_dir, attribute)
                    attribute_dictionary[key] = value

                attribute_layer = attribute_dir.split('-')[0]
                self.attributes[layer_number] = (attribute_name, attribute_dictionary)
                self.total_possible_collectables *= current_layer_attributes
            current_layer_attributes = 0

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
            return 1
        else:
            print('[WARNING]\n{}\nalready in current collectables collection.\n\n'.format(new_collectable))
            return 0

    def createCollectableCollection(self, collectable_desired_number, method):
        '''
        This function create a collection of #collectable_number colletables. If a collectable
        is already part of the collection it is not duplicated, therefore all the collectables 
        inside the collection are unique.
        '''
        collectables_to_be_created = min(collectable_desired_number, self.total_possible_collectables) 
        
        while collectables_to_be_created != len(self.collectables):
            _ = self.createCollectable(method)
        print('Created {} collectables.'.format(len(self.collectables)))

    def exportCollectableCollection(self):
        '''
        This function exports each collectable as individual image inside the self.export_folder
        with the correspondent metadata as json file. 
        '''
        for collectable_key in self.collectables.keys():
            collectable = self.collectables[collectable_key]
            # create the collectable image stacking all the attributes
            img = collectable.exportCollectable()
            # export the image
            imwrite('{}/{}.png'.format(self.export_folder, collectable.name), img)
            # export the metadata
            collectable.exportMetadata('{}/{}.json'.format(self.export_folder, collectable.name))

    def __str__(self):
        return 'Collectable generator of {} project.\nActual number of collectables inside the collection= {}/{}\n'\
        .format(self.project, len(self.collectables), self.total_possible_collectables)



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
