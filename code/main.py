from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import numpy as np
import pre_process
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from my_confusion_matrix import MyConfusionMatrix
#from pandas_ml import ConfusionMatrix


# Folder with the various subfolders
raw_data_folder = Path("../data/derive")
# Foldre with all of the new processed files
proc_data_folder = Path("../data/processed")

# Check if we've already processed the data, pre-process if not
try:
    _ = next(proc_data_folder.iterdir())
except StopIteration:
    # No files in preprocessed, so generate them
    pre_process.pre_process(raw_data_folder, proc_data_folder)

# Use scikit learn's count vectorizer to convert text files into X matrix by word frequency
corpus = proc_data_folder.iterdir()
vectorizer = CountVectorizer(input='filename',token_pattern=r'[a-zA-Z]+-?[a-zA-Z]+')
X = vectorizer.fit_transform(corpus)

# Generate y by iterating through files and extracting file names. Tested to make sure order is same with X matrix
y = np.array([])
for file in proc_data_folder.iterdir():
    # labels are stored in the filename after the dash
    label = int(file.stem.split('-')[1])
    # Not most efficient way but we don't expect crazy numbers of files so append should be fine
    y = np.append(y,[label])
    
# Start confusion matrix
labels = [515647,515648,515672,515673,515674]
my_cm = MyConfusionMatrix(labels) # Made my own because sklearn and pandas-ml have issues

# Create, train, and evalute the model
repeats = 10 # Adjust to better estimate accuracy
acc = 0 # Accumulator for accuracy
for i in range(repeats):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    #clf = BernoulliNB(alpha=0.045,fit_prior=False) # Uncomment for a Bernoulli NB model
    clf = MultinomialNB(alpha=0.065,fit_prior=False)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc += np.mean(y_pred != y_test)
    # Add results to confusion matrix
    my_cm.inputResults(y_test, y_pred)
	
acc = acc/repeats

# Print results
print("The accuracy is: " + str(acc))
print(my_cm.getMatrix())




