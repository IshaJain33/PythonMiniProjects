import time

text = "The quick brown fox jumps over the lazy dog"
print("Type this:", text)
input("Press Enter when ready...")

start_time = time.time()
user_input = input("Start typing: ")
end_time = time.time()

words_per_minute = len(user_input.split()) / ((end_time - start_time) / 60)
accuracy = len(set(user_input.split()) & set(text.split())) / len(text.split()) * 100

print(f"Speed: {words_per_minute:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")

