#!/usr/bin/python3
import sys
import pandas as pd

data = pd.read_excel(r'Farhang_farsi.xlsx')


def Matic(dataOfCsv):
    preparedSentence = []
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
    finalSentence = set(preparedSentence)
    return finalSentence


'''from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Testpyqt5')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1> Hello pyqt5</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())
'''
