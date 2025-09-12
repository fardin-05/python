#factorial & countdown 
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n * factorial(n-1)
def count(n):
    if n == 0:
        print('boom')
    else:
        print(n)
        count(n-1)
print("---menu---")
print('1.Calculate Factorial Number')
print("2.countdown Numbers")
choice = input("Enter Your Selection 1 or 2 :")
if choice == '1':
  n= int (input("Enter Your Number:"))
  print( n ,"the factorial is : ", factorial(n))
elif choice == '2':
  n = int(input("Enter Yor Number:"))
  count(n)
