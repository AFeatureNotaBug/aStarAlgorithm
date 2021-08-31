from Map import Map
import sys


allMaps = dict()    # Stores all open maps in a current session

while True:
    ask = input(": ").lower()
    
    #Help
    if ask == "help":
        print(
            "\nThis is the help section\n\n" +
            "help will show this menu\n" +
            "load to load a saved map\n" +
            "save to save a generated map\n" +
            "random to generate a random map\n" +
            "list to list all loaded maps\n" +
            "a to use A* algorithm on an existing map\n" +
            "quit to exit\n"
        )
    
    #Load
    if ask == "load":
        askFilename = input("Enter map name: ")
        askStorageName = input("Enter name to store map under: ")
        
        allMaps[askStorageName] = Map.load(askFilename)
        print("\n")
        
    #Save
    if ask == "save":
        askMapName = input("Enter name of map in current session: ")
        askFilename = input("Enter filename name: ")
        
        Map.save(allMaps[askMapName], askFilename)
        print("\n")
    
    #Random map
    if ask == "random":
        askMapName = input("Enter name for new map: ")
        askMapSize = input("Enter size for new map: ")
        askNodeCount = input("Enter number of nodes for new map: ")
        
        print("\nGenerating random map...")
        
        newMap = Map(int(askMapSize))
        newMap.randomMap(int(askNodeCount), 3)
        allMaps[askMapName] = newMap
        
        print("Map creation successful!\n")
    
    #List
    if ask == "list":
        for mapName in allMaps:
            print(mapName)
            
        print("\n")
    
    #A*
    if ask == 'a':
        askMapName = input("Enter map name: ")
        allMaps[askMapName].aStar()
        
        print("\n")
        
    #Quit
    if ask == "quit":
        sys.exit(0)
