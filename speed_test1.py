import random
import time
from tkinter import *

def start_typing():
    sentence = random.choice(sentences)
    sentence_label.config(text=sentence)
    input_text.config(state=NORMAL)
    input_text.delete("1.0", END)
    input_text.focus()
    start_button.config(state=DISABLED)
    global start_time
    start_time = time.time()

def end_typing():
    end_time = time.time()
    input_text.config(state=DISABLED)
    elapsed_time = end_time - start_time
    typed_text = input_text.get("1.0", END).strip()
    accuracy = calculate_accuracy(sentence_label.cget("text"), typed_text)
    wpm = calculate_wpm(typed_text, elapsed_time)
    result = f"Time: {elapsed_time:.2f} seconds\nAccuracy: {accuracy:.2f}%\nWPM: {wpm:.2f}"
    result_label.config(text=result)
    start_button.config(state=NORMAL)

def calculate_accuracy(expected, actual):
    correct_count = sum(1 for e, a in zip(expected, actual) if e == a)
    accuracy = (correct_count / len(expected)) * 100
    return accuracy

def calculate_wpm(text, elapsed_time):
    words = len(text.split())
    wpm = (words / elapsed_time) * 60
    return wpm

# Sample sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Learning to code is fun and rewarding.",
    "Practice makes perfect in typing speed."
]

# Create the GUI
window = Tk()
window.title("Speed Typing Test")

sentence_label = Label(window, text="", font=("Arial", 24))
sentence_label.pack()

input_text = Text(window, height=5, width=50, state=DISABLED)
input_text.pack()

start_button = Button(window, text="Start Typing", command=start_typing)
start_button.pack()

result_label = Label(window, text="", font=("Arial", 24, "bold"))
result_label.pack()

end_button = Button(window, text="End Typing", command=end_typing)
end_button.pack()

window.mainloop()
