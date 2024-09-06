meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY": "spaventoso, inquietante",
            "PARA": "preoccuparsi per qualcosa, paranoiarsi"
            }
parola = input("inserisci una parola meme che non capisci(usa solo lettere maiuscole):")


if parola in meme_dict:
    print(parola, ":", meme_dict[parola])
else:
    print("questa parola non è contenuta nel dizionario")
