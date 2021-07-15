vowels = ["a", "e", "i", "o", "u"]
input_fr = input('Please write something here: ')
letters = input_fr.replace(" ", "")

def numberOfVowels(letters):
    v = []
    for i in letters:
        if i in vowels:
            v.append(i)
    vcount = len(v)
    return print(f"Vowels detected: {v}, there are {vcount}")

numberOfVowels(letters)

