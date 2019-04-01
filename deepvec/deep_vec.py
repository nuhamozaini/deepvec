import pandas as pd
from tensorflow.python.keras.layers import Dense, GRU
from tensorflow.python.keras.layers.embeddings import Embedding
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.python.keras.preprocessing.text import Tokenizer

from deepvec.helpers import read_lines, divide


class DeepVec:

    def __init__(self, path='', feature='', label=''):
        self.path = path
        self.feature = feature
        self.label = label

    def prepare(self):
        data_frame = pd.read_csv(open(self.path, 'rU'), encoding='utf-8', engine='c')
        return data_frame

    def proceed(self, data_frame):
        observations = read_lines(self.path)
        first_part, second_part = divide(observations-1)
        x_train = [line.strip() for line in data_frame.loc[:first_part, self.feature]]
        y_train = data_frame.loc[:first_part, self.label]
        x_test = [line.strip() for line in data_frame.loc[second_part:, self.feature]]
        y_test = data_frame.loc[second_part:, self.label]
        self.tokenize(x_train, y_train, x_test, y_test)

    def tokenize(self, x_train, y_train, x_test, y_test):
        tokenizer_obj = Tokenizer()
        total = x_train + x_test
        tokenizer_obj.fit_on_texts(total)

        max_length = len(total)
        vocab_size = len(tokenizer_obj.word_index) + 1
        x_train_tokens = tokenizer_obj.texts_to_sequences(x_train)
        x_test_tokens = tokenizer_obj.texts_to_sequences(x_test)

        x_train_pad = pad_sequences(x_train_tokens, maxlen=max_length, padding='post')
        x_test_pad = pad_sequences(x_test_tokens, maxlen=max_length, padding='post')
        model = DeepVec.build(vocab_size, max_length)
        DeepVec.train(model, x_train_pad, y_train, x_test_pad, y_test)

    @staticmethod
    def build(vocab_size, max_length):
        embedding = 100
        model = Sequential()
        model.add(Embedding(vocab_size, embedding, input_length=max_length))
        model.add(GRU(units=32, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model

    @staticmethod
    def train(model, x_train_pad, y_train, x_test_pad, y_test):
        model.fit(x_train_pad, y_train, batch_size=128, epochs=5, validation_data=(x_test_pad, y_test), verbose=2)



