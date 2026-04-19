# def main():

#     # Output using our own function
#     name = input("What's your name? ")
#     hello(name)

#     # Output without passing the expected arguments
#     hello()


# # Create our own function
# def hello(to="world"):
#     print("hello,", to)

# # This alone, however, will create an error of sorts. If we run python hello.py, nothing happens! The reason for this is that nothing in this code is actually calling the main function and bringing our program to life. To fix this, we can add the following code at the end of our file:

def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()