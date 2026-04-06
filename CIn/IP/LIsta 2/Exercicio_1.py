print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")

quantidade = 0
lista_musicas = ""

musica = input()

while musica.lower() != "voa, voa brabuleta":
    quantidade += 1
    lista_musicas += musica

    musica = input()

    if musica.lower() != "voa, voa brabuleta":
        lista_musicas += " - "

print(f"A quantidade de músicas selecionadas foi {quantidade}")
print(f"Setlist de músicas: {lista_musicas}")