from collectableGenerator import CollectableGenerator

def main():
    project = 'Test'
    main_folder = './TestProject' 
    collectableGenerator = CollectableGenerator(project, main_folder)
    
    # import pdb; pdb.set_trace()

    collectableGenerator.createCollectable('random_uniform')

    print(collectableGenerator)

    collectableGenerator.createCollectableCollection(100, 'random_uniform')

    for collectable in collectableGenerator.collectables:
        print(collectableGenerator.collectables[collectable])

    print('Total possible collectables = {}'.format(collectableGenerator.total_possible_collectables))


    print('---------test exportCollectableCollection---------')
    collectableGenerator.exportCollectableCollection()

if __name__ == '__main__':
    main()
    print('DONE!')