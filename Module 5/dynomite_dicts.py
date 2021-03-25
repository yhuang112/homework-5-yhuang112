if __name__ =="__main__":
    pokedex ={
        'Venosaur': ['Grass', 'Poisen'],
        'Charizard': ['Fire', 'Flying'],
        'Blastoise': ['Water']  
    }
    # print(pokedex)

    del pokedex["Blastoise"]

    print(pokedex)