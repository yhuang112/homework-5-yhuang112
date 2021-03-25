if __name__ == "__main__":
    pokemon =("picachu", "charmander", "bulbasaur")
    print(pokemon[1])

    unpack_pokemon = tuple(pokemon)
    starter1,starter2,starter3=unpack_pokemon
    print(starter1)
    print(starter2)
    print(starter3)
    
    myname =tuple("Yaling")
    print(myname)

    print("i" in myname)

    intergers = range(2,11)
    for interger in intergers:
        print(interger)
 
    i=2
    while i<11:
        print(i)
        i+=1

    strings = "This is a simple string"
    # print(strings)
    for string in strings:
        print(string)

    sets = ("this","is","a","simple","set")
    for i in range(1,4):
        for charter in sets:
            print(f"{i} + {charter}")
                
                    
        
