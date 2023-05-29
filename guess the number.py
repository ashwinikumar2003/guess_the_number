from tkinter import *
import random

# taking a random value from 1 to 100
t = random.randint(1, 101)

class Screen:

    # creating constructor for screen class
    def __init__(self):
        self.win = Tk()
        self.count = 5
        self.win.title("Number guessing game")
        self.win.geometry("400x400")
        self.win.resizable(width=False, height=False)

        # creating different labels for the game
        self.lbl1 = Label(self.win, text="Number guessing game", font=("harrington", 25, "bold"), justify="center", fg="Blue")
        self.lbl1.pack()

        self.lbl2 = Label(self.win, text="Enter a positive number from 1 to 100", pady=15)
        self.lbl2.pack()

        self.entry = Entry(self.win, width=15, borderwidth=2)
        self.entry.pack(pady=10)

        self.lbl3 = Label(self.win, text="You have {} trial(s) left".format(self.count), font=("ariel", 14), fg="green")
        self.lbl3.pack()

        self.btn = Button(self.win, text="submit",font=("Ariel",13),fg="white",bg="black", command=lambda: self.clicked(t))
        self.btn.pack()

        self.lbl4 = Label(self.win, text="", font=("Ariel", 14), pady=5)
        self.lbl4.pack()

        self.lbl5 = Label(self.win, text="", font=("red", 11))
        self.lbl5.pack()

        self.lbl6 = Label(self.win)
        self.lbl6.pack()

        self.hint_btn = Button(self.win, text="Hint",command=self.hint,bg="grey",fg="white",font=("Arial", 12, "bold"))

        self.hint_btn.pack()
    # creating function for updating the screen after clicking button
    def update(self):
        if hasattr(self, 'entry'):
            self.entry.configure(bg="cyan")
            self.win.after(1000, lambda: self.entry.config(bg="SystemButtonFace"))
            self.win.after(500, lambda: self.entry.delete(0, END))

    # function for checking trials
    def check_trials(self):
        if self.count > 1:
            self.count -= 1
            self.lbl3.configure(text="You have {} trial(s) left".format(self.count))
        elif self.a == t:
            self.lbl3.configure(text="")
        else:
            self.btn.destroy()
            self.lbl3.configure(text="")
            self.lbl4.configure(text="Better Luck Next Time!")
            self.lbl5.configure(text="The correct number was {}".format(t))
            self.lbl6.configure(text="")

    # function performed after clicking submit button
    def clicked(self, t):
        print(t)
        try:
            self.a = int(self.entry.get())
            if self.a < t:
                self.lbl4.configure(text="Try Again! You guessed too small")
                self.check_trials()
                self.update()
            elif self.a > t:
                self.lbl4.configure(text="Try Again! You guessed too high")
                self.check_trials()
                self.update()
            else:
                self.lbl4.configure(text="Congratulations!")
                self.check_trials()
                self.update()
                self.btn.destroy()

        except ValueError:
            self.lbl5.configure(text="Please enter integer value only", fg="red")
            self.win.after(2000, lambda: self.lbl5.configure(text=""))
            self.update()

    # function for hints
    def hint(self):
        hint_text = "Hint: "
        if t % 2 == 0:
            hint_text += "The number is even. \n"
        else:
            hint_text += "The number is odd. \n"

        if t < 50:
            hint_text += "The number is less than 50. \n"
        elif t > 50:
            hint_text += "The number is greater than 50. \n"
        else:
            hint_text += "The number is 50. \n"

        if t % 10 == 0:
            hint_text += "The number is a multiple of 10. \n"

        sqrt_t = int(t ** 0.5)
        if sqrt_t ** 2 == t:
            hint_text += "The number is a perfect square. \n"

        self.lbl6.configure(text=hint_text)

    # function for mainloop
    def play(self):
        self.win.mainloop()

if __name__ == '__main__':
    obj = Screen()
    obj.play()