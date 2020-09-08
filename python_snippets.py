
##WHILE WITH BREAK
i=0
while i < 6:
    print (i)
    if i==3:
        break
    i += 1

##WHILE WITH CONTINUE
i=0
while i < 6:
    i += 1
    if i==3:
        continue
    print (i)
print (i)
    


##FUNCTION WITH UNKNOWN ARGUMENTS
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


##FUNCTION WITH UNKNOWN VALUES
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


##FUNCTION WITH DEFAULTS
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


##FUNCTION WITH FOR LOOP
def my_function(food):
  for x in food:
    print ("Connected to ")  
    print(x)

fruits = ["10.10.10.10", "11.11.11.11", "100.100.100.100"]

my_function(fruits)