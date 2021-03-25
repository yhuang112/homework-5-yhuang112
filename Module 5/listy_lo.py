if __name__ == "__main__":
    food =["rice","beans"]
    print(food)
    food.append("broccoli")
    print(food)

    add=["bread","pizza"]
    food.extend(add)
    print(food)
    print(food[slice(0,2)])
    print(food[len(food)-1])

    mystrings= "eggs,fruit,orange juice"
    print(mystrings)

    breakfast=mystrings.split(",")
    print(breakfast)
    print(len(breakfast))


    numlist=[]
    while True:
        inputnumber = input("please enter a number: ")

        if inputnumber =="stop":
            break
        value = float(inputnumber)
        numlist.append(value)

    average = sum(numlist)/len(numlist)
    minimal = min(numlist)
    maximal = max(numlist)

    print(f"Average: {average}")
    print(f"Minimal: {minimal}")
    print(f"Maximal: {maximal}")

    




    
    