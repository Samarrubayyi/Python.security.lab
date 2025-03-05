import random 


print( random.randint(1,100))

color= ['red' , ' gold' , 'blue ' , 'green']
print( random.choice(color))

print( random.random()) 

list=[1,2,3,4,5,6,7,8,9,10]   
random.shuffle(list)
print(list)