def count_vowels(text):
    vowels = "aeiouAEIOU"
    text.lower()
    vowels_count = {}
    for char in text:
        if char in vowels:
            if char in vowels_count:
                vowels_count[char] += 1
            else:
                vowels_count[char] = 1
    return vowels_count

input_text = input("Please enter a text: ")
result = count_vowels(input_text)
print("Vowel count:", result)