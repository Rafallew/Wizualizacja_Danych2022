produkt1 = {
    "masło": "szt",
    "chleb": "szt",
    "ziemniaki": "kg",
    "sok pomarańczowy": "l",
    "pasta do zębów": "szt",
    "coca cola": "l",
}

print("Produkty sporzywcze do kupienia: ", produkt1)

produkt2 = {k: v for (k, v) in produkt1.items() if v == "szt"}

print("Produkty do kupienia na sztuki: ", produkt2)