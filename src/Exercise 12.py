inp: str = input("Enter a sentence: ")

# Splits the string into words by whitespace. The first character is moved
# to the end and finally "ay" is appended. Every word is then concatenated into
# a space-delimited string.
out: str = " ".join(w[1:] + w[0] + "ay" for w in inp.split())

print(out)
