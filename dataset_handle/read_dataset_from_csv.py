import pandas as pd
import os

def read_csv_from_dataset0():
    #Replace with your path to dataset folder
    path = "../../data/dataset0"
    count = 0
    for file in os.listdir(path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == ".csv":
            print("Read csv file:", path + "/" + file, "\n")
            data = pd.read_csv(path + "/" + file)
            data.drop('Id', inplace=True, axis=1)
            data.drop('RatingDist4', inplace=True, axis=1)
            data.drop('RatingDistTotal', inplace=True, axis=1)
            data.drop('PublishMonth', inplace=True, axis=1)
            data.drop('PublishDay', inplace=True, axis=1)
            data.drop('Publisher', inplace=True, axis=1)
            data.drop('RatingDist2', inplace=True, axis=1)
            data.drop('RatingDist5', inplace=True, axis=1)
            data.drop('ISBN', inplace=True, axis=1)
            data.drop('RatingDist3', inplace=True, axis=1)
            data.drop('RatingDist1', inplace=True, axis=1)
            print(data)
            data.to_csv("dataset/dataset0_" + str(count) + ".csv")
            count += 1

def read_csv_from_dataset1():
    # Replace with your path to dataset folder
    path = "../../data/dataset1"
    count = 0
    for file in os.listdir(path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == ".csv":
            print("Read csv file:", path + "/" + file, "\n")
            data = pd.read_csv(path + "/" + file)
            data.drop('bookID', inplace=True, axis=1)
            data.drop('isbn', inplace=True, axis=1)
            data.drop('isbn13', inplace=True, axis=1)
            data.drop('text_reviews_count', inplace=True, axis=1)
            data.drop('publisher', inplace=True, axis=1)
            print(data)
            data.to_csv("dataset/dataset1_" + str(count) + ".csv")
            count += 1

def read_csv_from_dataset2():
    # Replace with your path to dataset folder
    path = "../../data/dataset2"
    count = 0
    for file in os.listdir(path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == ".csv":
            print("Read csv file:", path + "/" + file, "\n")
            data = pd.read_csv(path + "/" + file)
            data.drop('book_edition', inplace=True, axis=1)
            data.drop('book_isbn', inplace=True, axis=1)
            data.drop('book_format', inplace=True, axis=1)
            data.drop('book_review_count', inplace=True, axis=1)
            data.drop('image_url', inplace=True, axis=1)
            print(data)
            data.to_csv("dataset/dataset2_" + str(count) + ".csv")
            count += 1

def read_csv_from_dataset3():
    # Replace with your path to dataset folder
    path = "../../data/dataset3"
    count = 0
    for file in os.listdir(path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == ".csv":
            print("Read csv file:", path + "/" + file, "\n")
            data = pd.read_csv(path + "/" + file)
            data.drop('image', inplace=True, axis=1)
            data.drop('previewLink', inplace=True, axis=1)
            data.drop('publisher', inplace=True, axis=1)
            data.drop('infoLink', inplace=True, axis=1)
            print(data)
            data.to_csv("dataset/dataset3_" + str(count) + ".csv")
            count += 1

def read_csv_from_dataset4():
    # Replace with your path to dataset folder
    path = "../../data/dataset4"
    count = 0
    for file in os.listdir(path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == ".csv":
            print("Read csv file:", path + "/" + file, "\n")
            data = pd.read_csv(path + "/" + file)
            data.drop('asin', inplace=True, axis=1)
            data.drop('soldBy', inplace=True, axis=1)
            data.drop('imgUrl', inplace=True, axis=1)
            data.drop('productURL', inplace=True, axis=1)
            data.drop('price', inplace=True, axis=1)
            data.drop('isKindleUnlimited', inplace=True, axis=1)
            data.drop('category_id', inplace=True, axis=1)
            print(data)
            data.to_csv("dataset/dataset4_" + str(count) + ".csv")
            count += 1

read_csv_from_dataset4()

# data = pd.read_csv('../../data/dataset4/kindle_data-v2.csv')
#
# print("Original 'input.csv' CSV Data: \n")
# print(data.columns)