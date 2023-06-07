# Function that returns the character in a position from the string
def CharAtPos(x:str,y:int):
    if y>len(x)-1:
        return
    return(x[y])

# Function that returns the vowels in the string - Case Insensitive
def ReturnVoewls(textString:str):
    
    vowelList=["a","e","i","o","u"]
    return [x for x in textString if x.lower() in vowelList]

# Test Code Here
print(CharAtPos("Sunday",4))
print(ReturnVoewls("April"))