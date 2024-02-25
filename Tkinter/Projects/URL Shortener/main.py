import tkinter
import pyshorteners


window = tkinter.Tk()

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)


window.title("URL Shortener")
window.geometry("300x150")

longurl_label = tkinter.Label(window, text="Enter Long URL")
longurl_entry = tkinter.Entry(window)
shorturl_label = tkinter.Label(window, text="Output Shortened URL")
shorturl_entry = tkinter.Entry(window)
shortener_button = tkinter.Button(window, text="Shorten URL", command=shorten)


longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shortener_button.pack()


window.mainloop()