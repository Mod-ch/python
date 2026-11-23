import qrcode  # pyright: ignore[reportMissingModuleSource]
img = qrcode.make("baba chemaci")
img.save("hello.png")