# word = "bottles"

# for beer_num in range(10, 0, -1):
#     print(beer_num, word, "of beer on the wall")

#     if beer_num == 1:
#         print("No more bottles of beer on the wall")
#     else:
#         new_num = beer_num - 1
#         if new_num == 1:
#             word = "bottle"
#         print(new_num, word, " of beer on the wall")
# print()

# vowels = ['a','e','i','o','u']
# word = input('write a word: ')
# found = []

# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for _ in found:
#     print(_) 

# def main():
#     x = get_int()
#     print(f"x is : {x}")

# def get_int():
    
#     while True:
#         try:
#             x = int(input("input a number: "))
#         except ValueError:
#             print("X is not a number")
#         else:
#             break
#     return x

# main()

# phrase = "don't panic!"

# plist = list(phrase)


# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)


# phrase = "Don't panic!"
# plist = list(phrase)

# new_phrase = ''.join(plist[1:3])

# print(phrase) 
# print(plist)
# print(new_phrase)

# paranoid_android = "Marvin"
# letters = list(paranoid_android)
# for char in letters:
#  print('\t'*2, char)




# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = {}
# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter, 0)
#         found[letter] += 1
# for k, v in sorted(found.items()):
#  print(k, 'was found', v, 'time(s).')


# a = ()
# print(not a)



