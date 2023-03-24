# Just a Note
# This application is supposed to create a file called words_to_learn.csv after the green check button is clicked
# A word only gets removed from the original list if the check mark is clicked after the card is flipped.
# If it is clicked before the card is flipped , the entry remains
# This is intended funtionality.

from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# -------------------LOGIC-----------------#


#-----------------------------------Determining which file gets opened. See alternative code below-------------------#
filename = "data/words_to_learn.csv"
if os.path.isfile(filename): #check for existence of words_to_learn.csv and set it as our source of words if it exists
    french_words_df = pd.read_csv("data/words_to_learn.csv")
    to_learn = french_words_df.to_dict(orient='records')
else: #if words_to_learn.csv doesn't exist, set our source of words to french_words.csv
    french_words_df = pd.read_csv("data/french_words.csv")
    to_learn = french_words_df.to_dict(orient='records')

#--------------- alternative code to determine what file gets opened  ----------------------#
# try:  #test for existence of words_to_learn.csv
#     with open("data/words_to_learn.csv", 'r') as file:
#         file.read()
# except FileNotFoundError: #if words_to_learn.csv does not exist, our source of words will be french_words.csv
#     french_words_df = pd.read_csv("data/french_words.csv")
#     to_learn = french_words_df.to_dict(orient='records')
# else: #if words_to_learn.csv exists, it will be our source of words
#     french_words_df = pd.read_csv("data/words_to_learn.csv")
#     to_learn = french_words_df.to_dict(orient='records')


# to_learn is a list of dictionaries with format [{'French': 'sample word', 'English': 'sample word'}, {'French': 'sample word', 'English': 'sample word'}]
print(to_learn)

def next_card():
    global random_french_word
    random_french_word = random.choice(to_learn)["French"]
    canvas.itemconfig(canv_title, text="French", fill="black")
    canvas.itemconfig(canv_word, text=random_french_word, fill="black")
    canvas.itemconfig(canv_image, image=front_card_image)


def flip():
    for word_dict in to_learn: #word_dict is a dictionary with structure {'French': 'sample word', 'English': 'sample word'}
        if word_dict["French"] == random_french_word:
            global known_card #known_card is a dictionary with format {'French': 'sample word', 'English': 'sample word'}
            known_card = word_dict  #assigning the word dict to a global variable so it can be removed from the list if the known button is clicked.
            english_translation = word_dict['English']
            print(word_dict["English"])
            canvas.itemconfig(canv_image, image=back_card_image)
            canvas.itemconfig(canv_title, text="English", fill="white")
            canvas.itemconfig(canv_word, text=english_translation, fill="white")




def know():
    next_card()
    window.after(1500, flip)
    to_learn.remove(known_card)
    print(to_learn)

    words_to_learn_df = pd.DataFrame(to_learn)
    words_to_learn_df.to_csv('data/words_to_learn.csv', index=False)
    print(words_to_learn_df)


def don_t_know():
    next_card()
    window.after(1500, flip)


# ----------------------------------UI----------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---- images-------#
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canv_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
canv_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canv_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

unknown_button = Button(image=cross_image, highlightthickness=0, command=don_t_know)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0, command=know)
known_button.grid(row=1, column=1)

next_card()
window.after(2000, flip)


window.mainloop()
