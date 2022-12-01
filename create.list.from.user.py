#Write a Python script to create a list of city names taken from the user.
x=int(input("how many city names"))
n=[]
for i in range(0,x):
    city=input("Enter city name -{} " .format(i+1))
    n.append(city)
print(n)