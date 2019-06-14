import pickle

X = pickle.load(open("X-Cat-Dog-Features.pickle", "rb"))
y = pickle.load(open("y-Cat-Dog-Labels.pickle", "rb"))

print(X[1])