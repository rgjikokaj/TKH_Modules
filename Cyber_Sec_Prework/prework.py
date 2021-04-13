#challenge 1

Name_enter = input("What is your name?")
print ("This is your first step " + Name_enter)


#challenge 2


over_under_list = [1,45,32,21,5,17,43,93]
for num in over_under_list:
 print (num)
if num > 25:
	print ("over")
else:
	print ("under")



#challenge 3
	names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
longest_string = max(names_list, key=len)
print(longest_string)

#Challenge 4
    
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
def names(names_list):
  return max(names_list, key=len)

big_name = names(names_list)
print(big_name)


#challenge 5

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]



def names_1(names_list):
  evenlist = []
  oddlist = []
  for name in names_list:
    if len(name) % 2 == 0:
      even_new_name = "b" + name[1:]
      evenlist.append(even_new_name)
    else:
      odd_new_name = name[:-1] + "c"
      oddlist.append(odd_new_name)

  print(evenlist)
  print(oddlist)
  return evenlist

new_names = names_1(names_list)
print(new_names)
	
