# dictionary = a changable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington, DC',
            'Ukraine':'Kyiv',
            'Poland':'Warsaw', 
            'Lithuania':'Vilnius'}
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

capitals.update({'Czechia':'Prague'})
capitals.update({'USA':'Las Vegas'})

capitals.pop('USA')
capitals.clear()

for key,value in capitals.items():
    print(key,value)


