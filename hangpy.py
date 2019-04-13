def defineWord():
    global word
    word = input("Please type a word to play: ")
    print("Your word is: " + word)
    confirmWord();
    return word

def confirmWord():
    confirm = input("Please confirm (y or n): ")
    if confirm == 'y':
        return setTurnsCount()
    if confirm == 'n':
        return defineWord()
    if confirm != 'y' and confirm != 'n':
        print("Invalid choice please enter a valid option. y for yes, n for no.")
        return confirmWord()
    print (confirm)
    return confirm

def setTurnsCount():
    global tries
    tries = input("How many tries would you like to give? ")
    print("Amount of tries: " + tries)
    return startGame()

def startGame():
    input("Ready? (y or n): ")

defineWord();
