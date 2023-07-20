# explore dictionary in python
my_data = {101:"john",201:"fionna",301:"george", 661:"harry"}
print("my_data")
print (my_data)
print("min:",min(my_data))
print("max:",max(my_data))
print("sum:",sum(my_data))
print(my_data[201])
print(my_data.get(201))
my_data.pop(201)      #delete operation
print(my_data)
my_data[775]="leo"   #insert operation
print(my_data)
my_data[775]="kim"      #updtate operation
print(my_data)
del my_data[775]
print(my_data)

# example
columns =["ludhiana","ferozpur","moga","jalandhar","bathinda"]
population ={}.fromkeys (columns,1200)
print("population",population)
population["ferozpur"]=3100
#convert dictionary into list of tuples
items = list(population.items())
print("items")
print(items)
