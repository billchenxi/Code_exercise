## Bill's Solution

### Notes:
First, the `map.xml` is different from the one showed in the `code_exercise.docx`. Specifically the room id is not integer in the given map, they are strings.

### Dependencies
The `requirements.txt` is my local environment, which includes a lot of extra unnecessary libraries. The most absolutely needed ones are:

```
python3.7
pandas
xmltodict
argparse
```

### How to run it

1. Clone the repo
2. At the repo directory, do following one of the two:
   a. `python start.py -c scenario.txt `
   or
   b. `python start.py -m map.xml -s dining-room -t "Pickaxe" "Book"`
3. example output would be:
```
Bills-MacBook-Pro:code_exercise bill$ python start.py -c scenario.txt 
scenario.txt
scullery
['Plate', 'Fishing-rod', 'Lamp', 'Book', 'Pickaxe', 'Pine-cone']
-------------- User Enter Info -----------------
The map location is  map.xml
You are starting from  scullery
All the objects are  ['Plate', 'Fishing-rod', 'Lamp', 'Book', 'Pickaxe', 'Pine-cone']

-------------- Start -----------------
                      0                      1                 2
0                    ID                   Room  Object collected
1                ------                 ------            ------
2              scullery               Scullery              None
3   secret-passage-west  Secret Passage (West)              None
4               library                Library              Book
5   secret-passage-west  Secret Passage (West)              None
6              scullery               Scullery              None
7               kitchen                Kitchen              None
8           dining-room            Dining Room             Plate
9               hallway                Hallway              None
10                porch                  Porch              None
11              hallway                Hallway              None
12          dining-room            Dining Room              None
13              kitchen                Kitchen              None
14             scullery               Scullery              None
15              library                Library              None
16              hallway                Hallway              None
17           front-yard             Front Yard              None
18           dirt-track             Dirt Track              None
19           front-yard             Front Yard              None
20                porch                  Porch              None
21                 pond                   Pond       Fishing-rod
22           dirt-track             Dirt Track              None
23                 mesa                   Mesa              None
24           dirt-track             Dirt Track              None
25            foothills              Foothills              None
26          pine-forest            Pine Forest         Pine-cone
27            foothills              Foothills              None
28                 mesa                   Mesa              None
29          scree-slope            Scree Slope              None
30        cave-entrance          Cave Entrance              None
31          scree-slope            Scree Slope              None
32          pine-forest            Pine Forest              None
33  secret-passage-east  Secret Passage (East)              None
34        cave-entrance          Cave Entrance              None
35           low-tunnel             Low Tunnel           Pickaxe
36        cave-entrance          Cave Entrance              None
37          huge-cavern            Huge Cavern              None
38  secret-passage-east  Secret Passage (East)              None
39  secret-passage-west  Secret Passage (West)              None
40  secret-passage-east  Secret Passage (East)              None
41         narrow-crawl           Narrow Crawl              None
42     underground-lake       Underground Lake              Lamp
--------------- End ------------------
```
