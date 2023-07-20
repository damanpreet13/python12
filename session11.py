"""
MULTI VALUE CONTAINER 
   sequences
   tuple
   list
   set
   string
   
    dictioinary
    
    PROPERTIES:
    1 Indexing
    2 Negative indexing
    3 Slicing
    4 Concatenation
    5 Multiplicity
    6 Membership Testing
    """
    
my_data = [10, 20, 30]

numbers = [
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
]

print(len(my_data))
print(my_data[1])
print(len(numbers))
print(numbers[1][2])
large_data = [
[
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
],
[
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
]
]

print(large_data[1][2][1])
print(my_data[-1])
print(large_data[-2][-2][-4])
#Slicing
data = list(range(10,101, 10))
print("DATA:",data)
print("DATA:[:5]",data[:5])
print("DATA:[4:]",data[4:])
print("DATA:[2:6]",data[2:6])
print("DATA [:-5]",data[:-5])
print("DATA:[-5:-2]",data[-5:-2])


#concatenation
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print("DATA3:", data3)

#Multiplicity
data4 = data1 * 3
print("DATA 4 :", data4)

#Membership testing
print(10 is data1)
print(100 is data1)
print(1000 not in data1)