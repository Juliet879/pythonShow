# conditions
  # uses logical conditions from mathemaatics(== ,>= ,<= ,> ,< )
  # if the operation is true or false,do something
age = int(input('How old are ? '))

if age<=17:
    print('Too young for this!')
elif age<=26:
    print('You can apply!')
else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    print('Sorry,not qualified')


# list operations
student_data = ['Jennifer','Lovelace',24,True,'Kenya']
student_data.insert(1,'Maji')                            #Add an item to the list
student_data.pop(0)                                      #remove an item to the list
print(student_data)


# Tuples operations
    #Tuples are immutable,the items are accesible just as the lists
random = (54,'Africa',[2,5,4],'Blessed',(254,253,257))
print(random[1])                                       #access individual items in the collection
# print(random.pop(2))                                 #You cannot change the items in tuple object


# looping using comprehensions in list
student_age = [21,19,24,22,18,23,17]
year_birth = [2021-x for x in student_age]
print(year_birth)

# Dictionaries
   # Unordered collection of items in key:value formart inside curly brace separated by commas 
person = {'name':'Milka','age':25}
person['name'] = 'Dennis'                                       #change value 
print(person['name'])                                           #accessing the values
person.get('occupation',['teacher','farmer'])
print(person)
