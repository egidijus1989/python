input = input("Parasykite nekoduota zodi...")
specialus_symboliai = "!@#$%^&*()-+?_=,<>/ "

def solve(text):
    n = ord('z') + ord('a')
    N = ord('Z') + ord('A')
    ans=[]
    for i in range(len(text)):
        if text[i].islower():
            mazoji = n - ord(text[i])
            ans.append(chr(mazoji))
        elif:
            didzioji = N - ord(text[i])
            ans.append(chr(didzioji))
        else:
            
    return   "".join(ans)
  
print(solve(input))