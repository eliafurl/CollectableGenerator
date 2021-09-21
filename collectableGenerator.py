# Implementation of the CollectableGenerator class
from collectable import Collectable
from utilities import *

class CollectableGenerator:
    def __init__(self, project, main_folder):
        # List containing all the collectables objects
        self.collectables = []
        # String of the project name
        self.project = project
        # String of the path to the main folder of the project
        self.main_folder = main_folder

    def addCollectable(self):
        id_number = len(self.collectables) + 1
        new_collectable = Collectable(self.project, id_number, self.main_folder)
        self.collectables.append(new_collectable)


    def __str__(self):
        return 'Collectable generator of {} project.\nActual number of collectables = {}\n'.format(self.project, len(self.collectables))