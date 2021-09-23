# Implementation of the CollectableGenerator class
from collectable import Collectable
from utilities import *
import os
from os.path import isdir, join

class CollectableGenerator:
    def __init__(self, project, project_folder):
        # List containing all the collectables objects
        self.collectables = []
        # String of the project name
        self.project = project
        # String of the path to the main folder of the project
        self.project_folder = project_folder
        attributes_path = join(project_folder, 'source_layers')
        self.attributes = self.loadAttributes(attributes_path)

    def loadAttributes(self,attributes_path):
        attributes_dir = os.listdir(attributes_path)
        attributes = {}
        for attribute_dir in sorted(attributes_dir):
            if isdir(join(attributes_path, attribute_dir)):
                attribute_dictionary = {}
                '''
                TODO: fix this into the following:
                attributes = { '00' : ('BG', attributes_dictionary)}
                attributes_dictionary = {'GREEN', 'absolute/path/to/png'}
                '''
                for attribute in os.listdir(join(attributes_path, attribute_dir)):
                    temp = attribute.split('-')
                    key = temp[0]
                    value = temp[1][:-4]
                    #print('key = {}\nvalue = {}\n\n'.format(key, value))
                    attribute_dictionary[key] = value
                print(attribute_dir)
                attribute_layer = attribute_dir.split('-')[0]
                print('attribute_name = {}\nattribute_dictionary = {}\n\n'.format(attribute_name, attribute_dictionary))
                attributes[attribute_layer] = attribute_dictionary



        print(attributes_dir)
        return attributes

    def addCollectable(self):
        id_number = len(self.collectables) + 1
        new_collectable = Collectable(self.project, id_number, self.project_folder)
        self.collectables.append(new_collectable)


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
        # attributes = { '00' : ('BG', attributes_dictionary)}
        # attributes_dictionary = {'GREEN', 'absolute/path/to/png'}
