from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import tensorflow as tf
from Savery import *

print("\n## Create network model:")
input_layer = keras.Input(shape=(32,), name='checkers_board')

hidden_layer_1 = layers.Dense(64, activation='relu', name='dense_1')(input_layer)
hidden_layer_2 = layers.Dense(128, activation='relu', name='dense_2')(hidden_layer_1)
hidden_layer_3 = layers.Dense(64, activation='relu', name='dense_3')(hidden_layer_2)

output_piece = layers.Dense(32, activation='softmax', name='piece')(hidden_layer_3)
output_move = layers.Dense(32, activation='softmax', name='move')(hidden_layer_3)

model = keras.Model(
    inputs=[input_layer],
    outputs=[output_piece, output_move],
)

model.summary()
# keras.utils.plot_model(model, "my_first_model.png")
# tf.keras.utils.plot_model(model, to_file="my_first_model.png", show_shapes=True)


# ----------------------------------------------------------------------------------------------------------------------

print("\n## Load and reshape input/output data:")

train_input = load_board()
train_input = train_input.astype('float32') / 5
print("train_input ", train_input)
print("shape ", train_input.shape)
print()
train_output_piece = load_piece()
train_output_piece = train_output_piece.astype('float32')
print("train_output_piece ", train_output_piece)
print("shape ", train_output_piece.shape)
print()
train_output_move = load_move()
train_output_move = train_output_move.astype('float32')
print("train_output_move ", train_output_move)
print("shape ", train_output_move.shape)
print()

# Зарезервируем 10,000 примеров для валидации
border = -11
validation_input = train_input[border:]
train_input = train_input[:border]

validation_output_piece = train_output_piece[border:]
train_output_piece = train_output_piece[:border]

validation_output_move = train_output_move[border:]
train_output_move = train_output_move[:border]

print("validation_input ", validation_input.shape)
print("train_input ", train_input.shape)
print("validation_output_piece ", validation_output_piece.shape)
print("train_output_piece ", train_output_piece.shape)
print("validation_output_move ", validation_output_move.shape)
print("train_output_move ", train_output_move.shape)

# ----------------------------------------------------------------------------------------------------------------------

print("\n## Compile network:")
model.compile(optimizer=keras.optimizers.RMSprop(),
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=[keras.metrics.SparseCategoricalAccuracy()])

print('\n## Train the model on train_data')
history = model.fit(train_input,
                    y=[train_output_piece, train_output_move],
                    batch_size=8,
                    epochs=1000,
                    validation_data=(validation_input, [validation_output_piece, validation_output_move]))

# Возвращаемый объект "history" содержит записи
# значений потерь и метрик во время обучения
print('\nhistory dict:', history.history)

# ----------------------------------------------------------------------------------------------------------------------
# # Возвращаемый объект "history" содержит записи
# # значений потерь и метрик во время обучения
# print('\nhistory dict:', history.history)
#
# # Оценим модель на тестовых данных, используя "evaluate"
print('## Evaluate network:')
results = model.evaluate(validation_input, [validation_output_piece, validation_output_move], batch_size=32)
print('test loss, test acc:', results)
#
#
#
#
# # Сгенерируем прогнозы (вероятности - выходные данные последнего слоя)
# # на новых данных с помощью "predict"
# print('\n# Генерируем прогнозы для 3 образцов')
# predictions = model.predict(test_input[:1])
# for i in range(len(predictions)):
#     print("test_output ", test_output[i], " pred ", np.argmax(predictions[i]))
