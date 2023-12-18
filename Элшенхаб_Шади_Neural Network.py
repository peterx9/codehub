#Реализация сверточной нейронной сети (CNN) может быть выполнена с использованием популярных платформ глубокого обучения, 
#таких как TensorFlow с API Keras или PyTorch. Я приведу простой пример использования TensorFlow и Keras для классификации изображений. 
#В этом примере предполагается, что TensorFlow установлен (pip install tensorflow).

# Импортируйте необходимые библиотеки
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Определите модель CNN
model = models.Sequential()

# Сверточные слои
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Сгладить слой
model.add(layers.Flatten())

# Полностью связанные слои
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))  # Assuming you have 10 classes

# Скомпилируйте модель
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Распечатайте сводную информацию об архитектуре модели.
model.summary()



#Подготовка данных:

# Определите генераторы данных
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# Укажите путь к вашему набору данных
train_generator = train_datagen.flow_from_directory('path/to/train',
                                                    target_size=(224, 224),
                                                    batch_size=32,
                                                    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory('path/to/validation',
                                                        target_size=(224, 224),
                                                        batch_size=32,
                                                        class_mode='categorical')


# Обучение модели:
#В этом примере модель обучается в течение 10 эпох.
history = model.fit(train_generator,
                    epochs=10,
                    validation_data=validation_generator)




#теперь это улучшенный код

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Определение модели CNN
model = models.Sequential()

# Сверточные слои
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.5))  # Добавление слоя Dropout
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.5))  # Добавление слоя Dropout
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.5))  # Добавление слоя Dropout

# Сглаживание
model.add(layers.Flatten())

# Полностью связанные слои
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))  # Добавление слоя Dropout
model.add(layers.Dense(10, activation='softmax'))  # Предполагая 10 классов

# Компиляция модели
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Вывод информации о модели
model.summary()

# Подготовка данных
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    'path/to/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    'path/to/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Обучение модели
history = model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

# Сохранение модели
model.save('image_classification_model.h5')

# Визуализация обучения
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
