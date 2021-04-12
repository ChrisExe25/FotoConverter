from PIL import Image

print("inserisci la tua immagine, nella stessa cartella di questo file.")

image = input("inserisci il nome dell'immagine (compresa l'estensione): ")

img = Image.open(image)
bEw = img.convert("L")
bEw.save(input("inserisci il nome dell'output (comresa estensione): "))
bEw.show()

input('Immagine salvata, premi invio per chiudere.')
