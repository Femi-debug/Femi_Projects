sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
new_sentence = sentence.replace("!", " ")
print(new_sentence) # Output: The quick brown fox jumps over the lazy dog.
cap_sentence = new_sentence.upper()
print(cap_sentence) # Output: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
print(new_sentence[::-1]) # Output: reverse of The quick brown fox jumps over the lazy dog.