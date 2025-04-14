import random

text = "Das ist ein Beispieltext anhand dessen ich schauen kann was mit dem Text passiert wenn er durch meinen Blackout Poetry Generator gejagt wird."

with open("text.txt", "r", encoding="utf-8") as file:
    txt = file.read()

def blackout_poem(text, reveal_chance=0.1):
    words = text.split()
    output = []

    for word in words:
        if random.random() < reveal_chance:
            output.append(word)
        else:
            output.append("█" * len(word))
    
    return " ".join(output)

print(blackout_poem(txt))