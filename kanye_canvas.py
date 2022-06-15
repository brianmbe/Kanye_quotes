from tkinter import *
from quote import kanye_quote


def create_canvas():
    def get_quote():
        return kanye_quote()

    window = Tk()
    window.title("KANYE WEST'S QUOTES")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"),
                       fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()
