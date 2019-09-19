

import tensorflow as tf

classifier = tf.keras.models.load_model('breast_cancer_classifier.model')

Y_pred = classifier.predict(X_test)
Y_pred = [ 1 if y>=0.5 else 0 for y in Y_pred ]

total = 0
correct = 0
wrong = 0
for i in Y_pred:
  total=total+1
  if(Y_test.at[i,0] == Y_pred[i]):
    correct=correct+1
  else:
    wrong=wrong+1

print("Total " + str(total))
print("Correct " + str(correct))
print("Wrong " + str(wrong))