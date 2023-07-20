"""
for each or enhanced for loop
"""
data = list(range(10,101,10))
print(data)
"""for idx in range(len(data)):
    print(data[idx])
"""
for element in data:
  print(element)
  # enhanced for loop will work on set , list , tuple....
  data = set(data)
  for element in data:
    print(element)

    student = {
         "roll no": "1208",
         "name":"damanpreet singh",
         "age":  19,
    }
print("dictionary data....")
items = student.items()
for item in items:
#print(items)
 print(item[0],item[1])
 # dictionary keys
 print("dictionary data....")
 keys = student.keys()
 for key in keys:
   print(key)
   #print dictinary keys and values
 print("dictionary keys&values....")
for keys in student:
    print(key, student[key])


