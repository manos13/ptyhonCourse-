# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    alphabetCipher = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift] + string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]  
    alphabet = string.ascii_uppercase + string.ascii_lowercase 

    return {alphabet[index] : alphabetCipher[index]  for index in range(len(alphabet))}
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    copyText = list(text)
    for index in range(len(text)):
        for k,v in coder.iteritems():
            if text[index] == k:
                copyText[index] = v
                
    return "".join(copyText)
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    
    assert(shift >0 or shift < 26) ,"is not between 0 <= shift <26 got %d " % shift
    return applyCoder(text,buildCoder(shift))# Remove this comment when you code the function

#
# Problem 2: Decryption
#
import pdb; pdb.set_trace()
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    d = {n: 0 for n in range(25)}    
    shift = 0
    while True:
        newText = applyShift(text, shift)

        textList = newText.split(" ")
        count = 0 
        for word in textList:
            if isWord(wordList,word):
                count +=1 
        d[shift] = count
        if shift == 25:
            break
        shift += 1
    return max(d,key=d.get)

    """
    shift = 1
    while True: 
        try:
            newText = applyShift(text,26-shift)

            #newText = removePun(newText)
            textList = newText.split(" ")
            count = 0 
            #testCount = len(textList)
            for word in textList:
                #testWord = word in wordList
                if isWord(wordList,word):
                    count += 1
            if count == len(textList):
                break
            shift += 1   
        except AssertionError:
            return 0       
        if 26-shift == 25:
            return 0 

        return 26 -shift
    """
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    

    return applyShift(getStoryString(),findBestShift(wordList, getStoryString()))# Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    #s = applyShift('Hello, world!', 0)
    #print s
    #bestShift = findBestShift(wordList, s)
    #print bestShift
    #print applyShift(s,bestShift)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
