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
    for i in ",.-_: ":
        letters = letters.replace(i,"") #used GPT to find out why replace was not working here. Needed to create a way to allow it to select all desired characters 
    letters = letters.strip()  
    return letters      #watching this work finally was beautiful 

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
                pass        #this was the only way I could figure out how to get it to work if there was any commas in the phrase OR any spaces in the phrase EDIT: redundant now, leaving it in for that sake 
        removed = phrase.count("_")
        print(f"Number of letters redacted: {removed}")
        print(f"Redacted phrase: {phrase}\n") 

def MessageRedaction():
    # YOUR CODE STARTS HERE, each line must be indented (one tab) 
    #input phrase while loop

    #output of redacted phrase
    greeting()
    slashingProtocol()
    # YOUR CODE ENDS HERE

MessageRedaction() 