# string  =input("Enter the string ")
# # list1 = []
# # for i in range(len(string)-1,-1,-1):
# #   list1.append(string[i])
# # print("".join(list1))

# reverse_string=""
# for char in range(len(string)-1,-1,-1):
#     reverse_string+=string[char]
# print("Reverse String",reverse_string )

def reverse(string):
    char=list(string)
    print("char",char)
    for k in range((len(string)//2)+1):
        char[k],char[len(char)-k-1] = char[len(char)-k-1], char[k]
    return "".join(char)

string="country"
print(reverse(string))    