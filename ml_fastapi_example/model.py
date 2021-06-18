
from os import EX_CANTCREAT
import pandas as pd
from scipy.sparse import data
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisModel:
    def __init__(self):
        '''
            Creates a simple model to solve the Iris Classification Problems
        '''
        self.df = pd.read_csv('iris.csv')
        self.model_name = 'iris_model.pkl'
        try:
            self.clf = joblib.load(self.model_name)
        except Exception as _:
            self.clf = self._train_model()
            joblib.dump(self.clf, self.model_name)

    def _train_model(self):
        '''
            Trains a RandomForestClassifier
            to solve the Iris problem
        '''
        X = self.df.drop('species', axis=1)
        y = self.df['species']
        clf = RandomForestClassifier()
        return clf.fit(X, y)

    def predict(self, sepal_length, sepal_width, petal_length, petal_width):
        data_input = [[sepal_length, sepal_width, petal_length, petal_width]]
        data_pred = self.clf.predict(data_input)
        prob = self.clf.predict_proba(data_input).max()
        return data_pred[0], prob
