from collectable import Collectable

def main():
    project = 'Test'
    id_number = 3
    main_folder = 'TestProject'

    new_collectable = Collectable(project, id_number, main_folder)

    print(new_collectable)

if __name__=='__main__':
    main()
    print('DONE!')