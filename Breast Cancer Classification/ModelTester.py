import tensorflow as tf
import pandas as pd

classifier = tf.keras.models.load_model('breast_cancer_classifier.model')
X_test = pd.read_csv("F:\\Datasets\\Breast Cancer Classification\\xtest.csv", header=None)
Y_test = pd.read_csv("F:\\Datasets\\Breast Cancer Classification\\ytest.csv", header=None)

Y_pred = classifier.predict(X_test)
Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred ]

total = 0
correct = 0
wrong = 0
for i in range(len(Y_pred)):
  total=total+1
  if(Y_test.at[i,0] == Y_pred[i]):
    correct=correct+1
  else:
    wrong=wrong+1

print("Total " + str(total))
print("Correct " + str(correct))
print("Wrong " + str(wrong))