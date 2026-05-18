print("EchoBot ready! Type 'exit' to quit.")

while True:                           # loop runs forever
    user_input = input("You: ")        # take user input
    if user_input.lower() == "exit":   # check for exit condition
# .lower() converts the whole string to lowercase
        print("EchoBot: Goodbye!")     
        break                          # stop the loop
    else:
        print("EchoBot:", user_input)  # echo back the input
