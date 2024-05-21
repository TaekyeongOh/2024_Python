word=input('문자열을 입력하시오.')

length=len(word)

if length%2==1:
    half=length//2
else:
    half=(length+1)//2

word1 = word[0:half]
word2 = word[half:]

print(word2,word1)