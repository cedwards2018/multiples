
# Ask for user input
userNum = input("Tell me a number. ")

# Convert to float
userNum = float(userNum)

# Do the multiplying
for multiple in range(1,10):
	print("{} time {} is {}. ".format(userNum, multiple, userNum*multiple))