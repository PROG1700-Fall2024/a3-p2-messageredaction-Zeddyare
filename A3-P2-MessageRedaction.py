#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0433704
#Student Name: Zachary Rudolf

#variable initializing 
phrase = ""
letters = ""
def phraseInput():
    phrase = input("Type a phrase (or 'quit' to exit program): ")
    return phrase
#input letters to remove
def letterInput():
    letters = input("\nType a comma-separated list of letters to redact: ") 
    letters = letters.replace(",.-_: ", "")
    letters = letters.strip()  
    return letters 

#greeting/directions
def greeting():
    print("Welcome to the letter-slasher!\n")

def slashingProtocol():
    quit = False
    while quit == False: 
        phrase = phraseInput() 
        if phrase.lower() == "quit":
            quit = True
            print("\nThanks for slashing!") 
            break 
        letters = letterInput()
     #removal loop 
        for i in letters.upper(): 
            if i != "," and i != " ":
                phrase = phrase.replace(i,"_")
            else: 
                pass
        for i in letters.lower():
            if i != "," and i != " ":
                phrase = phrase.replace(i,"_")
            else: 
                pass
        removed = phrase.count("_")
        print(f"Number of letters redacted: {removed}")
        print(f"Redacted phrase: {phrase}\n") 

def MessageRedaction():
    # YOUR CODE STARTS HERE, each line must be indented (one tab) 
    #input phrase while loop
    
    #output of redacted letters

    #output of redacted phrase
    greeting()
    slashingProtocol()






    # YOUR CODE ENDS HERE

MessageRedaction() 