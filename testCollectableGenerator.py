from collectableGenerator import CollectableGenerator

def main():
    project = 'Test'
    main_folder = './TestProject' 
    collectableGenerator = CollectableGenerator(project, main_folder)

    collectableGenerator.addCollectable()

    print(collectableGenerator)



if __name__ == '__main__':
    main()
    print('DONE!')