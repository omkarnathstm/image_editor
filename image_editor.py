from PIL import Image
import numpy as np


class ImageEditor:
    def __init__(self):
        self.image = None
        self.image_name = None

    def load_image(self):
        while True:
            try:
                self.image_name = input("Enter image name: ")
                self.image = np.asarray(
                    Image.open(f"images/{self.image_name}")
                )
                print("Image loaded successfully!\n")
                break

            except FileNotFoundError:
                print("❌ Image not found. Please try again.\n")

    def image_info(self):
        if self.image is None:
            print("No image loaded")
            return

        height, width, channel = self.image.shape

        print("===== Image Info =====")
        print(f"Height  : {height}")
        print(f"Width   : {width}")
        print(f"Channel : {channel}")
        print("======================\n")

    def negative_image(self):
        if self.image is None:
            print("No image loaded")
            return

        self.image = 255 - self.image
        print("Negative image created.\n")

    def gray_scale(self):
        if self.image is None:
            print("No image loaded")
            return

        self.image = np.mean(self.image, axis=2).astype(np.uint8)
        print("Grayscale image created.\n")

    def brightness(self):
        if self.image is None:
            print("No image loaded")
            return
        while True:
            brightness_value = int(input("Enter brightness (-255 to 255): "))
            if -255 <= brightness_value <= 255:
                break
            print("Please enter a value between -255 and 255.")
        temp_image = self.image.astype(np.int16)
        self.image = np.clip(temp_image + brightness_value,
                             0, 255).astype(np.uint8)

    def contrast(self):
        if self.image is None:
            print("No image loaded")
            return
        factor = float(input("Enter contrast factor: "))
        temp_image = self.image.astype(np.float32)
        self.image = (temp_image - 128) * factor + 128
        self.image = np.clip(self.image, 0, 255)
        self.image = self.image.astype(np.uint8)

    def flip(self):
        if self.image is None:
            print("No image loaded")
            return
        while True:
            flip_aspect = input("Enter flip aspect h or v")
            if flip_aspect not in ("h", "v"):
                print("Invalid input")
            else:
                break
        if flip_aspect == "h":
            self.image = self.image[:, ::-1]
        else:
            self.image = self.image[::-1, :]

    def save_image(self):
        if self.image is None:
            print("No image loaded")
            return

        image = Image.fromarray(self.image)
        image.save(f"output/{self.image_name}")

        print(f"Image saved successfully as output/{self.image_name}")


# ---------------- MAIN ----------------

editor = ImageEditor()

editor.load_image()
editor.image_info()
# editor.negative_image()
# editor.gray_scale()
# editor.brightness()
# editor.contrast()
editor.flip()
editor.save_image()


print((np.array([250], dtype=np.uint8))+20)
