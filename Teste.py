import BlackBox as bb
import cv2

teste = bb.classify()

raça = str(teste["class_name"])
confidence = teste["confidence"]

print(raça)

raça_to_file = {
    'poodle': 'modelos/poodle.jpg',
    'bull_terrier': 'modelos/bull_terrier.jpg',
    'labrador': 'modelos/labrador.jpg',
    'pug': 'modelos/pug.jpg',
    'beagle': 'modelos/beagle.jpg',
    'chiuahua': 'modelos/chiuahua.jpg'
}

print(raça)
aux = raça_to_file[raça]

img = cv2.imread(aux, 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
