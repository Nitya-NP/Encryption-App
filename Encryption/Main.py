import tkinter as tk
from tkinter import ttk, messagebox
from Encryption import Encryption

def updateCipherOptions(event=None):
    cipher = cipherChoice.get()

    shiftLabel.pack_forget()
    shiftEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()

    if cipher == "Caesar":
        shiftLabel.pack(pady=(5, 0))
        shiftEntry.pack(pady=5)
    elif cipher == "Password":
        passwordLabel.pack(pady=(5, 0))
        passwordEntry.pack(pady=5)


def processMessage():
    msg = inputText.get("1.0", tk.END).rstrip()
    cipher = cipherChoice.get()
    mode = modeChoice.get()

    if not msg:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    try:
        if cipher == "Caesar":
            shift = int(shiftEntry.get())
            result = (
                Encryption.caesarEncrypt(msg, shift)
                if mode == "Encrypt"
                else Encryption.caesarDecrypt(msg, shift)
            )

        elif cipher == "Symbol":
            result = (
                Encryption.symbolEncrypt(msg)
                if mode == "Encrypt"
                else Encryption.symbolDecrypt(msg)
            )

        elif cipher == "Password":
            password = passwordEntry.get()
            if not password:
                messagebox.showwarning("Warning", "Please enter a password.")
                return
            result = (
                Encryption.passwordEncrypt(msg, password)
                if mode == "Encrypt"
                else Encryption.passwordDecrypt(msg, password)
            )
        else:
            return

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    outputText.config(state="normal")
    outputText.delete("1.0", tk.END)
    outputText.insert(tk.END, result)
    outputText.config(state="disabled")


def copyResult():
    result = outputText.get("1.0", tk.END).strip()
    if not result:
        messagebox.showwarning("Warning", "Nothing to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    messagebox.showinfo("Copied", "Result copied to clipboard.")


def clearAll():
    inputText.delete("1.0", tk.END)
    outputText.config(state="normal")
    outputText.delete("1.0", tk.END)
    outputText.config(state="disabled")
    shiftEntry.delete(0, tk.END)
    shiftEntry.insert(0, "3")
    passwordEntry.delete(0, tk.END)

# ================= GUI SETUP =================

root = tk.Tk()
root.title("Encryption App")
root.geometry("700x600")
root.configure(bg="#1e1e1e")

# Colors & Fonts
colorBg = "#1e1e1e"
colorText = "#ffffff"
colorEntry = "#2e2e2e"
colorButton = "#ff4c4c"
colorCopy = "#3a86ff"
colorClear = "#555555"

fontLabel = ("consolas", 18, "bold")
fontText = ("consolas", 12)

# ================= INPUT =================

tk.Label(
    root,
    text="E N C O D E D",
    bg=colorBg,
    fg=colorButton,
    font=("consolas", 30, "bold")
).pack(pady=(5, 5))


tk.Label(root, text="Enter Message", bg=colorBg, fg=colorText, font=fontLabel).pack(pady=(10, 0))
inputText = tk.Text(root, height=5, width=65, bg=colorEntry, fg=colorText, insertbackground=colorText)
inputText.pack(pady=5)

# ================= MODE =================

modeChoice = tk.StringVar(value="Encrypt")
frameMode = tk.Frame(root, bg=colorBg)
frameMode.pack(pady=5)

tk.Radiobutton(
    frameMode, text="Encrypt", variable=modeChoice, value="Encrypt",
    bg=colorBg, fg=colorText, selectcolor=colorEntry,font = fontText
).pack(side="left", padx=30)

tk.Radiobutton(
    frameMode, text="Decrypt", variable=modeChoice, value="Decrypt",
    bg=colorBg, fg=colorText, selectcolor=colorEntry, font = fontText
).pack(side="left", padx=30)

# ================= CIPHER =================

tk.Label(root, text="Cipher Type", bg=colorBg, fg=colorText, font=fontText).pack()
cipherChoice = ttk.Combobox(root, values=["Caesar", "Symbol", "Password"], state="readonly")
cipherChoice.current(0)
cipherChoice.pack(pady=5)
cipherChoice.bind("<<ComboboxSelected>>", updateCipherOptions)

# ================= OPTIONS =================

shiftLabel = tk.Label(root, text="Shift (Caesar Cipher)", bg=colorBg, fg=colorText, font=fontText)
shiftEntry = tk.Entry(root, bg=colorEntry, fg=colorText, insertbackground=colorText)
shiftEntry.insert(0, "3")

passwordLabel = tk.Label(root, text="Password", bg=colorBg, fg=colorText, font=fontLabel)
passwordEntry = tk.Entry(root, bg=colorEntry, fg=colorText, insertbackground=colorText, show="*")

updateCipherOptions()

# ================= BUTTONS =================

frameButtons = tk.Frame(root, bg=colorBg)
frameButtons.pack(pady=5)

processButton = tk.Button(
    frameButtons, text="Encrypt / Decrypt",
    bg=colorButton, fg="#ffffff",
    font=("consolas", 12, "bold"),
    width=18, command=processMessage
)
processButton.pack(side="left", padx=8)

copyButton = tk.Button(
    frameButtons, text="Copy Result",
    bg=colorCopy, fg="#ffffff",
    font=("consolas", 12, "bold"),
    width=14, command=copyResult
)
copyButton.pack(side="left", padx=8)

clearButton = tk.Button(
    frameButtons, text="Clear",
    bg=colorClear, fg="#ffffff",
    font=("consolas", 12, "bold"),
    width=10, command=clearAll
)
clearButton.pack(side="left", padx=8)

# ================= OUTPUT =================

tk.Label(root, text="Result", bg=colorBg, fg=colorText, font=fontLabel).pack(pady=10)
outputText = tk.Text(root, height=5, width=65, bg=colorEntry, fg=colorText, state="disabled")
outputText.pack()

footerLabel = tk.Label(root, text="© 2025 Nitya Patel | Encryption Tool – Keep your text secure", bg=colorBg, fg="#aaaaaa", font=("Helvetica", 10))
footerLabel.pack(side="bottom", pady=10)


root.mainloop()
