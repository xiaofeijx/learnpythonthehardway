tabby_cat = "\tI'am tabbed in."
persian_cat = "I'am split\non a line."
backsalsh_cat = "I'am \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass\nkk
"""

print tabby_cat
print persian_cat
print backsalsh_cat
print fat_cat

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,