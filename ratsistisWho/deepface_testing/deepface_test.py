from deepface import DeepFace

obj = DeepFace.analyze(img_path='panemorfosMixalis.jpg', actions = ['race'])

print(obj)