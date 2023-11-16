text1 = input("Enter first text: ")
text2 = input("Enter second text: ")
text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()
print(sorted(text1))
print(sorted(text2))
if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("Not anagrams")
