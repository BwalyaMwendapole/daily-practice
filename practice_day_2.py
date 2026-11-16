#practice_day_2

import random

Answers = ["yes", "maybe", "If you work hard", "Are oranges orange?", "NO"]

print("Magic 8 Ball - Ask me anything!")

while True:
    question = input('Ask your question (or type "exit" to quit): ')
    if question == "exit":
        print("Bye! 8 - Ball out.")
        break
    print("The Magic 8 - Ball says:" + random.choice(Answers))