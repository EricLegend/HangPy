def defineWord():
    word = input("Please type a word to play: ")
    print("Your word is: " + word)
    confirmWord();
    return word

def confirmWord():
    confirm = input("\nPlease confirm (y or n)")
    if confirm == 'y':
        return gameStart()
    if confirm == 'n':
        return defineWord()
    if confirm != 'y' and confirm != 'n':
        print("Invalid choice please enter a valid option. y for yes, n for no.")
        return confirmWord()
    print (confirm)
    return confirm

defineWord();
