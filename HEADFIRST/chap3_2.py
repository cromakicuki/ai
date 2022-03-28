vowels = ['a','e','i','o','u'] # vowels 변수 리스트

word = input('Provive a word to search for vowels: ')

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k,'was found',v,'time(s).')