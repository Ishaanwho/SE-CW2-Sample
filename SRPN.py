stack1=[]

def process_command(i):
 
 if i not in '^/*+-=%d':

   if int(i) > 2147483647:
    stack1.append(2147483647)
   elif int(i) < -2147483648:
    stack1.append(-2147483648)
   else:
    stack1.append(int(i))
        
 elif i == '=':
  if len(stack1) == 0:
   print('Stack Underflow')
  else:
   print(stack1[-1])
   
 elif i == 'd': 
  if len(stack1) == 0:
   print('Stack Underflow')
  else:
   for i in stack1:
    print(int(i))
      
 else: 
  if len(stack1)>1:
    y= stack1.pop()
    x= stack1.pop()
        
    if i == '/': 
     if y==0:
       print('Divide by 0.')
     elif (x//y) > 2147483647:
      stack1.append(2147483647)
     else:
      stack1.append(x//y)
      

       
    elif i == '*':
     if (x*y) > 2147483647:
        stack1.append(2147483647)
     else:
        stack1.append(x*y)
    
    elif i == '+':
      if (x+y) > 2147483647:
        stack1.append(2147483647)
      else:
        stack1.append(x+y)
      
      
    elif i == '-':
      if (x-y) < -2147483648:
        stack1.append(-2147483648)
      elif (x-y) > 2147483647:
         stack1.append(2147483647)
      else:
        stack1.append(x-y)
    
  
    elif i == '^':
     if y < 0:
       print("Negative power.")
       stack1.append(x)
       stack1.append(y)
     
     else:
       if x**y > 2147483647:
        stack1.append(2147483647)
       else:
        stack1.append(int(x**y))
    
    
    elif i == '%':
     stack1.append(x%y)
    else:
     print("Invalid input")  
  
  else: 
     print('Stack underflow.')
 
           

      
    
        


#This is the entry point for the program.
#It is suggested that you do not edit the below,
#to ensure your code runs with the marking script
if __name__ == "__main__": 
  while True:
    try:
      cmd = input()
      pc = process_command(cmd)
    except EOFError: 
      exit()
