from requests import get
from tkinter import Canvas


def kanye_quote():
    canvas = Canvas()
    quote_text = canvas.create_text(150, 207, text="Kanye's quote", width=250, font=("Arial", 20, "bold"),
                                    fill="white")

    response = get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
