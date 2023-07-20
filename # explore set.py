# explore set in python
john_followers = {"fionna","sia","jack","joe","george"}
print("john followers:",john_followers)
print(type(john_followers))
numbers1 = list(range(10,101,10))
print("numbers is:", numbers1)
print(type(numbers1))
numbers1 = set(numbers1)
print("number now:",numbers1)
print("numbers type:",type(numbers1))
numbers1.add(10)
numbers1.add(110)
numbers1.add(20)
numbers1.add(220)
print("numbers after add:",numbers1)
numbers1.pop()
numbers1.pop()
print("numbers after pop:", numbers1)
numbers1.remove(50)
numbers1.discard(90)
print("numbers after remove & discard is:",numbers1)


john_followers = {"fionna","sia","jack","joe","george"}
jake_followers = {"anna","jack","leo","joe","harry","mike"}
fionna_followers = {"sia","joe"}
print("john followers:",john_followers )
print("jake followers:",jake_followers )
print("fionna followers:",fionna_followers )
followers = john_followers.intersection(jake_followers)
print("followers are:", followers)
followers = john_followers.intersection(jake_followers).intersection(fionna_followers)
print("followers are:", followers)
print("is subset:",fionna_followers.issubset(john_followers))
print("is superset:",john_followers.issuperset(fionna_followers))

# a,b,c,d,e,f,g
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = a-b
print("C is:",c)
d = a&b
print("D is:",d)
e = a^b
print("E is:",e)
f = a|b
print("F is:",f)
g = a.symmetric_difference(b)
print("G is:",g)