import librosa, glob, os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

emotions = ['neutral','calm','happy','sad','angry','fearful','disgust','suprised']

def extract(filename):
    with librosa.load(filename, sr=None) as (X, sr):
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sr,n_mfcc=40).T, axis=0)
    return mfccs

def load(size=0.2):
    x, y = [], []
    for file in glob.glob("dataset/Actor_*/*.wav"):
        filename = os.path.basename(file)
        emotion = emotions[int(filename.split("-")[2])]
        feature = extract(file)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=size, random_state=7, train_size=size)

x_train, x_test, y_train, y_test = load()

model = MLPClassifier(hidden_layer_sizes=(100,), learning_rate='adaptive', max_iter=500)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
print(f"Accuracy:{accuracy * 100:.2f}")