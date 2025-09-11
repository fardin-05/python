# use function to check largest number 
def largest (a,b,c):
    if a>=b and a>=c : #return max(a, b, c)
        return a 
    elif b>=a and b>=c :
        return b 
    elif c>=a and c>=b  :
        return c
    else :
       return 'Invalid (please enter intiger number ! )'
        
#calculation 
def calculation (a,b,c,d):
    try :
       if d=='+':
        return a+b+c
       elif d=="-":
        return a-b-c
       elif d=='*':
        return a*b*c 
       elif d=='/':
        return a/b/c 
       else :
        return 'Invalid operator'
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"   
    
#selection 
print('----menu----')
print('1.check largest Number ')
print('2.calculation(+ - * /)')
print('3.both')
choice = input(' Please  Select Your Choice 1,2 or 3 :') 

#condition 
try :
   if choice == '1' :
      a=int(input("Enter Your First number : "))
      b=int(input("Enter Your Second number : "))
      c=int(input("Enter Your Third number : ")) 
      print (" largest number is : " , largest(a,b,c))
       
   elif choice == '2' :
    print('\'avoid divide by zero (ZeroDivisionError:division by zero )\'')
    a=int(input("Enter Your First number : "))
    b=int(input("Enter Your Second number : "))
    c=int(input("Enter Your Third number : ")) 
    d=input("Enter Your Operator (+ - * /):")
    print ("The total is : " , calculation(a,b,c,d))

   elif choice =='3':
    a=int(input("Enter Your First number : "))
    b=int(input("Enter Your Second number : "))
    c=int(input("Enter Your Third number : ")) 
    d=input("Enter Your Operator (+ - * /):")
    print (" largest number is : " , largest(a,b,c))
    print ("The total is : " , calculation(a,b,c,d))

   else :
    print("incorrect Your Selection ")
except ValueError:
    print("Error: Please enter valid integer numbers!")




