from tkinter import *
from random import randint
import pandas as pd

root = Tk()
root.title("Words Challenge")
root.geometry("500x400")

words = pd.read_excel("C:/Users/jamie/Desktop/NTUIB13/Flashcard/Level_1.xlsx")
words = words.to_numpy().tolist()
words = [tuple(elt) for elt in words]

# get a count of word list
count = len(words)

def pas(self):
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0,END)
    hint_label.config(text="")
    # Reset Hint Stuff
    hinter = ""
    hint_count = 0

    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    #update label with vocabulary
    vocabulary.config(text=words[random_word][1])


def answer(self):
    global random_word
    if my_entry.get() == words[random_word][0]:
        global hinter, hint_count
        # Clear the screen
        answer_label.config(text="")
        my_entry.delete(0, END)
        hint_label.config(text="")
        # Reset Hint Stuff
        hinter = ""
        hint_count = 0
        # Create random selection
        random_word = randint(0, count - 1)
        # update label with vocabulary
        vocabulary.config(text=words[random_word][1])
    else:
        answer_label.config(text="Incorrect!")

#Keep Track Of the Hints
hinter = ""
hint_count = 0
def hint(self):
    global hint_count, hinter
    if hint_count < len(words[random_word][0]):
        hinter = hinter + words[random_word][0][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


# Labels
vocabulary = Label(root, text="", font=("微軟正黑體",20))
vocabulary.pack(pady=50)

answer_label = Label(root, text="", font=("Arial", 12))
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Arial", 15))
my_entry.pack(pady=20)

# Create Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)
root.bind("<Return>", answer)

pass_button = Button(button_frame, text="Pass", command=pas)
pass_button.grid(row=0, column=1)
root.bind("<Escape>", pas)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=20)
root.bind("<Right>", hint)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Give the First Random Word
random_word = randint(0, count - 1)
vocabulary.config(text=words[random_word][1])

root.mainloop()
