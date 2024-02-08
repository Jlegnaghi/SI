import keyboard

def main():
    print("Pressione 'Alt + Shift + S' para sair.")
    barcode = ""
    keyboard.add_hotkey("alt+shift+s", lambda: exit_program(barcode))

    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "enter":
                save_barcode(barcode)
                barcode = ""
            else:
                barcode += event.name

def save_barcode(barcode):
    with open("codigos.txt", "a") as file:
        file.write(barcode + "\n")
        print(f"Código '{barcode}' salvo em codigos.txt")

def exit_program(barcode):
    if barcode:
        save_barcode(barcode)
    print("Programa encerrado.")
    exit()

if __name__ == "__main__":
    main()
