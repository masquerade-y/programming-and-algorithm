"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
Beijing (China, Asia)

Print the following (using "print"):
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""



locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Asia']['China'].append('Beijing')
locations['Africa'] = {'Egypt': ['Cairo']}

print 1
sorted_loc = sorted(locations['North America']['USA'])
for city in sorted_loc:
    print city

print 2
asia = [(city +  " - " + country) for country, cities in locations['Asia'].items() for city in cities]
for city in sorted(asia):
    print city

# Note that here double loop list comprehension is used. Pay attention to the sequence of the nested for loop.
