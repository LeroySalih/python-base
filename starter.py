def mySum(a, b):
    return a + b
    
if __name__ == "__main__":
    
    # Should output the first and last letter of the word entered by 
    # the user.
    word = input("Enter a word.")
    print("The first letter is {0}".format(word[0]))
    print("The last letter is {0}".format(word[-1:]))