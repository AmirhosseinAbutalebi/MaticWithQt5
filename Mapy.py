#!/usr/bin/python3
'''
add needed library same panadas for read file csv and xlsx
and pyqt for use qt and ui and sys for access the system commends
'''
import sys
import pandas as pd

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5 import QtGui

# This define just for create sentences and get dataframe and Make changes and return array of sentences
def Matic(dataOfCsv):

    # This variable is made for all sentences because we may have a duplicate sentence
    preparedSentence = []

    '''
    This loop is to move to the number of dataframes and separate
    all the names that are combined with me and us and have meaning
    according to the data frame and consider them as
    sentences and store them in the array.
    '''
    for word in dataOfCsv.iloc[:, 0]:

        for pronoun in ["من", "ما"]:

            existWord = dataOfCsv.iloc[:, 0].str.contains(pronoun + word).any()
            if existWord:

                if pronoun == "ما":
                    preparedSentence.append("به " + pronoun + " نگو " + word +
                                            "," + pronoun + word + " تو نیستیم .")

                else:
                    preparedSentence.append("به " + pronoun + " نگو " + word +
                                            "," + pronoun + word + " تو نیستم .")

    # This array for remove duplicate sentence
    finalSentence = set(preparedSentence)
    return finalSentence


class windowMatic(QMainWindow):

    def __init__(self):
        # Call the parent constructor
        super().__init__()

        # Set the title of the window
        self.setWindowTitle("Matic")
        # Set the width and height of the window
        self.resize(350, 160)
        # Move the position of the window
        self.move(800, 400)

        # Create label for the Path of the file csv or xlsx
        self.lbl1 = QLabel('Write directory of csv or xlsx :', self)
        self.lbl1.setGeometry(10, 0, 300, 50)

        # Create textbox for Path
        self.textbox1 = QTextEdit(self)
        self.textbox1.setGeometry(10, 45, 330, 30)

        # Create push button for start the Matic XD
        self.submit = QPushButton('Start', self)
        self.submit.setGeometry(80, 90, 190, 30)

        # Create label for show the result Operations performed
        self.lblResult = QLabel('', self)
        self.lblResult.setGeometry(110, 110, 200, 50)

        # Call function when the button is clicked
        self.submit.clicked.connect(self.onClicked)

        self.setWindowIcon(QtGui.QIcon('Icon.png'))

        # Display the window
        self.show()

    def onClicked(self):
        # This array has final sentences that we can Extraction from file
        finalSen = []

        # Define variable for get data csv or xlsx and use it for Matic
        pathOfCsvorxlsx = self.textbox1.toPlainText()

        # Read file csv or xlsx
        data = pd.read_excel(pathOfCsvorxlsx)

        # Call function for get sentences
        finalSen = Matic(data)

        # This code for save sentences on file txt
        with open("Result.txt", 'w', encoding='utf-8') as file:
            file.write(finalSen)
        file.close()


        # With this output just we make sure that program do job
        output = "Operations performed"
        self.lblResult.setText(output)


'''
With this code run function
'''
if __name__ == '__main__':

    '''
    The follow code just for test def Matic and
    can remove or tested.
    finalSen = Matic(data)
    print(finalSen)
    '''

    # Create object PyQt application
    app = QApplication([])
    window = windowMatic()
    # Start the event loop for executing the application
    app.exec()
