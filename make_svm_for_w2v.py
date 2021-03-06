from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import os
import numpy
import random

from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import json
import MeCab

corpusdir = "./model/"
file_w2v_model = corpusdir + "w2v_all_vector200_win5_sgns0.vec"

model = KeyedVectors.load_word2vec_format(
    file_w2v_model, binary=False)
mecab_path = os.getenv("MECAB_NEOLOGD_PATH")
mecab = MeCab.Tagger("-d {0}".format(mecab_path))
hot_masudas = []
masudas = []
hot_vectors = []
vectors = []

for i in range(1, 4995):
    if os.path.exists("data/hot_entry_no_noun_and_adj/masuda_{0}.json".format(i)):
        with open("data/hot_entry_no_noun_and_adj/masuda_{0}.json".format(i), "r") as f:
            hot_masuda_objs = json.load(f)
        for masuda in hot_masuda_objs:
            if masuda["content"] is not None:
                node = mecab.parseToNode(masuda["content"])
                sum_of_vector = 0
                while node:
                    try:
                        sum_of_vector += model[node.surface]
                    except:
                        pass
                    node = node.next
                if type(sum_of_vector) is not int:
                    hot_vectors.append(sum_of_vector)
                    hot_masudas.append(masuda)
    

for i in range(2, 5001):
    with open("data/entry_no_noun_and_adj/masuda_{0}.json".format(i), "r") as f:
        masuda_objs = json.load(f)
    for masuda in masuda_objs:
        if masuda["content"] is not None:
            node = mecab.parseToNode(masuda["content"])
            sum_of_vector = 0
            while node:
                try:
                    sum_of_vector += model[node.surface]
                except:
                    pass
                node = node.next
            if type(sum_of_vector) is not int:
                vectors.append(sum_of_vector)
                masudas.append(masuda)

print("-----文章読み込み終わり-----")
features = []
labels = []
target_names = ['class 0', 'class 1']

for hot_vec in hot_vectors:
    features.append(hot_vec)
    labels.append(1)
for vec in vectors:
    features.append(vec)
    labels.append(0)
# トレーニングデータ:テストデータ を 9:1 に分割
data_train, data_test, label_train, label_test = train_test_split(
    features, labels, test_size=0.1, random_state=1)

# トレーニングデータから分類器を作成 (Linear SVM)
# parameters = [
#     {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['linear'], 'tol': [
#         0.001, 0.0001], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100, 1000], 'class_weight':['balanced']},
#     {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma':[
#         0.001, 0.01, 0.1, 1, 10, 100, 1000], 'class_weight':['balanced']},
#     {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['poly'], 'tol': [0.001, 0.0001],
#         'degree': [2, 3, 4], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100], 'class_weight':['balanced']},
#     {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['sigmoid'], 'tol': [
#         0.001, 0.0001], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100], 'class_weight':['balanced']}
# ]
# estimator = GridSearchCV(SVC(), parameters, cv=2, n_jobs=-1, return_train_score=False, scoring="precision_weighted")
estimator = SVC(kernel='rbf', C=1000, tol=0.01, gamma='scale', class_weight="balanced")
estimator.fit(data_train, label_train)
# テストデータを分類器に入れる
label_predict = estimator.predict(data_test)
# Accuracy
# print(estimator.best_params_, flush=True)
# print(estimator.cv_results_, flush=True)
print(classification_report(label_test, label_predict, target_names=target_names))
print(accuracy_score(label_test, label_predict), flush=True)
