
import fitz
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def edit_pdf():
    file = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file:
        return

    doc = fitz.open(file)
    text = simpledialog.askstring("PDF Editor", "Enter text:")

    if text:
        page = doc[0]
        page.insert_text(
            (100, 100), text,
            fontsize=20,
            color=(1, 0, 0)
        )

        save = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if save:
            doc.save(save)
            messagebox.showinfo("Success", "PDF Saved!")

    doc.close()

root = tk.Tk()
root.title("Mini PDF Editor")
root.geometry("300x150")

tk.Button(
    root,
    text="Open & Edit PDF",
    command=edit_pdf
).pack(pady=40)

root.mainloop()
