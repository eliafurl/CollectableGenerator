from collectableGenerator import CollectableGenerator

def main():
    project = 'Test'
    main_folder = './TestProject' 
    collectableGenerator = CollectableGenerator(project, main_folder)
    
    # import pdb; pdb.set_trace()

    collectableGenerator.createCollectable('random_uniform')

    print(collectableGenerator)
    for collectable in collectableGenerator.collectables:
        print(collectableGenerator.collectables[collectable])



if __name__ == '__main__':
    main()
    print('DONE!')