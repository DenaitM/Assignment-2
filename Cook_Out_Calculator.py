import math

print("\nWelcome to the cookout calculator!\n")
print("One pack of hot dogs contains: 10 hot dogs")
print("One pack of hot dog buns contains: 8 hot dog buns")

def getNumberOfPeople():
    numberofPeople = int(input("\nHow many people are attending the cookout? "))

    return numberofPeople


def getNumberOfHotdogs(numberofPeople):
    OnepackofHotdog = 10

    numberofHotdogs = input("\nHow many hotdogs will each person get? ")
    if numberofHotdogs == int(0):
        print("\nYou have entered 0 hotdogs, please enter a number greater than 0")
    elif int(numberofHotdogs) > 0: #lets assume 2 hotdogs per person
                            #assume 2 each person    #assume 10 people
        numberofHotdogsTotal = int(numberofHotdogs) * int(numberofPeople) # = 20 hot dogs needed
        numberofhotDogPacksNeeded = math.ceil(numberofHotdogsTotal / OnepackofHotdog) # = 2 packs of hot dogs needed
        print("\nMinimum number of packages of hot dogs required: ", math.ceil(numberofhotDogPacksNeeded))
       
    else:
        print("\nPlease enter a valid number of hotdogs")
    
    return numberofHotdogsTotal, numberofhotDogPacksNeeded, OnepackofHotdog
   

def getHotDogBunsNeeded(numberofHotdogsTotal, numberofPeople):
    OnepackofHotdogBuns = 8

#get number of hot dog bun packs needed
    numberofhotDogBunPacksNeeded = numberofHotdogsTotal/OnepackofHotdogBuns # = 2.5 packs of hot dog buns needed
    if numberofhotDogBunPacksNeeded % 1 != 0:
        numberofhotDogBunPacksNeeded = int(numberofhotDogBunPacksNeeded) + 1 

     
    print("\nMinimum number of packages of hot dog buns required: ", round(numberofhotDogBunPacksNeeded))

    return numberofhotDogBunPacksNeeded


def getLeftOverHotdogs(numberofHotdogsTotal, numberofhotDogPacksneeded, OnepackofHotdog):
    
    totalofHotDogsBought = numberofhotDogPacksneeded * OnepackofHotdog

    leftOverHotdogs = totalofHotDogsBought - numberofHotdogsTotal  # = 0 hot dogs left over

    print("\nLeft over hot dogs: ", leftOverHotdogs)
    
    return leftOverHotdogs

# 20 hot dogs needed
# 2 hotdogs per person


def getLeftOverHotdogBuns(numberofhotDogBunPacksNeeded, OnepackofHotdogBuns, numberofHotDogs):
    OnepackofHotdogBuns = 8 # 8 hot dog buns in a pack

    # numberofhotDogBunPacksNeeded = 2.5
    # numberofhotDogPacksNeeded = 2
    totalHotDogBuns = numberofhotDogBunPacksNeeded * OnepackofHotdogBuns # = 20 hot dog buns needed
    leftOverHotdogBuns = totalHotDogBuns - numberofHotDogs # = 4 hot dog buns left over
    print("\nLeft over hot dog buns: ", leftOverHotdogBuns)

    return leftOverHotdogBuns


def main():
    numberofPeople = getNumberOfPeople()
    numberofHotdogsTotal, numberofhotDogPacksNeeded, OnepackofHotdog = getNumberOfHotdogs(numberofPeople)
    numberofhotDogBunPacksNeeded = getHotDogBunsNeeded(numberofHotdogsTotal, numberofPeople)
    getLeftOverHotdogs(numberofHotdogsTotal, numberofhotDogPacksNeeded, OnepackofHotdog)

    
    OnepackofHotdogBuns = 8
    getLeftOverHotdogBuns ( numberofhotDogBunPacksNeeded, OnepackofHotdogBuns, numberofHotdogsTotal) 

    

if __name__ == "__main__":
    main()
    


"""
  Assuming: 10 people & 2 hotdogs per person

    if 10 people  then 2 packs of hotdogs for 2 hotdogs each
    10*2 = 20, 20 hotdogs/10 people = 2 hotdogs per person
    2 packs of hot dogs needed

    3 packages of hot dog buns needed
    3 pack of buns *8 = 24, 24-20 hot dogs = 2 hotdog buns per person

    left over hotdogs = 20 - 10*2 = 0
    left over hotdog buns = 24 - 10*2 = 4

"""
    



