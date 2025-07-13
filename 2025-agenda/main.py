from contacto import Contacto
import time

contactos = []


def listar():
    for contacto in contactos:
        print(contacto)


if __name__ == "__main__":
    contactos.append(Contacto("Pepe", "Mártinez"))
    contactos.append(Contacto("Marta", "Barquero"))
    print("Contactos creados:")
    listar()
    print("Esperando...")
    time.sleep(0.5)

    print(contactos[0])
    print(contactos[0])
    print(contactos[0])
    print(contactos[0])
    print("=" * 24)
    time.sleep(2)

    contactos[1].nombre = "Petunja"
    contactos[1].nombre = "Petuni"
    contactos[1].nombre = "Petunia"
    listar()

    print("-" * 24)
    time.sleep(2)
    print(contactos[0])
    print(contactos[1])
    print(contactos[0])

    print("-" * 24)
    time.sleep(2)
    listar
