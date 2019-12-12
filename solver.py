import sys
import xmltodict
import pandas as pd
from pprint import pprint

class Solver:
    def __init__(self, map_path='map.xml', start_point=None, targets=[]):
        """Solver class for solve the A-Maze-ingly Retro Route Puzzle 
        
        Args:
            map_path (str, optional): the path to the map location. Defaults to 'map.xml'.
            start_point (str, optional): starting room for search the objects. Defaults to None.
            targets (list, optional): list of objects to be collected. Defaults to [].
        """
        self.map = self.get_map(map_path)
        self.targets = targets
        self.results = [['ID', 'Room', 'Object collected'], 
                        ["------", "------", "------"]]

        self.search_objects(self.get_room_from_id(start_point))
        

    def search_objects(self, current_room):
        """Function that search the object from the current room
        
        Args:
            current_room (class): current room need to be searched.
        
        """
        if not self.targets:
            return None
        
        targets_found = []
        for target in self.targets:
            try:
                for obj in [current_room['object']['@name']]:
                    if str(obj).lower() == str(target).lower():
                        targets_found.append(str(obj))
                        self.targets.remove(str(obj))
            except:
                pass
        
        if targets_found:
            targets_collected = ','.join(targets_found)
        else:
            targets_collected = 'None'
        
        self.results.append([current_room['@id'], current_room['@name'], targets_collected])
        
        self.navigate(current_room)
        
        

    def get_room_from_id(self, room_id):
        """Function that get the room dictionary from the map give a room_id.
        
        Args:
            room_id (str): room id that match the one in the map.
        
        Returns:
            dict: room dictionary
        """
        try:
            room = next((room for room in self.map if room["@id"] == room_id))#.next()
            if room:
                return room
            else:
                print("Room is not in the map.")
        except:
            print("Problem at 'get_room_from_id' function.")
    
    def navigate(self, current_room):
        """Function that basing on the current room to find the next sequence of rooms.
        
        Args:
            current_room (dict): currently searched room
        """
        current_room_loc = [i for i, room in enumerate(self.map) if room == current_room]

        if '@north' in current_room:
            new_room_id = current_room['@north']
            self.map[current_room_loc[0]].pop('@north')
            self.search_objects(self.get_room_from_id(new_room_id))

        if '@south' in current_room:
            new_room_id = current_room['@south']
            self.map[current_room_loc[0]].pop('@south')
            self.search_objects(self.get_room_from_id(new_room_id))

        if '@west' in current_room:
            new_room_id = current_room['@west']
            self.map[current_room_loc[0]].pop('@west')
            self.search_objects(self.get_room_from_id(new_room_id))

        if '@east' in current_room:
            new_room_id = current_room['@east']
            self.map[current_room_loc[0]].pop('@east')
            self.search_objects(self.get_room_from_id(new_room_id))

    def print_map(self):
        """Helper function that print out map
        """
        pprint(self.map)
    
    def get_map(self, map_path):
        """Helper function that process the map.
        
        Args:
            map_path (str): path to where map located
        
        Returns:
            dict: map dictionary
        """
        try:
            with open(map_path) as fd:
                map = xmltodict.parse(fd.read())['map']['room']
            return map
        except:
            print("Invalid map path!")
    
    def print_solution(self):
        """Helper function that print all the result.
        """
        results = pd.DataFrame(self.results)
        pprint( results )

if __name__ == '__main__':
    s = Solver()
    s.print_map()
    s.get_loc_from_id('pond')