from Map import Map
import sys, os


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
        print("\nMaps directory:\n", os.listdir("Maps"), "\n")
        
        askFilename = input("Enter map name: ")
        
        try:
            loadMap = Map.load(askFilename)
            
            askStorageName = input("Enter name to store map under: ")
            allMaps[askStorageName] = Map.load(askFilename)
            
        except:
            print("No map with given filename")
            
        print("\n")
        
    #Save
    if ask == "save":
        mapNames = [mapName for mapName in allMaps]
        
        askMapName = input("Enter name of map in current session: ")
        
        if askMapName in mapNames:
            askFilename = input("Enter filename name: ")
            
            if askFilename + ".map" in os.listdir("Maps"):
                askOverwrite = input("This will overwrite an existing map. Continue? (yes/no)").lower()
                
                if askOverwrite == "yes":
                    Map.save(allMaps[askMapName], askFilename)
                    
            else:
                Map.save(allMaps[askMapName], askFilename)
        
        else:
            print("No map with the given name exists")
        
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
        print([mapName for mapName in allMaps], "\n")
    
    #A*
    if ask == 'a':
        askMapName = input("Enter map name: ")
        allMaps[askMapName].aStar()
        
        print("\n")
        
    #Quit
    if ask == "quit":
        sys.exit(0)
