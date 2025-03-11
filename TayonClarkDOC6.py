def UserInput():
    str1 = input("Enter first string")
    str2 = input("Enter second string")
    return str1, str2

def uncommonConcat(str1, str2):
    s1 = set(str1)
    s2 = set(str2)

    FindCommonChar = s1 & s2
    FindUncommonChar1 = s1 - FindCommonChar
    FindUncommonChar2 = s2 - FindCommonChar

    result = "".join(FindUncommonChar1) + "".join(FindUncommonChar2)

    return result

if __name__=="__main__":
    str1, str2 = UserInput()
    result = uncommonConcat(str1, str2,)
    print(result)



