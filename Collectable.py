class Collectable:
    def __init__(self, project, id_number, attributes_names, attributes_values, attributes_imgs):
        # string containing the name of the project the collectable is part of
        self.project = project
        # unique number identiying the collectable inside the collection
        self.id = id_number
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