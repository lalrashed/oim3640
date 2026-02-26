# count = 0
# for letter in 'mississippi':
#     if letter == 's':
#         count += 1
# print(count)

# n = 6
# while n != 0:
#     print(n)
#     n = n - 2
# #will be negative
# n = 5
# while n != 0:
#     print(n)
#     n = n - 2

def uses_any(word, letters):
    for letter in word:
        if letter in letters:
            return True
        else return False

print(uses_any('hello','aeiou'))

