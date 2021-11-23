# Question 16(a)
# Examination Number: your mom

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1.upper()) == sorted(word2.upper())):
    print(word1, 'is an anagram of', word2)
else:
    print(word1, 'is NOT an anagram of', word2)
    
if is_anagram(word1.upper(), word2.upper()) == True:
    print(word1, 'is an anagram of', word2)
else:
    print(word1, 'is NOT an anagram of', word2)
    
phrase = input('Enter a phrase: ')
nPhrase = phrase.replace(' ','')

if (sorted(word1.upper()) == sorted(nPhrase.upper())):
    print(word1, 'is an anagram of', phrase)
else:
    print(word1, 'is NOT an anagram of', phrase)
    
if (sorted(word2.upper()) == sorted(nPhrase.upper())):
    print(word2, 'is an anagram of', phrase)
else:
    print(word2, 'is NOT an anagram of', phrase)