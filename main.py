if __name__ == "__main__":
    from cli import LatexOCR
    from PIL import Image
    image = Image.open(r'img\test.jpg')
    model = LatexOCR()
    print('$'+model(image)+'$')