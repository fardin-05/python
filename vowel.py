a=input("Enter Your Alphabet:")
vowel=[]
for i in a :
    if i.lower() in ['a','e','i','o','u'] :
        if i.lower() not in vowel:
            vowel.append(i.lower())
if vowel:
        print('the vowel is :', vowel )
else:
        print('this is constant')



