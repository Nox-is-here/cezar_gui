import tkinter as tk
from tkinter import ttk
from tkinter import *


def cezar(x, combobox):
    polskie_litery = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    duze_polskie_litery = polskie_litery.upper()

    przesuniecie = int(combobox.get())

    if x in polskie_litery:
        indeks_l = polskie_litery.find(x)
        nowy_indeks = (
            indeks_l + przesuniecie
        ) % len(polskie_litery)

        return polskie_litery[nowy_indeks]

    elif x in duze_polskie_litery:
        indeks_l = duze_polskie_litery.find(x)
        nowy_indeks = (
            indeks_l + przesuniecie
        ) % len(duze_polskie_litery)

        return duze_polskie_litery[nowy_indeks]

    else:
        return x


def cezar2(x, combobox):
    polskie_litery = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    duze_polskie_litery = polskie_litery.upper()

    przesuniecie = int(combobox.get())

    if x in polskie_litery:
        przesuniecie = combobox.get()
        indeks_l = polskie_litery.find(x)
        nowy_indeks = (indeks_l - int(przesuniecie)) % len(polskie_litery)
        return polskie_litery[nowy_indeks]
    elif x in duze_polskie_litery:
        przesuniecie = combobox.get()
        indeks_l = duze_polskie_litery.find(x)
        nowy_indeks = (indeks_l - int(przesuniecie)
                       ) % len(duze_polskie_litery)
        return duze_polskie_litery[nowy_indeks]
    else:
        return x


def przetworzanie(event=None):

    tekst = text_wejscie.get("1.0", "end-1c")

    przetworzony = ""
    for znak in tekst:
        przetworzony += cezar(znak, combo_box)

    text_zaszyfrowany.delete("1.0", "end")
    text_zaszyfrowany.insert("1.0", przetworzony)


def place():
    pass


def select(event):
    selected_item = combo_box.get()
    label.config(text="Wybierz przesuniecie: " + selected_item)


def nowe_okno():
    top2 = Toplevel()
    top2.title("Szyfr Cezara - odszyfrowywanie!")

    ramka1_nowe_okno = tk.Frame(top2)

    label = tk.Label(
        ramka1_nowe_okno,
        text="Wybierz przesuniecie: "
    )
    label.grid(row=1, column=1)

    combo_box2 = ttk.Combobox(
        ramka1_nowe_okno,
        values=[x for x in range(1, 37)],
        state="readonly",
        width=3
    )
    combo_box2.grid(row=1, column=5)

    combo_box2.set("2")

    ramka1_nowe_okno.pack(
        anchor="nw",
        pady=(15, 15),
        padx=20
    )

    # tekst wejściowy
    label1_top = tk.Label(
        top2,
        text="Wprowadź zaszyfrowaną wiadomość:",
        fg="black"
    )
    label1_top.pack(anchor="nw", padx=20)

    text_wejscie2 = Text(
        top2,
        height=10,
        width=50
    )
    text_wejscie2.pack(
        padx=(20, 20),
        pady=(0, 10)
    )

    # tekst wyjściowy
    label2 = tk.Label(
        top2,
        text="Odszyfrowana wiadomość:",
        fg="black"
    )
    label2.pack(anchor="nw", padx=20)

    text_odszszyfrowany = Text(
        top2,
        height=10,
        width=50
    )
    text_odszszyfrowany.pack(
        padx=(20, 20),
        pady=(0, 20)
    )

    def przetworzanie2(event=None):
        tekst = text_wejscie2.get("1.0", "end-1c")

        przetworzony = ""

        for znak in tekst:
            przetworzony += cezar2(
                znak,
                combo_box2
            )

        text_odszszyfrowany.delete("1.0", "end")
        text_odszszyfrowany.insert(
            "1.0",
            przetworzony
        )

    text_wejscie2.bind(
        "<KeyRelease>",
        przetworzanie2
    )

    combo_box2.bind(
        "<<ComboboxSelected>>",
        przetworzanie2
    )

    button = Button(
        top2,
        text="Zamknij",
        width=25,
        command=top2.destroy
    )
    button.pack(pady=(0, 20))


# main window
root = tk.Tk()
root.title("Szyfr Cezara - szyfrowanie")


ramka1 = tk.Frame(root)


label = tk.Label(ramka1, text="Wybierz przesuniecie: ")
label.grid(row=1, column=1)

# Combobox
combo_box = ttk.Combobox(
    ramka1,
    values=[x for x in range(1, 37)],
    state="readonly",
    width=3
)
combo_box.grid(row=1, column=5)

combo_box.set("2")

combo_box.bind(select)

ramka1.pack(anchor="nw", pady=(15, 15), padx=20)

# label 1
label1 = tk.Label(root, text="Wprowadź wiadomość: ", fg="black")
label1.pack(anchor="nw", padx=20)


# tekst widget 1
text_wejscie = Text(root, height=10, width=50)
text_wejscie.pack(padx=(20, 20), pady=(0, 10))

text_wejscie.bind("<KeyRelease>", przetworzanie)

combo_box.bind(
    "<<ComboboxSelected>>",
    przetworzanie
)

# label 2
label2 = tk.Label(root, text="Zaszyfrowana wiadomość: ", fg="black")
label2.pack(anchor="nw", padx=20)


# tekst widget 2
text_zaszyfrowany = Text(root, height=10, width=50)
text_zaszyfrowany.pack(padx=(20, 20), pady=(0, 20))


# button
button = tk.Button(root, text="Odszyfrowywanie", width=25,
                   command=nowe_okno)
button.pack(pady=(0, 20))


root.mainloop()
