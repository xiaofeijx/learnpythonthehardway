# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY state has:", cities['NY']
print "OR State has:", cities['OR']

# print some state
print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbre in states.items():
    print "%s is abbreviated %s" % (state, abbre)


# print every city in state
print '*' * 10
for abb, city in cities.items():
    print "%s has the city %s"% (abb, city)


# now do both at the same time
print '-' * 10
for aa, baba in states.items():
    print "%s state is abbreviated %s and has city %s" % (aa, baba, cities[baba])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Dose Not Exist')
print "The city for the state 'TX' is: %s" % city

