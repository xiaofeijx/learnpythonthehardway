the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also can go through a mixed lists too
for i in change:
    print "I got %r" % i

# build a list

elements = range(0, 6)

# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     elements.append(i)


# now print it
for i in elements:
    print "Element was %d" % i


