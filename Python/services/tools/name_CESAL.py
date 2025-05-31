import pyfiglet

def cesal_logo():
    print("-" * 65)
    ascii_art = pyfiglet.figlet_format("C E S A L", font="starwars")
    ascii_pontos = ascii_art.replace("#", ".").replace("*", ".").replace("@", ".").replace("█", ".").replace("|", ".")
    print(ascii_pontos)
    print("CENTRO DE ENSINO SUPERIOR DE ALAGOAS")
    print("-" * 65)