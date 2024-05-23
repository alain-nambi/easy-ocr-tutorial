import easyocr

# Initialize the EasyOCR reader with English and French languages
reader = easyocr.Reader(['fr'])  # explicitly set gpu=False to avoid CUDA/MPS warnings

# # Read the image file
# with open("Capture d’écran du 2024-05-22 12-18-45.png", "rb") as f:
#     img = f.read()

# print(img)

# Perform OCR on the image
results = reader.readtext("Capture d’écran du 2024-05-22 12-18-45.png")

print(results)

# print(results.text)

texts = []
for (bbox, text, prob) in results:
    texts.append(text)
print(f'Text: {texts}')

