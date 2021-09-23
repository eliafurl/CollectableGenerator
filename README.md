# Collectable Generator Project
This repository contains the Collectable Generator. It is a simple tool for generating random collectables from sample pngs, stacking a defined number of layers and exporting the final image as png. OpenCV has been used for the image processing.

### Project Folder structure:
```
testProject:
|
|-- source_layers:
|   | 
|   |-- 00-BG:             layer-0
|   |   |-- BG-GREEN.png
|   |   |-- BG-NO.png
|   |
|   |-- 01-CORE:           layer-1
|   |   |-- CORE-BLU.png
|   |   |-- CORE-GREEN.png
|   |
|   |-- 02-STAR:           layer-2
|   |   |-- STAR-1.png
|   |   |-- STAR-2.png
|   |   |-- STAR-3.png
|   |   |-- STAR-4.png
|
|-- TBD: exported collectable pngs
```

### CollectableGenerator
This is a class used for creating a collectable project. It contains all the possible attributes, all the methods for the generation and export of all the collectables. 

### Collectable
This is a class for storing all the informations about a single collectable. 

### Utilities
This is a collection of useful methods.
