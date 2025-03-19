import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Input, Embedding, Dense, LayerNormalization, Dropout, MultiHeadAttention, GlobalAveragePooling1D, Flatten, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import pretty_midi
from sklearn.model_selection import train_test_split

# the Transformer - courtesy of geeks4geeks - https://www.geeksforgeeks.org/transformer-model-from-scratch-using-tensorflow/
class Transformer(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads, dff, dropout_rate=0.1):
        super(Transformer, self).__init__()
        self.att = MultiHeadAttention(d_model, num_heads)
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(dropout_rate)
        self.dropout2 = Dropout(dropout_rate)
        self.ffn = tf.keras.Sequential([
            Dense(dff, activation="relu"),
            Dense(d_model)
        ])

    def call(self, x, training, mask):
        attn_output = self.att(x, x, mask)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(x + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        out2 = self.layernorm2(out1 + ffn_output)
        return out2


##################################### setup

keys_dict = pd.read_csv("Output/keys_dict-2.csv")
N=4

lblEncoder = LabelEncoder()
allChords = pd.concat([keys_dict[f"prev_chord_{i+1}"].fillna("None") for i in range(N)])
lblEncoder.fit(allChords.unique()+["None"])

# chord labels
keys_dict["chord"] = keys_dict["chord"].fillna("None")
keys_dict["chord"] = lblEncoder.fit_transform(keys_dict["chord"])
chordLbls = np.array(keys_dict["chord"])

# prev chords
for i in range(N):
    keys_dict[f"prev_chord_{i+1}"] = lblEncoder.fit_transform(keys_dict[f"prev_chord_{i+1}"].fillna("None"))

prevChords = np.array(keys_dict[[f"prev_chord_{i+1}" for i in range(N)]].values)

# melody sequences
melodySequences = [str(val) for val in keys_dict['melody_sequence']]
numericizedMelodySequences = [list(map(int, [i.strip(",") for i in seq[1:-1].split(", ")])) for seq in melodySequences]
maxSeqLen = len(max(numericizedMelodySequences, key=(lambda x: len(x))))
paddedNumericizedMelodySequences = np.array([(seq + [0]*(maxSeqLen-len(seq))) for seq in numericizedMelodySequences])

#####################################
##################################### model setup

# train-val/test split -> first is excluded due to that being the test song (reference the end of the code for more info)
# 80-20 split
trainXmelody, testXmelody, trainXchords, testXchords, trainY, testY = train_test_split(paddedNumericizedMelodySequences[5:], prevChords[5:], chordLbls[5:], test_size=0.2, random_state=95)

# melody model
melodyInput = Input(shape=(maxSeqLen,))

melodyEmbedding = Embedding(input_dim=128, output_dim=32, mask_zero=True)
outputM_E = melodyEmbedding(melodyInput) # simplifies data from high dimension to lower dimension space

melodyTransformer = Transformer(32, 6, 64) 
outputM_T = melodyTransformer(outputM_E, training=True, mask= tf.cast(melodyEmbedding.compute_mask(outputM_E), dtype=tf.float32))

melodyPooled = GlobalAveragePooling1D()
outputM_P = melodyPooled(outputM_T)

# prev chord model
chordInput = Input(shape=(N,))

chordEmbedding = Embedding(input_dim = len(lblEncoder.classes_), output_dim=32)
outputC_E = chordEmbedding(chordInput)

chordFlat = Flatten()
outputC_F = chordFlat(outputC_E)

chordDense = Dense(32, activation="relu")
outputC_D = chordDense(outputC_F)

# merge both models
mergerFunc = Concatenate()
mergedModel = mergerFunc([outputM_P, outputC_D])

# final dense layer
finalDense = Dense(64, activation="relu")
output_FD = finalDense(mergedModel)

# output dense layer
outputLyr = Dense(len(lblEncoder.classes_), activation="softmax")
output = outputLyr(output_FD)

# model compiling
lr = 0.001
model = Model(inputs=[melodyInput, chordInput], outputs=output)
model.compile(optimizer=Adam(learning_rate = lr), loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=["accuracy"])

#####################################
##################################### da training

batchSize = 32 # 32 8 16
epochs = 5

model.fit([trainXmelody, trainXchords], trainY, validation_data=([testXmelody, testXchords], testY), batch_size=batchSize, epochs=epochs)

model.save("model.h5")

#####################################
##################################### predicter

def predicter(seq, prevChords):
    numericizedMelodySeq = list(seq)
    paddedNumericizedMelodySeq = np.array([numericizedMelodySeq + [0]*(maxSeqLen-len(numericizedMelodySeq))])
    numericizedPrevChords = lblEncoder.transform([chord if chord in lblEncoder.classes_ else "None" for chord in prevChords])
    prediction = model.predict([paddedNumericizedMelodySeq, np.array([numericizedPrevChords])], verbose=False)
    bestPredictionEncoded = np.argmax(prediction) # decides which prediction is highest
    return lblEncoder.inverse_transform([bestPredictionEncoded])[0] # reverses the encoding -> aka un-numericize

for fNum in range(1, 5):
    midi = pretty_midi.PrettyMIDI(f"POP909/00{fNum}/00{fNum}.mid")
    melody_notes = []
    for instrument in midi.instruments:
        if "melody" in instrument.name.lower():
            melody_notes = [note.pitch for note in instrument.notes]
            break
    chords = ["None" for _ in range(4)]

    for i in range(4, len(melody_notes)-4):
        seq = tuple(melody_notes[i:i+4])
        prevChords = chords[i-4:i]
        chords.append(predicter(seq, prevChords))
        
    print(fNum)
    print("Melody:", melody_notes)
    print("Chords:", chords[4:])
    print()