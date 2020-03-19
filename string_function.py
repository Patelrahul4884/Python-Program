# capitalize()->Converts the first character to upper case
# s="hello world!"
# print(s.capitalize())

#casefold()->Converts string into lower case
# s="HELLO WORLD!"
# print(s.casefold())

#center()->Returns a centered string
# s="hello world"
# print(s.center(30,"'"))

#count()->Returns the number of times a specified value occurs in a string
# s="aaabbbccc ddd fff"
# print(s.count("d"))

#encode()->Returns an encoded version of the string
# s='python is not gäod programming language'
# print(s.encode(encoding='ascii',errors='backslashreplace'))

#endswith()	Returns true if the string ends with the specified value
# s="elon musk is the real world iron man"
# print(s.endswith("iron"))

#expandtabs()->Sets the tab size of the string
# s='t\te\ts\tl\ta'
# print(s.expandtabs(2))

#zfill()->Fills the string with a specified number of 0 values at the beginning
# s="spacex"
# print(s.zfill(10))

#translate()->translate the characters using ascii table
# s='elon musk'
# print(s.translate({109:116}))

#split()->Splits the string at the specified separator, and returns a list
# name="patel rahul rajubhai"
# print(name.split(" "))


#splitlines()->Splits the string at line breaks and returns a list
# s="python is the most popular programming language\nIt is easy as compared to other languages"
# print(s.splitlines())

#join()->Joins the elements of an iterable to the end of the string
# t=("rahul","patel")
# l=["rahul","patel"]
# name=['r','a','h','u','l']
# separator="-"
# print(separator.join(t))    #joining tuple with '-' seperator
# print(separator.join(l))    #joining list  with '-' seperator
# print("".join(name))        #Joining with empty seperator.

#lstrip()->Returns a left trim version of the string
# s="    rahul    "
# new=s.lstrip()
# print('patel',new,'rajubhai')

#replace()->Returns a string where a specified value is replaced with a specified value
# s="I like ISRO"
# print(s.replace("ISRO","SPACEX"))

#partition()->Returns a tuple where the string is parted into three parts
# s="player unknown battleground"
# print(s.partition("unknown"))

#format()->Formats specified values in a string
game="warface"
genre="fps"
print("{} is {} game.".format(game,genre))
