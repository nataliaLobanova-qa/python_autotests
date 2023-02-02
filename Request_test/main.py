import requests
import json 

token = '05b137e42225e8820497c38374719eeb'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json' ,'trainer_token' : token},
json = {
    "name": "Бальтазар3000",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print (response.text)




response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json' ,'trainer_token' : token},
json = {
    "pokemon_id": 3301,
    "name": "Сатоши",
    "photo": ""
})

print(response_change.text)


response =requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json' ,'trainer_token' : token},
json = {
    "pokemon_id": "3301"
})

print(response.text)

