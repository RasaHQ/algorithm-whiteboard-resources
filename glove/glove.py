from tensorflow.keras.layers import Embedding, Dense, Flatten, Input, Dot
from tensorflow.keras.models import Sequential, Model

dim_words = 5

# this one is so we might grab the embeddings
model_emb = Sequential()
embedding = Embedding(num_words, dim_words, input_length=1)
model_emb.add(embedding)
model_emb.add(Flatten())

word_one = Input(shape=(1,))
word_two = Input(shape=(1,))

cross_prod = Dot(axes=1)([model_emb(word_one), model_emb(word_two)])
out = Dense(1, activation="relu")(cross_prod)

glovelike = Model(inputs=[word_one, word_two], outputs=out)