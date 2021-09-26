from collectableGenerator import CollectableGenerator

def main():
    project = 'Test'
    main_folder = './TestProject' 
    collectableGenerator = CollectableGenerator(project, main_folder)
    
    # import pdb; pdb.set_trace()

    collectableGenerator.createCollectable()

    print(collectableGenerator)



if __name__ == '__main__':
    main()
    print('DONE!')