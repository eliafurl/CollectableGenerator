from collectable import Collectable

def main():
    project = 'Test'
    id_number = 3
    attributes_names = ('BG', 'CORE', 'STAR')
    attributes_values = ('GREEN', 'BLU', '1')

    new_collectable = Collectable(project, id_number, attributes_names, attributes_values)

    print(new_collectable)

if __name__=='__main__':
    main()
    print('DONE!')