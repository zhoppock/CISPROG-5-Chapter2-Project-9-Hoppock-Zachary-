# We are going to calculate how many nautical miles are in a given number of kilometers:

# Input a number of kilometers
kilometersString = input("Input a distance in kilometers: ")
kilometers = int(kilometersString)

# Compute the number of degrees from the input number of kilometers using the formula:
# Degrees = kilometers / 111
degrees = kilometers/111

# Compute the number of nautical miles from the number of degrees using the formula:
# Nautical miles = Degrees * 60
nauticalMiles = degrees * 60

# Print the nautical miles
print("The kilmeter distance converted into nautical miles is " + str(nauticalMiles) + " nautical miles.")