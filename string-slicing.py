# slicing = create a substring by extacting the elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Shinji Ikari"

#[start:stop:step]
#first index is inclusive, last one is axclusive, so [0,6)
#equivalent to first_name = name[:6]
first_name = name[0:6]
print(first_name)

last_name = name[7:12]
print(last_name)

#step
#equivalent:  every_second_character = name[::2]
every_second_character = name[0:14:2]
print(every_second_character)

reversed_name = name[::-1]
print(reversed_name)

#slice
website1 = "https://google.com"
website2 = "https://wikipedia.com"
#(start,stop,step)
slice = slice(8, -4)
print(website1[slice])
print(website2[slice])