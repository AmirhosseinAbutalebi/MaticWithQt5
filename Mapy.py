#!/usr/bin/python3
'''
add needed library same panadas for read file csv and xlsx
and pyqt for use qt and ui and sys for access the system commends
'''
import sys
import pandas as pd

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# define variable for get data csv or xlsx and use it for Matic
data = pd.read_excel(r'Farhang_farsi.xlsx')

# this array has final sentences that we can Extraction from file
finalSen = []

# this define just for create sentences and get dataframe and Make changes and return array of sentences
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


finalSen = Matic(data)
'''
The following code is also for testing sentences
You can leave a comment
print(finalSen)
'''

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110,85)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("Matic")
    widget.show()
    sys.exit(app.exec_())

'''
With this code run function
'''
if __name__ == '__main__':
    finalSen = Matic(data)
    window()
