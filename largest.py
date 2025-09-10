
a = [1,2,3,4,5,6]
#first Largest int Number 
largest =  int ()  # শুরুতে negative infinity
second=largest
for i in a:
    if i > largest :
        largest = i
print("first largest number:", largest )

#second largest int number 
for i in a :
    if i>second  and i != largest:
        second =i 
print("second largest number:", second)
