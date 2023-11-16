text1 = input("Enter first text: ")
text2 = input("Enter second text: ")
text1 = "".join(sorted(text1.replace(" ", "").lower()))
text2 = "".join(sorted(text2.replace(" ", "").lower()))
if len(text1) > 1 and text1 == text2:
    print("Anagrams")
else:
    print("Not anagrams")
