"""start.py

Author: Xi Che
Date: Dec 10
"""

import sys
import xmltodict
import argparse

from solver import Solver
from pprint import pprint


def solution_func(map_path, start_point, object_list):
    return Solver(map_path, start_point, object_list)

def process_scenario(scenario_path):
    try:
        with open(scenario_path) as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        return content[0], content[1:]
    except:
        print("Something wrong with the scenario file.")



if __name__ == '__main__':
    arguments_parser = argparse.ArgumentParser(description='Solver for Maze!')
    arguments_parser.add_argument('-c', '--scenario', required=False,\
        help='path to scenario', type=str)
    arguments_parser.add_argument('-m', '--map', required=False,\
        help='path of map', type=str)
    arguments_parser.add_argument('-s', '--start_point', required=False,\
        help='start point for search', type=str)
    arguments_parser.add_argument('-t', '--targets', nargs='+', required=False,\
        help='object to collect', type=str)

    args = arguments_parser.parse_known_args()[0]
    
    if args.map and args.start_point and args.targets:

        map_path = args.map
        start_point = args.start_point
        object_list = args.targets
    
    elif args.scenario and not (args.map or args.start_point or args.targets):
        map_path = "map.xml"
        start_point, object_list = process_scenario(args.scenario)

    
    print("-------------- User Enter Info -----------------")
    print("The map location is ", map_path)
    print("You are starting from ", start_point)
    print("All the objects are ", object_list)
    print()
    print("-------------- Start -----------------")
    solution = Solver(map_path, start_point, object_list) # solution_func(map_path, start_point, object_list)
    solution.print_solution()

    print("--------------- End ------------------")


    # pdf_parser = Model(options.input)
    # # print('(the' in pdf_parser.tokenize_original)
    # print(pdf_parser.title, pdf_parser.parties, pdf_parser.persons, pdf_parser.effective_dates)
    # with open("sample.txt", "w") as text_file:
    #     text_file.write(pdf_parser.raw_text)
    # pdf_parser.write_json_output(pdf_parser.features_obj.features, 'sample.json')