#Exercise XP
#Ex1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict1 = dict(zip(keys, values))
print(dict1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict2={}
for i,y in zip(keys, values):
     dict2[y] = i
print(dict2)

#Ex2
total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for people in family.keys():
     if 3<= family[people] <=12:
         total += 10
     elif family[people] > 12:
         total+=15
     else:
         pass
print(total)


names=[]
ages=[]
dict1={}
total= 0

name = input("Enter the name (type done if you're done): ")
while name !="done":

     age = input(f'Enter {name}s age: ')
     names.append(name)
     ages.append(age)
     name = input("Enter the next name: ")
print(ages)
print(names)


for people in dict1.keys():
     if 3<= int(dict1[people]) <=12:
         total += 10
     elif int((dict1[people])) > 12:
         total+=15
     else:
         pass
print(f'Total: ${total}')



#Ex2
list_name = []

list_age = []

while True:

    name = str(input("Please enter your name! (type quit when done)?"))

    list_name.append(name)

    age = str(input("Please enter your age! (type quit when done)?"))

    list_age.append(age)

    if name and age == 'quit':

        break



list_name.remove("quit")

list_age.remove("quit")

new_age_list = list(map(int, list_age))

family = dict(zip(list_name, new_age_list))

print(family)

cost = 0



for name, age in family.items():

   

    if age < 3:

        print(name + " ticket is free")

    elif age < 12:

        print(name + " ticket is $10")

        cost = cost + 10

    else:

        print(name + " ticket is $15")

        cost = cost + 15

 

print("Your total cost is $", cost)

#EX3
brand = {
     'name': 'Zara',
     'creation_date': '1975',
     'creator_name': 'Amancio Ortega Gaona',
     'type_of_clothes': ['men', 'women', 'children', 'home'],
     'international_competitors': ['Gap', 'H&M', 'Benetton'],
     'number_stores': 7000,
     'major_color':
     {'France': 'blue',
      'Spain': 'red',
      'US': ['pink', 'green']},

}

brand['number_stores'] = 2
print(brand)


client = brand['type_of_clothes']
print(f"Zaras clients are {', '.join(client)}")


brand['country_creation'] = 'Spain'
print(brand)


print("The key exists")
(brand['international_competitors']).append("Desigual")


del brand['creation_date']


print(brand['international_competitors'][-1])
print(brand['international_competitors'])

 
print(brand['major_color']['US'])


print(len(brand))


print(brand.keys())



more_on_zara = {
     "creation_date": 1975, 
     "number_stores": 10000,
}


brand.update(more_on_zara)
print(brand ['number_stores'])


#Ex4

disney_users_A={}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for count, value in enumerate(users):
     if ("i" in value) == False:
         disney_users_A[value]=count
         print("works")
     else: continue
print(disney_users_A)


disney_users_A={}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for count, value in enumerate(users):
     if ((value.startswith("M")) or (value.startswith("P")))==0:
         disney_users_A[value]=count

    
print(disney_users_A)

#EX GOLD
birthdays = {
     'James':'2000/05/13',
     'Harry':'1994/11/13',
     'Herbert': '1986/08/09',
     'Greg': '1909/03/28',
     'Zack': '1854/12/12'
}

print('Welcome, you can look up the birthdays of the people in the list')

user_input = input('Please enter the name: ')

birthday = birthdays[user_input]

print(f'{user_input}s birthday is: {birthday}')

#EX2

birthdays = {
     'James':'2000/05/13',
     'Harry':'1994/11/13',
     'Herbert': '1986/08/09',
     'Greg': '1909/03/28',
     'Zack': '1854/12/12'
}
print('Welcome, you can look up the birthdays of the people in the list')
for i in birthdays:
     print(i)
user_input = input('Please enter the name: ')

if user_input in birthdays:
     print(f'{user_input}s birthday is: {birthdays[user_input]}')
else: print(f'Sorry, we don’t have the birthday information for {user_input}')

#EX3

birthdays = {
     'James':'2000/05/13',
     'Harry':'1994/11/13',
     'Herbert': '1986/08/09',
     'Greg': '1909/03/28',
     'Zack': '1854/12/12'
 }


new_name = input('Enter a new name: ')
new_birthday = input(f'Enter {new_name}s birthday YYYY/MM/DD: ')
birthdays[new_name]=new_birthday
print('Welcome, you can look up the birthdays of the people in the list')
for i in birthdays:
     print(i)
user_input = input('Please enter the name: ')

if user_input in birthdays:
     print(f'{user_input}s birthday is: {birthdays[user_input]}')
else: print(f'Sorry, we don’t have the birthday information for {user_input}')

#Ex4----

items = {"banana": 4,
     "apple": 2,
     "orange": 1.5,
     "pear": 3}

for i in items:
     print (f'The price of a {i} is ${items[i]}')



items = {("banana", 4): 2,
     ("apple", 2): 4,
     ("orange", 1.5): 2,
     ("pear", 3): 1}


total = 0
for i in items:
     cost = i[1]*items[i]
     print(cost)
     total += cost
print(total)

# EXERCISE NINJA
string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"


li = string.split(",")

print(len(li))


li.sort(reverse= True)
print (li)


counter = 0 
for i in li:
     if 'o' in i:
         counter += 1
print(counter)


counter = 0 
for i in li:
     if 'i' in i == False:
         counter +=1
print(counter)


li_2 = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]


li_2_set = set(li_2)


counter = 0
print(f'There are {len(li_2)} companies in the list of {",".join(li_2_set)}.')


li_2.sort()

final = []
for i in li_2:
     word = i[::-1]
     word = "".join(word)
     final.append(word)
print(final)






#Time Challenge- perfect NUm
user_num = int(input("Enter a number to see if it perfect: "))
divisable = []

for i in range(1,user_num):
     if (user_num % i == 2):
         divisable.append(i)
if sum(divisable) == user_num:
     print("True")
else: print("False") 

#Time Challenge 2
sentance = input("Enter a sentance: ")

sen_li = sentance.split()
sen_li.reverse()

rev_sen =" ".join(sen_li)
print(rev_sen)


# Daily Challenge: Dictionaries
# Challenge 1
word = input("Enter a word : ")
import re
pattern = re.compile(r"(^[a-zA-Z]+$)+")
cond = pattern.fullmatch(word)
if cond ==None:
    print("Enter a word")
else :

      list = {}
      fin=len(word)
      for i in range(0,fin) :
              if word[i] in list :
                  list[word[i]].append(i)
              else :
                  list[word[i]]=[i]
      print(list)
      
      
#DC2
items_purchase = {
   "Apple": "$4",
   "Honey": "$3",
   "Fan": "$14",
   "Bananas": "$4",
   "Pan": "$100",
   "Spoon": "$2"
 }

wallet = "$100" 

sorted= items_purchase
print(sorted)
buy =[]
for i in sorted:
    if(int(sorted[i][1:]) <= int(wallet[1:])):
          buy.append(i)
if buy == []:
    print("Nothing")
else : 
    print(buy)

def higest_even(li):
    evens = []
    for sorted in li:
         if sorted % 2 == 0:
              evens.append(sorted)
         return max(evens)
print(higest_even([4,5,7,9,9,9,9,9,9,9,9]))
def super_func(*args, **kwargs):
   total = 0
   for items in kwargs.values():
    total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

