from tensorflow import keras
from tensorflow.keras import layers
import numpy as np




inputs = keras.Input(shape=(784,), name='digits')
print("inputs ", inputs)
print("shape ", inputs.shape)
x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
x = layers.Dense(64, activation='relu', name='dense_2')(x)
outputs = layers.Dense(10, activation='softmax', name='predictions')(x)

print("outputs ", outputs)
print("shape ", outputs.shape)

model = keras.Model(inputs=inputs, outputs=outputs)


# ----------------------------------------------------------------------------------------------------------------------
# Загрузим учебный датасет для этого примера
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("train_input ", x_train)
print("shape ", x_train.shape)
x_train = x_train.reshape(60000, 784).astype('float32') / 255


print("train_output ", y_train)
print("shape ", y_train.shape)
y_train = y_train.astype('float32')


print("test_input ", x_test)
print("shape ", x_test.shape)
x_test = x_test.reshape(10000, 784).astype('float32') / 255


print("test_output ", y_test)
print("shape ", y_test.shape)
y_test = y_test.astype('float32')

# Предобработаем данные (это массивы Numpy)

# Зарезервируем 10,000 примеров для валидации
x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]

print("x_train ", x_train)
print("type ", type(x_train))
print("shape ", x_train.shape)


# ----------------------------------------------------------------------------------------------------------------------
# Укажем конфигурацию обучения (оптимизатор, функция потерь, метрики)
model.compile(optimizer=keras.optimizers.RMSprop(),
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=[keras.metrics.SparseCategoricalAccuracy()])


# Обучим модель разбив данные на "пакеты"
# размером "batch_size", и последовательно итерируя
# весь датасет заданное количество "эпох"
print('# Обучаем модель на тестовых данных')
history = model.fit(x_train,
                    y_train,
                    batch_size=32,
                    epochs=1,
                    # Мы передаем валидационные данные для
                    # мониторинга потерь и метрик на этих данных
                    # в конце каждой эпохи
                    validation_data=(x_val, y_val))


# ----------------------------------------------------------------------------------------------------------------------
# Возвращаемый объект "history" содержит записи
# значений потерь и метрик во время обучения
print('\nhistory dict:', history.history)

# Оценим модель на тестовых данных, используя "evaluate"
print('\n# Оцениваем на тестовых данных')
results = model.evaluate(x_test, y_test, batch_size=128)
print('test loss, test acc:', results)

# Сгенерируем прогнозы (вероятности - выходные данные последнего слоя)
# на новых данных с помощью "predict"
print('\n# Генерируем прогнозы для 3 образцов')
predictions = model.predict(x_test[:1])
for i in range(len(predictions)):
    print("test_output ", y_test[i], " pred ", np.argmax(predictions[i]))

# print("test_input[:3]: ", test_input[:3])
# print("test_output[:3]: ", test_output[:3])
# print("predictions ", predictions)
# print('размерность прогнозов:', predictions.shape)