'''' Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary 
in a way that item from list1 is the key and item from list2 is the value'''
aainu = ['Teenie', 'Weenie', 'Tweenie']
bday = [17, 6, 2002,]

d = {}
for i in range(len(aainu)):
    d[aainu[i]] = bday[i]

print(d)


#question2
''' Merge two Python dictionaries into one
Below are the two dictionaries. Write a Python program to merge them into one dictionary'''
dict1 = {'Teenie': 17, 'Weenie': 6, 'Tweenie': 2002}
dict2 = {'Inu': 28, 'Mam': 10, 'Bebu': 98}
dict = {}
dict = dict1.copy()
dict.update(dict2)
print(dict)


#question3
'''Print the value of key ‘cuteness’ from the below dict
note: scores are out of 100'''
portfolio = {
    "class": {
        "student": {
            "name": "Aainu",
            "marks": {
                "hotness": 110,
                "cuteness": 120,
                "smartu"  : 1000000
            }
        }
    }
}

print(portfolio["class"]["student"]["marks"]["cuteness"])


#question4
'''Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting 
the mentioned keys from the below dictionary.
'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}
#Keys to extract
keys = ["name","goal", "city"]

dict = {}
for i in brewed.keys():
    if i in keys :
        dict[i] = brewed[i]
print(dict)        
print(type(brewed.keys()))
for i in keys:
    dict[i] = brewed[i]
print(dict)    


#question5
'''Delete a list of keys from a dictionary
Write a Python program to remove the mentioned keys from dictionary'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000000,
    "city": "kub's heart"}
# Keys to remove
keys = ["name","goal","salary"]

dict = {}
for i in keys:
    brewed.pop(i)

print(brewed)  

#question6
'''Write a Python program to check if value 200 exists in the following dictionary.'''
sample = {'a': 100, 'b': 200, 'c': 300}

k = False
for i in sample.values():
    if i == 200:
        k = True
    
print(k)    

if 200 in sample.values():
    print("yes")
else:
    print("no mtlb nahi ")    


#question7
'''Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}

brewed["location"] = brewed.pop("city")


print(brewed)


#question8
'''Change value of a key in a nested dictionary
Write a Python program to change pari’s salary to 8500 in the following dictionary.'''
saleh = {
    'emp1': {'name': 'charu', 'salary': 7500},
    'emp2': {'name': 'enu', 'salary': 8000},
    'emp3': {'name': 'pari', 'salary': 500}
}

saleh["emp3"]["salary"]=85000000
print(saleh)


#question9
'''Write a Python program to iterate over dictionaries using for loops.'''
brewed = {
    "name": "Bebu",
    "goal": "Buddh sa jeewan",
    "age": 20,
    "salary": 8000000,
    "city": "kub's heart"}

print((len(brewed)))


#question10
'''Print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys'''
d = {}
for i in range(1,18):
    d[i] = i * i

print(d)    

#question11
'''Write a Python program to sum all the items in a dictionary.
Write a Python program to multiply all the items in a dictionary.'''
dict = {'Teenie': 17, 'Weenie': 6, 'Tweenie': 2002}
c = 0
m = 1
for i in dict.keys():
    c = c + dict[i]
    m = m * dict[i]
print([c,m])

