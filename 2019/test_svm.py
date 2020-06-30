from sklearn.externals import joblib
from sklearn.metrics import classification_report, accuracy_score

import numpy
import sys

estimator = joblib.load('./hot_or_not_estimator.pkl')
entry = [numpy.loadtxt('./hot_vec/'+sys.argv[1])]
test_pred = estimator.predict(entry)
print(classification_report(test_labels, test_pred))
print(accuracy_score(test_labels, test_pred))