import time #importing module for time delays

Loop=False



print("hello world")
for i in range(1,100,1):
    print(i)
Naam=input("Hello What is you name! ")
print("Hello", Naam)


daghoehetgaat=input("How is you doing today Good / Bad ")
if daghoehetgaat=="Good":
    print("That is very nice to hear!")
elif daghoehetgaat=="Bad":
    print("That is to bad ")
else :print("Sorry i do not understand.  Please repeat me!")
print("Choose between: It is raining. / There are some clouds. / It is sunny today")
Weatherquestion=input("What is the weather today? ")
if Weatherquestion=="It is raining.":
    print("CHoose between: A lot. / Just a little bit.")
    Rainquestion=input("How much? ")
    if Rainquestion=="A lot.":
        print("Than i am going to be wet!")
    elif Rainquestion=="Just a little bit.":
        print("Now that is just annoying!")
elif Weatherquestion=="There are some clouds.":
    Cloudquestion=print("It is probably windy than..")
elif Weatherquestion=="It is sunny today":
    print("Nice! Now i do not have to put on another pare of socks on...")
else :Loop
print("Sorry i do not understand. Please repeat me!")

while Loop==True:
    break

Myname=input("What do you think my name is? ")
print("That is correct. I am", Myname)
