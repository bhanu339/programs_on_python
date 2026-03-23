def is_anagram(s,t):
    return sorted(s)==sorted(t)
s=input('enter first string:')
t=input('enter second string:')
if is_anagram(s,t):
    print('valid anagram')
else:
    print('not valid anagram')    