import csv

def charger_pokémons_csv(fichier):
    pokemons = {}
    with open(fichier,"r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            nom_pokemon = row[0]
            stats = list(map(int,row[1:]))
            pokemons[nom_pokemon] = stats

        return pokemons

pkmn1 = charger_pokémons_csv("pokemon.csv")
for nom, stats in pkmn1.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokémons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
