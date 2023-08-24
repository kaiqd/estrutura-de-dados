def checkVowels(s, v, c):
    if len(s) == 0: return v > c
    if s[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return checkVowels(s[1:], v+1, c)
    else:
        return checkVowels(s[1:], v, c+1)
    
print(checkVowels("Kaique", 0, 0))