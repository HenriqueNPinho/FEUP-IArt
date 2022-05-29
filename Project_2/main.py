import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpt
import sklearn as sk
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier



if __name__ == '__main__':
    dataset = pd.read_csv('data.csv', delimiter=';')
    dataset_corr = dataset.corr()
    print(dataset_corr)
    print()
    print(dataset.head())
    print()
    print(dataset.describe())
    print()
    print(dataset.info())

    columns = dataset.columns

    col_list = list(columns)
    col_list = col_list.drop()
    new_col_list = col_list[:-1]

    all_inputs = dataset[new_col_list].values

    all_labels = dataset['Target'].values

    (training_inputs,
    testing_inputs,
    training_classes,
    testing_classes) = train_test_split(all_inputs, all_labels, test_size=0.25, random_state=1)


    # Create the classifier
    decision_tree_classifier = DecisionTreeClassifier()

    # Train the classifier on the training set
    decision_tree_classifier.fit(training_inputs, training_classes)

    # Validate the classifier on the testing set using classification accuracy
    print(decision_tree_classifier.score(testing_inputs, testing_classes))