my_name = "Rick"
print(my_name[0])


list1 = [5, 10, 15, 20, 25, 50, 20]
if not 20 in list1:
    print("20 not in list")
else:
    index = list1.index(20)
list1[index] = 200

print(list1)

cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]
print(cities[:-1])

usernum = input("Enter your Number")

num = 12

for i in range(1, 13):
   print(num, 'x', i, '=', num*i);

current_number = 1 
while current_number <= 10:    
    print(current_number)   
    current_number += 1

print("Finished")

list1 = [5, 10, 15, 20, 25, 50, 20]

desired_item = 20
index = len(list1) - 1

while index >= 0:
	if list1[index] == desired_item:
		break

	index -= 1

print(f"the index of the last item is {index}")
for i in range(len(list1) - 1, -1, -1):
    	if list1[i] == desired_item:
         break

print(f"the index of the last item is {index}")


sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class'],['student'],['history'])
