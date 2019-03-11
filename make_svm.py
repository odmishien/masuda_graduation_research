from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib
import os
import numpy
import random

hot_entry_vecs = os.listdir('./hot_vec_doushi')
not_hot_entry_vecs = os.listdir('./normal_vec_doushi')
while len(hot_entry_vecs) < len(not_hot_entry_vecs):
    not_hot_entry_vecs.pop(random.randrange(len(not_hot_entry_vecs)))
features = []
labels = []
target_names = ['class 0', 'class 1']

for hot_entry_vec in hot_entry_vecs:
    features.append(numpy.loadtxt('./hot_vec_doushi/'+hot_entry_vec))
    labels.append(1)
for not_hot_entry_vec in not_hot_entry_vecs:
    features.append(numpy.loadtxt('./normal_vec_doushi/'+not_hot_entry_vec))
    labels.append(0)
for data in features:
    if len(data) != 100:
        index = features.index(data)
        features.remove(data)
        labels.pop(int(index))
# トレーニングデータ:テストデータ を 9:1 に分割
data_train, data_test, label_train, label_test = train_test_split(features, labels, test_size=0.1, random_state=1)

# トレーニングデータから分類器を作成 (Linear SVM)
parameters = [
    # {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['linear'],'tol': [0.001,0.0001], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100,1000], 'class_weight':['balanced']},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100,1000],'class_weight':['balanced']}
    # {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['poly'],'tol': [0.001,0.0001], 'degree': [2, 3, 4], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100],'class_weight':['balanced']},
    # {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['sigmoid'],'tol': [0.001,0.0001], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100],'class_weight':['balanced']}
    ]
estimator = GridSearchCV(SVC(), parameters, cv=2,n_jobs = -1,return_train_score=False)
# estimator = SVC(kernel='rbf',C=10, tol=0.01, gamma='scale', class_weight="balanced")
estimator.fit(data_train, label_train)
# テストデータを分類器に入れる
label_predict = estimator.predict(data_test)
# Accuracy
print(estimator.best_params_)
print(classification_report(label_test, label_predict, target_names=target_names))
# print(accuracy_score(label_test, label_predict))