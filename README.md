# data_project
Python project that gathers data from Pokemon API and allows user to compare to Pokemon stats

# usage
```
./compare_pokemon.py -s pikachu
name             = pikachu     
hp               = 35          
attack           = 55          
defense          = 40          
special_attack   = 50          
special_defense  = 50          
speed            = 90  

./compare_pokemon.py -c pikachu charizard
name             = pikachu      charizard      
hp               = 35           78             
attack           = 55           84             
defense          = 40           78             
special_attack   = 50           109            
special_defense  = 50           85             
speed            = 90           100   

./compare_pokemon.py
usage: compare_pokemon.py [-h] [-s STAT] [-c pk1 pk2]

A script that is used to get base stats on 1 pokemon or can compare 2 pokemon

options:
  -h, --help            show this help message and exit
  -s STAT, --stat STAT  Get stats for one pokemon
  -c pk1 pk2, --compare pk1 pk2
```
