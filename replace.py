# create string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# replace "!" with " "
sentence = sentence.replace("!", " ")
# print string
print(sentence)
# capitalise string
sentence = sentence.upper()
# print string
print(sentence)
# define reverse function - uses slice to read variable backwards
def reverse(x):
    return x[::-1]
#apply reverse function to string 
sentence = reverse(sentence)
# print string
print(sentence)