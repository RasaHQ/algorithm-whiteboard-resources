import time
import pathlib

import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline, make_pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer

from memo import memlist, memfunc, memfile, time_taken, grid

from sklearn.model_selection import train_test_split
from whatlies.language import FasttextLanguage, UniversalSentenceLanguage

ft_lang = FasttextLanguage("../whatlies/embeddings/cc.en.300.bin")
use_lang = UniversalSentenceLanguage()


def generate_model(emb, model='lr'):
    models = {
        'lr': LogisticRegression(solver='liblinear', class_weight="balanced"),
    }
    if emb == "use":
        union = FeatureUnion([
            ('cv', CountVectorizer()),
            ('cv-ngram', CountVectorizer(analyzer='char', ngram_range=(2, 3))),
            ('use_lang', use_lang)
        ])
        mod = make_pipeline(union, models[model])
    elif emb == "ft":
        union = FeatureUnion([
            ('cv', CountVectorizer()),
            ('cv-ngram', CountVectorizer(analyzer='char', ngram_range=(2, 3))),
            ('ft', ft)
        ])
        mod = make_pipeline(union, models[model])
    elif emb == "cv-ngram":
        union = FeatureUnion([
            ('cv', CountVectorizer()),
            ('cv-ngram', CountVectorizer(analyzer='char', ngram_range=(2, 3))),
        ])
        mod = make_pipeline(union, models[model])
    return mod


@memfile('benchmark-logs.jsonl')
@time_taken()
def experiment(dataset, model, emb="cv", train_size=100, test_size=1000):
    df = (pd.read_csv(datasets[dataset])
          .loc[lambda d: ~d['text'].isna()]
          .loc[lambda d: ~d['label'].isna()])

    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'],
                                                        test_size=test_size,
                                                        stratify=df['label'],
                                                        random_state=42)

    # Everything must be a list when the input is text.
    X_train, y_train = list(X_train[:train_size]), list(y_train[:train_size])
    X_test, y_test = list(X_test), list(y_test)

    # Generate and train the model
    mod = generate_model(emb=emb, model=model)
    mod.fit(X_train, y_train)

    # Gather stats
    y_train_pred = mod.predict(X_train)
    tic = time.time()
    y_test_pred = mod.predict(X_test)
    toc = time.time()
    return {
        'accuracy_test': np.mean(y_test == y_test_pred),
        'accuracy_train': np.mean(y_train == y_train_pred),
        'pred_time': toc - tic
    }


settings = grid(
    dataset=["scope"],
    model=["lr"],
    emb=["ft", "use", "cv-ngram"],
    train_size=np.arange(500, 9500, 500),
    test_size=[4000]
)

for s in settings:
    experiment(**s)
