import time 
import pandas as pd
from sklearn.model_selection import train_test_split

from whatlies.language import BytePairLanguage, UniversalSentenceLanguage, SentenceTFMLanguage, CountVectorLanguage
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


df = pd.read_csv("toxicity-train.csv.zip").replace({"\n", ""})

def clean_text(txt_col):
    return txt_col.str.replace(r'\n', " ")

def to_train_df(dataf):
    dataf = dataf.copy() 
    dataf['bad'] = dataf[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].sum(axis=1)
    dataf['label'] = ['toxic' if b else 'fine' for b in dataf['bad'] != 0]
    dataf['text'] = clean_text(dataf['comment_text'])
    return dataf[['text', 'label']]



train_df = df.pipe(to_train_df)[:20000]
x_train, x_test, y_train, y_test = train_test_split(list(train_df['text']), train_df['label'])


lang_use = UniversalSentenceLanguage("large")
lang_bp  = BytePairLanguage("en", dim=300, vs=200_000)
lang_brt = SentenceTFMLanguage('distilbert-base-nli-stsb-mean-tokens')


models = {}
results = []

def get_name(o):
    return o.__class__.__name__
    
for lang in [CountVectorizer(), lang_bp, lang_use, lang_brt]:
    for mod in [SVC(class_weight='balanced'), LogisticRegression(solver='liblinear', class_weight='balanced')]:
        pipe = Pipeline([
            ("feat", lang),
            ("mod", mod)
        ])
        models[get_name(lang), get_name(mod)] = pipe
        tic = time.time()
        pipe.fit(list(x_train), y_train)
        toc = time.time() 
        print(f"report for {get_name(lang), get_name(mod)}")
        train_time = toc - tic
        print(f"train time: {train_time}")
        tic = time.time()
        y_pred = pipe.predict(x_test)
        toc = time.time()
        print(f"pred time: {toc - tic}")
        d = classification_report(y_test, y_pred, output_dict=True)
        data = {
            'lang': get_name(lang), 
            'mod': get_name(mod),
            'precision': d['toxic']['precision'], 
            'recall': d['toxic']['recall'],
            'pred-time': toc - tic,
            'train-time': train_time
            
        }
        results.append(data)
        print(classification_report(y_test, y_pred))

pd.DataFrame(results).to_csv("results.csv", index=False)
