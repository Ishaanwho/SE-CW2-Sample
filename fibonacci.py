current=1
previous=0
next=0
list1 = []
    
for i in range(1,11): 
   previous = current
   current = next
   next = current + previous
   list1.append(current)
print(list1)



   
   


