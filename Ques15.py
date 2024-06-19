# Program to read data from a CSV file and print it to the console

import csv

# Reading data from the CSV file
with open('E:\Python&ML\Assignment 1\data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for name in csv_reader:
        print(name)
