from tkinter import *
import pandas
import random

BACKGROUND = "#B1DDC6"
current_card = {}
cards = {}

LANGUAGE_FONT = ("Arial", 40, "italic")
LANGUAGE_POS_X = 400
LANGUAGE_POS_Y = 150
WORD_FONT = ("Arial", 60, "bold")
WORD_POS_X = 400
WORD_POS_Y = 263

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    cards = original_data.to_dict(orient="records")
else:
    cards = data.to_dict(orient="records")


# ------------------------- GET NEXT CARD ----------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards)
    canvas.itemconfig(card_side, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=show_english)

# --------------------------- FLIP CARD ------------------------------- #
def show_english():
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

# -------------------------- UNKNOWN CARDS ---------------------------- #
def known_word():
    cards.remove(current_card)
    data = pandas.DataFrame(cards)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND)

flip_timer = window.after(3000, func=show_english)

canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_side = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(LANGUAGE_POS_X, LANGUAGE_POS_Y, font=LANGUAGE_FONT)
word = canvas.create_text(WORD_POS_X, WORD_POS_Y, font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
known_word_button = Button(image=correct, highlightthickness=0, command=known_word)
unknown_word_button = Button(image=wrong, highlightthickness=0, command=next_card)
known_word_button.grid(column=1, row=1)
unknown_word_button.grid(column=0, row=1)

next_card()

window.mainloop()
