from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('image.jpg')

# Изменение размера изображения
resized_image = image.resize((200, 200))

# Применение размытия
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Сохранение изображения в другом формате
blurred_image.save('blurred_image.png')

# Вывод информации о изображении
print(f'Original size: {image.size}, Resized size: {resized_image.size}')