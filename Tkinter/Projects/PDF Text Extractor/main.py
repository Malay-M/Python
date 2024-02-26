import tkinter
from tkinter import filedialog
import PyPDF2

def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file", 
                                          initialdir="F:\Code\Python\Tkinter\Projects\PDF Text Extractor",
                                          filetypes=[("PDF files", "*.pdf")])
    
    filename_label.configure(text=filename)
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)


    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        outputfile_text.insert(tkinter.END, current_text)
    
    

window = tkinter.Tk()
window.title("PDF Text Extractor")



filename_label = tkinter.Label(window, text="No File Selected")
filename_label.pack()

outputfile_text = tkinter.Text(window)
outputfile_text.pack()

openfile_button = tkinter.Button(window, text="Open PDF File", command=openFile)
openfile_button.pack()

window.mainloop()
