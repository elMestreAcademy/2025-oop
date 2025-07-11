import tkinter as tk
from tkinter import ttk


# 1) Clase base
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50      # 0 = lleno, 100 = hambriento
        self.energy = 50      # 0 = exhausto, 100 = descansado
        self.happiness = 50   # 0 = triste, 100 = feliz

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.happiness = min(100, self.happiness + 5)

    def rest(self):
        self.energy = min(100, self.energy + 30)

    def play(self):
        """Sobrescribir en subclases: gasta energía y sube felicidad."""
        raise NotImplementedError

    def make_sound(self):
        """Sobrescribir: ladra, maúlla, canta…"""
        raise NotImplementedError


# 2) Subclases
class Dog(Pet):
    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.happiness = min(100, self.happiness + 15)
        else:
            print(f"{self.name} está muy cansado para jugar.")

    def make_sound(self):
        return "¡Guau!"


class Cat(Pet):
    def play(self):
        if self.energy >= 5:
            self.energy -= 5
            self.happiness = min(100, self.happiness + 10)
        else:
            print(f"{self.name} está perezoso para jugar.")

    def make_sound(self):
        return "Miau!"


# 3) Interfaz con Tkinter
class PetApp:
    def __init__(self):
        self.pet = None
        self.root = tk.Tk()
        self.root.title("Mascota Virtual")
        self._build_ui()
        self.root.mainloop()

    def _build_ui(self):
        self._pets_frame()
        self._bars_frame()
        self._action_frame()

    def _pets_frame(self):
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)
        tk.Label(frame_top, text="Elige tu mascota:").pack(side="left")
        for cls in (Dog, Cat):
            btn = tk.Button(
                frame_top,
                text=cls.__name__,
                command=lambda
                c=cls: self._create_pet(c)
            )
            btn.pack(side="left", padx=5)

    def _bars_frame(self):
        self.info = {}
        frame_mid = tk.Frame(self.root)
        frame_mid.pack(pady=10)
        for attr in ("hunger", "energy", "happiness"):
            lbl = tk.Label(frame_mid, text=f"{attr.capitalize()}:")
            lbv = ttk.Progressbar(frame_mid, length=150, maximum=100)
            lbl.pack()
            lbv.pack(pady=2)
            self.info[attr] = lbv

    def _action_frame(self):
        frame_bot = tk.Frame(self.root)
        frame_bot.pack(pady=10)
        for act in ("feed", "play", "rest", "make_sound"):
            btn = tk.Button(frame_bot, text=act.capitalize(),
                            command=getattr(self, act))
            btn.pack(side="left", padx=5)

    def _create_pet(self, cls):
        name = cls.__name__ + str(1)  # o pedir input
        self.pet = cls(name)
        self._update_ui()

    def _update_ui(self):
        for attr, widget in self.info.items():
            widget['value'] = getattr(self.pet, attr)

    def feed(self):
        if self.pet:
            self.pet.feed()
            self._update_ui()

    def play(self):
        if self.pet:
            self.pet.play()
            self._update_ui()

    def rest(self):
        if self.pet:
            self.pet.rest()
            self._update_ui()

    def make_sound(self):
        if self.pet:
            print(self.pet.make_sound())


if __name__ == "__main__":
    PetApp()
