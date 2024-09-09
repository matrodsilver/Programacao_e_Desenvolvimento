from flask import Flask, redirect, render_template, request, send_from_directory
import pandas as pd
import numpy as np
from numpy import argmax
import tensorflow
from tensorflow import keras
from io import StringIO
from sklearn.model_selection import train_test_split

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Variables to be acessed between multiple pages
data = None        # the data uploaded
inputData = None   # the data that affects the output
outputData = None  # the data affected by the input
results = None     # the output columns
percentage = None  # the acuraccy rate of the model
AImodel = None     # the model configurations
predicted = None   # predicted values
maximums = []      # variable to store the maximum value of each column
minimums = []      # variable to store the minimum value of each column
outputStr2Int = {} # dictionary to convert the output from int to string


# This route is resposible for the main page, where the user can upload a file to be used
# and convert it to a suitable format for the AI model
@app.route("/", methods=["GET", "POST"])
def index():
    global data

    # saves the file data
    if request.method == "POST":
        file = request.files['fileChosen']

        if file.filename == '': # if no file is selected:
            return render_template('error.html', error='No file selected')

        # Using copilot for debuging, it came to my attention that this try block avoids file formatting errors
        try:
            file_content = file.read().decode('utf-8')
        except:
            return render_template('error.html', error='File format not supported')

        # It was also pointed by Copilot that the data could be saved in an stringIO object
        # in order to be converted to a pandas dataframe
        string_io = StringIO(file_content)

        try:
            data = pd.read_csv(string_io)
        except:
            return render_template('error.html', error='CSV file format necessary')

        return redirect("disconsider.html")

    else:
        return render_template("index.html")


# This route renders the page where the user can choose which columns to disconsider from training
@app.route("/disconsider.html", methods=["GET", "POST"])
def disconsider():
    global data

    if request.method == "POST":
        columnsDel = request.form.get(
            "columnsDisconsider").replace(' ', '').split(',') # isolate values

        if columnsDel != ['']:
            for column in columnsDel:
                if column in data: # if the column typed exists:
                    data = data.drop(column, axis=1) # drop this column
                else:
                    return render_template('error.html', error=f'Column ´{column}´ not found')

        return redirect("/result.html")

    else:

        return render_template("disconsider.html", columns=data.columns)


# This route renders the page where the user can choose which column is the output column
# and uses the data acquired to train the model
@app.route("/result.html", methods=["GET", "POST"])
def result():
    global inputData
    global outputData
    global results
    global maximums
    global minimums
    global outputStr2Int
    global percentage
    global AImodel

    if request.method == "POST":
        results = request.form.get("results")

        if results in data: # if the colun exists
            # separate the data in input and ouptut
            inputData = data.drop(results, axis=1) # all the column but the typed one
            outputData = data[results]             # the column typed one

        else:
            return render_template('error.html', error=f'Column ´{results}´ not found')

        # max and min values of each column are stored before normalization
        # to be used by manual testing values
        for i, column in enumerate(inputData):
            maximums.append((max(inputData[column])))
            minimums.append(min(inputData[column]))

        # data normalization
        for i, column in enumerate(inputData):
            inputData[column] = [valor/(maximums[i] - minimums[i])
                                 for valor in inputData[column]]

        # formatting dictionary of results to use as both numbers and strings
        n = 0
        for key in outputData:
            if key not in outputStr2Int:
                outputStr2Int[key] = n
                n += 1

        outputData = outputData.replace(outputStr2Int)
        outputData = pd.DataFrame(outputData)

        # using sklearn library to split the data evenly by occurence into training (85% of the data)
        # and test (15% of the data)
        train, test, answers_train, answers_test = train_test_split(
            inputData, outputData, stratify=outputData, test_size=.15, random_state=5)

        layers = 256  # neurons number

        AImodel = keras.Sequential(
            [
                keras.layers.Input(shape=((len(inputData.columns)),)),
                keras.layers.Dense(layers, activation=tensorflow.nn.selu),
                keras.layers.Dropout(.15),
                keras.layers.Dense(3, activation=tensorflow.nn.softmax)
            ]
        )

        AImodel.compile(
            optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # training the model
        AImodel.fit(train, answers_train, epochs=16, validation_split=0.15)

        # check model's acurracy
        guesses = AImodel.predict(test)

        errors = 0
        for i, value in enumerate(guesses):
            predicted_state = argmax(value)
            actual_state = answers_test[results].iloc[i]  # get value's index
            if predicted_state != actual_state:
                errors += 1

        percentage = 100 - errors/len(test)*100

        # save model
        AImodel.save('model.h5')

        return redirect("/completed.html")

    else:
        return render_template("result.html", columns=data.columns)


@app.route("/completed.html", methods=["GET", "POST"])
def completed():
    global data
    global percentage
    global AImodel
    global outputStr2Int
    global maximus
    global minimus
    global predicted
    global inputData

    if request.method == "POST":
        values_inputed_for_prediction = request.form.get(
            'values').replace(' ', '').split(',')

        try:
            values_inputed_for_prediction = [
                float(value) for value in values_inputed_for_prediction] # try converting values from str to float for prediction

        except:
            return render_template('error.html', error=f'Invalid input')

        try:
            predicted = reshape_and_test(
                values_inputed_for_prediction, AImodel, outputStr2Int, maximums, minimums) # predict inputed value

        except:
            return render_template('error.html', error=f'Invalid input')

        return render_template("completed.html", score=percentage, prediction=predicted, columns=inputData.columns)

    else:
        return render_template("completed.html", score=percentage, prediction="", columns=inputData.columns)


def reshape_and_test(values_test, model, o2s, maxs, mins):
    for i, column in enumerate(inputData):
        values_test[i] = values_test[i]/(maxs[i] - mins[i])

    # **Prova de valores**
    guess = np.array(values_test)
    guess_reshape = np.expand_dims(guess, axis=0)  # Add a batch dimension

    predicted_state = model.predict(guess_reshape)

    predicted_class = argmax(predicted_state[0])  # Assuming categorical output

    return f"Prediction:\n{list(o2s.keys())[predicted_class]}"


@app.route('/download')
def download_file():
    return send_from_directory("", "model.h5", as_attachment=True)