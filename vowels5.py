vowels = ['a','e','i','o','u']
word = input('provide a word to search for vowel:')

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter]+=1 
for k,v in found.items():
    print(k, 'was found', v, 'times')