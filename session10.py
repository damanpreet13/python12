"""
multi value containers
sequences
tuple
 list
 set
 string


dictionary
properties : 1 indexing
              2 negative indexing
              3 slicing
              4 concatenation
              5 multiplicity
              6 membership testing
               """
my_data= [10 , 20 , 30 ]

numbers = [
    [10,20 ,30 ],
    [10 , 20 , 30 , 40 , 50 , 60 ],
            [90 , 99],
         ]
# indexing
print(len(my_data))
print(my_data[1])
print(len(numbers))
print(numbers[1][2])
large_data = [
[
    [10 , 20 , 30 ],
    [10 , 20 , 30 , 40 , 50 , 60 ],
    [46 , 78 , 55 , 32],
],
[
    [10 , 20 , 30 ],
    [10 , 20 , 30 , 40 , 50 , 60 ],
    [46 , 78 , 55 , 32],  
]
]
print(large_data[1][2][3])
print(my_data[-1])
# negative indexing
print(large_data[-1][-3][-2])
# slicing
data = list(range(10,101,10))
print("Data:", data)
print("Data:[:5]", data[:5])
print("Data:[:4]", data[4:])
print("Data:[:2:6]", data[2:6])
print("Data:[:-5]", data[:-5])
print("Data:[-5:-2]", data[-5:-2])

# concatenation
data1 = [10,20,30]
data2 = [40,50,60]
data3 = data1 + data2
print("data3:", data3) 
#multiplicity
data4 = data1 * 3
print("Data:",data4)
# membership testing
print(10 in data1)
print(100 in data1)
print(1000 not in data1)

#dictionary
student = {
"Name":" Damanpreet singh",
"age":19,
"gender":"male",
"rollno": 1208,
"address":"ludhiana"
}
print(student["Name"])
print("rollno" in student)


# assignment    explore all the properties on string
# indexing
quote = "Search the candle rather than cursing the darkness" 
print("Quote:",quote)
print(len(quote))
print(quote[7])
print(quote[11])
# negative indexing
print(quote[-3])
print(quote[-15])
# slicing
print("Quote:",quote)
print("Quote:[:5]",quote[:5])
print("Quote:[5:]",quote[5:])
print("Quote:[2:10]",quote[2:10])
print("Quote:[-11:-5]",quote[-11:-5])
# concatenation
line1 = "search the candle rather "
line2 = "than cursing the darkness"
line3 = line1 + line2
print("Quote is:",line3)
# multiplicity
line4 = line1 * 5
print("after:",line4)
# membership testing
print("Search the candle rather than cursing the darkness" in quote )
print("rather than cursing the darkness" in quote )
print("Search" not in quote)
