import random 
import datetime 

operations_to_resolve = 10000

operations_done = 0 

x1 = datetime.datetime.now()

while operations_done != operations_to_resolve:
    random.randint(1, 1000)
    operations_done += 1 
    
x2 = datetime.datetime.now()


print("Starting time" + x1)
print("Seconds it took to perform the operations:")
print(x2 - x1)
print("") 
print("Number of operations it made:" + operations_to_resolve)
