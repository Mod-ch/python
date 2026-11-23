from PIL import Image , ImageFilter # type: ignore

before =Image.open("image.jpg")
# before.save("image.jpg")
# before.show()
after = before.filter(ImageFilter.BoxBlur(140)) # type: ignore
after.save("image_flou.jpg")
after.show()
print("Filtre applique avec succes")
# after = before.convert("L")
# after.show()
