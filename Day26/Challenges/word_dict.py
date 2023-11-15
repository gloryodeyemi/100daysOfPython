sentence = input()  # input = What is the Airspeed Velocity of an Unladen Swallow?
# 🚨 Don't change code above 👆
# Write your code below 👇
word_list = sentence.split()
# print(word_list)

result = {word: len(word) for word in word_list}
print(result)
