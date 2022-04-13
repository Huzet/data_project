#! /usr/bin/env python3
""""
Project reqs:
https://github.com/csfeeser/Python/blob/master/TLG/get_data_project.md

Pokemon API:
https://pokeapi.co/docs/v2#evolution-section

Description:
Script that can be quickly used to compare pokemon

TODO
[X] Argparse for using arguments
[X] Pull both pokemon data
[X] Compare Data
[ ] Write tests
[ ] Give diff of comparison
[ ] Pandas graph it 

Author: Tomas
v1
"""
import argparse
import requests

# argparse through arguments (user will pick what they want to see about pokemon)
parser = argparse.ArgumentParser(
    description="A script that is used to get base stats on 1 pokemon or can compare 2 pokemon")
parser.add_argument("-s",
                    "--stat",
                    type=str,
                    help="Get stats for one pokemon"
                    )
parser.add_argument("-c",
                    "--compare",
                    nargs=2,
                    metavar=("pk1", "pk2"),
                    help="Compare stats of 2 pokemon")
args = parser.parse_args()

if (args.stat == None and args.compare == None):
    print("Please use the -h or --help to get assistance: compare_pokemon.py -h ")

# takes id or name at the end
url_pokemon_stats = "https://pokeapi.co/api/v2/pokemon/"

# get pokemon data
def get_stats(pokemon_name):
    response = requests.get(url_pokemon_stats + pokemon_name)
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_dict = {"name": pokemon_data["forms"][0]["name"],
                        "hp": pokemon_data["stats"][0]["base_stat"],
                        "attack": pokemon_data["stats"][1]["base_stat"],
                        "defense": pokemon_data["stats"][2]["base_stat"],
                        "special_attack": pokemon_data["stats"][3]["base_stat"],
                        "special_defense": pokemon_data["stats"][4]["base_stat"],
                        "speed": pokemon_data["stats"][5]["base_stat"]
                        }
        return pokemon_dict

    else:
        print(
            f"Something went wrong. You either put in invalid pokemon name or timeout. Your error {response.status_code}")

# Main function that runs program
def main():
    if args.stat != None:
        # get argument
        pokemon_name = args.stat
        # get data
        pokemon_data = get_stats(pokemon_name)
        # pretty print for user
        dict_keys = list(pokemon_data)
        for index in range(0, len(dict_keys)):
            print("%-17s= %-12s"
                  % (dict_keys[index], pokemon_data[dict_keys[index]])
                  )

    elif args.compare != None:
        # get arguments
        pokemon_1, pokemon_2 = args.compare
        # get data
        pokemon_data_1 = get_stats(pokemon_1)
        pokemon_data_2 = get_stats(pokemon_2)
        # pretty print for user
        dict_keys = list(pokemon_data_1)
        for index in range(0, len(dict_keys)):
            print("%-17s= %-12s %-15s"
                  % (dict_keys[index], pokemon_data_1[dict_keys[index]], pokemon_data_2[dict_keys[index]])
                  )

if __name__ == "__main__":
    main()