text = input("Enter your String: ")
text = text.upper()
length_of_string = len(text)
reversed_string = text[::-1]

off_set = 0
for _ in range(length_of_string):
    print(text.ljust(length_of_string)+" "+reversed_string.rjust(length_of_string))
    text = text[:-1]
    reversed_string = reversed_string[1:]
    off_set+=1
