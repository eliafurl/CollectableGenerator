class Collectable:
    def __init__(self, project, id_number, main_folder):
        # Name of the project the collectable is part of
        self.project = project
        # Unique number identiying the collectable inside the collection
        self.id = id_number
        # Main folder of the project 
        self.main_folder = main_folder
        # Dictionary containing all the attributes and their values
        self.attributes = {}
        # Export folder for the collectable image
        self.export_folder = ""

    def __str__(self):
        return "Collectable #{} of {} project.".format(self.id, self.project)
