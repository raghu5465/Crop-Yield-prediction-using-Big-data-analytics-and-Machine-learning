Crop Yield Prediction Using Big Data Analytics And Machine Learning
This is a Readme file on how to run the given Crop Yield Prediction

Installation
Use the package manager to install the pyspark library pip install pyspark

pip install pyspark
Libraries used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree 
Usage
#Importing Spark Session
pyspark.sql import SparkSession

#Creates a dataframe 
crop_data_spark = spark.createDataFrame(crop_data_pd)

#Imports the library Sting Indexer from Pyspark
from pyspark.ml.feature import StringIndexer

Running the Code
Open the crop_predicition.py

Import the particular libraries as mentioned in the Readme file

Run the crop_prediciton.py notebook first then run the crop_prediciton.py GUI for the resulting crop prediction model