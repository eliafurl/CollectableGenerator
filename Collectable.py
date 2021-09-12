class Collectable:
    def __init__(self, project, id_number, main_folder):
        self.project = project
        self.id = id_number
        self.main_folder = main_folder
        self.attributes = {}
        self.export_folder = ""

    def __str__(self):
        return "Collectable #{} of {} project.".format(self.id, self.project)
