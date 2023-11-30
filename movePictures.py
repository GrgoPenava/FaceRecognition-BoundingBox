import os
import shutil

def izvadi_slike(ulazni_direktorij, izlazni_direktorij):
    for korisnik in os.listdir(ulazni_direktorij):
        korisnik_putanja = os.path.join(ulazni_direktorij, korisnik)
        if os.path.isdir(korisnik_putanja):
            for slika in os.listdir(korisnik_putanja):
                slika_putanja = os.path.join(korisnik_putanja, slika)
                if os.path.isfile(slika_putanja):
                    izlazna_putanja = os.path.join(izlazni_direktorij, slika)
                    shutil.move(slika_putanja, izlazna_putanja)
                    print(f'Pomaknuta slika: {izlazna_putanja}')

if __name__ == "__main__":
    ulazni_direktorij = 'lfw-deepfunneled'
    izlazni_direktorij = 'lfw-deepfunneled'

    if not os.path.exists(izlazni_direktorij):
        os.makedirs(izlazni_direktorij)

    izvadi_slike(ulazni_direktorij, izlazni_direktorij)
