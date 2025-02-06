# list datastructrctures
# lists are mutable
# lists are ordered
# lists are indexed
fruits = ['apple', 'banana', 'mangoes', 'pineapple', 'dragonfruit']
fruits[0]="Watermelon"
numbers = [1,2,3,4,5]
print(fruits)
numbers.append(6)
print(numbers)
print(f"I love eating {fruits[3]}")
numbers2 = [17,5,24,67,2,-7,0,13,1,5,-4]
numbers2.sort(reverse=True)
print(numbers2)

# tuple datastructure
# tuples are immutable(unchanged)
# tuples are ordered
# tuples are indexed
cars=('audi','mercedes','honda','toyota','BMW','suzuki')
print(cars)
nambari = (43,5,87,2,1,-3,-9,-100,-2345,9,0)
# nambari.sort(reverse=True)
print(sorted(nambari))
print(nambari)
print(f"I love {cars[3]}")

# set datastructure
# set are unordered
# set lack indexes
computers = {'dell','hp','lenovo', 'mac','ibm','acer','toshiba'}
computers.add('google')
computers.remove('lenovo')
print(computers)
num1={1,2,3,4,5}
num2={6,7,8,9,10}
union_set = num1.union(num2)
print(union_set)

# dictionaries datastructure
student={'Name':'Blaise', 'Age':17, 'Gender':'Male', 'School':'eMobilis'}
print(student['Name'])
print(f"Student name: {student['Name']}")
print(f"Student age: {student['Age']}")
print(f"Student gender: {student['Gender']}")
print(f"Student school: {student['School']}")