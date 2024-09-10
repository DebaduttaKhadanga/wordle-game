from random import randint

words = ["basis", "buyer", "bread", "pizza", "owner", "cheek", "woman", "tooth", "apple", "entry", "drama", "steak", "river", "hotel", "union", "thing", "salad", "shirt", "event", "honey"] 

def generateRandom(words: list):
    n = randint(0, len(words)-1)
    return words[n]

word = generateRandom(words)
# print(word)
iterations = 0

while True:
    inp = input("Enter your guess! : ")
    opt = ""
    if(len(inp)!=len(word)):
        print("Your guess is too long!")
        continue
    if(word == inp):
        iterations += 1
        print(f"Congrats! You guessed the word! It took you {iterations} tries!")
        break
    else:
        lst1 = list(word)
        lst2 = list(inp)
        for i in range(len(word)):
            if(lst1[i]==lst2[i]):
                opt += f"{lst1[i]} "
            else:
                opt += "_ "
        print(opt)
        iterations+=1
    if(iterations==5):
        print(f"You ran out of tries! The word was \"{word}\"!")
        break

