def check(str):
    str = str.lower()
    vowels = set ("aeiou")
    s = set({})

    for char in str:
        if char in vowels:
            s.add(char)
        else:
            pass    

    
    if len(s) == len(vowels):
        print("That is Vowels")

    else:
        print("That is Constants")    

if __name__ == "__main__":
    str = "SEEquoial"
    check(str)
