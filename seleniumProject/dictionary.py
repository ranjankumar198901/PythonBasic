# Dictionary

friends = {
    'tom' :'111-222-333',
    'jerry' :'33-22-11'
    
    }

print(friends['tom'])
#print(friends['abc'])

friends['bob']='888-666-777'

print(friends)  #{'tom': '111-222-333', 'jerry': '33-22-11', 'bob': '888-666-777'}

    #Delete item from dictionary
del friends['bob']
print(friends)

for key in friends:
    print(key,":",friends[key])

print(len(friends))  # 2

    # in and not in 
print('tom' in friends)
print('bob' not in friends)

print("hi")
    #Equality test (== and !=)
d1 = {'nike':41,'bob':33}
d2 = {'bob':3 ,'nike':41}
print(d1==d2)
print(d1!=d2)

    #dictionary Methods
#friends.popitem()   # randomly select an item and delete it 
print(friends)

#friends.clear()    # clear all the items from the dictionary
print(friends)

print(friends.keys())   # return all the keys from the dictionary
print(friends.values()) # returns all the values from the dictionary
    
print(friends.get('tom',"Not Exist"))

print(friends.pop('tom'))
print(friends)

