import cv2
import os

def detektiraj_lice_i_spremi(originalna_slika, izlazni_direktorij, ime_slike):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(originalna_slika, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(originalna_slika, (x, y), (x+w, y+h), (255, 0, 0), 2)

    izlazna_slika_path = os.path.join(izlazni_direktorij, f'{ime_slike}_bb.jpg')
    cv2.imwrite(izlazna_slika_path, originalna_slika)
    print(f'Spremljena slika: {izlazna_slika_path}')

def procesiraj_slike_u_direktoriju(direktorij_ulazni, izlazni_direktorij):
    for ime_slike in os.listdir(direktorij_ulazni):
        putanja_do_slike = os.path.join(direktorij_ulazni, ime_slike)
        originalna_slika = cv2.imread(putanja_do_slike)

        detektiraj_lice_i_spremi(originalna_slika, izlazni_direktorij, ime_slike)

if __name__ == "__main__":
    ulazni_direktorij = 'lfw-deepfunneled'
    izlazni_direktorij = 'lfw-deepfunneled-oznacene_slike'

    if not os.path.exists(izlazni_direktorij):
        os.makedirs(izlazni_direktorij)

    procesiraj_slike_u_direktoriju(ulazni_direktorij, izlazni_direktorij)
