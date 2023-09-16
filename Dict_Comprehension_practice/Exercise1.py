sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# split_sentence = sentence.split()

# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}
print(result)
