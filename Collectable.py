class Collectable:
    def __init__(self, project, id_number, attributes_names, attributes_values):
        # string containing the name of the project the collectable is part of
        self.project = project
        # unique number identiying the collectable inside the collection
        self.id = id_number
        # tuple containing all the attributes names
        self.attributes_names = attributes_names
        # tuple containing all the attributes values
        self.attributes_values = attributes_values

    def __str__(self):
        return 'Collectable #{} of {} project.\n'.format(self.id, self.project)
