import sys
import logging
from newser import Newser
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QListView, QTableView, QTextEdit, QGridLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class CustomListModel(QStandardItemModel):
    def __init__(self,parent=None):
        super(CustomListModel,self).__init__()
        pass

class CustomListView(QListView):
    def __init__(self,parent=None):
        super(CustomListView,self).__init__()
        self.model = CustomListModel(self)


class CustomListItem(QStandardItem):
    def __init__(self,parent=None):
        super(CustomListItem,self).__init__()
        pass

class ParameterGrid(QWidget):
    def __init__(self,parent=None):
        super(ParameterGrid,self).__init__(parent=parent)
        # self.initVars()
        self.initUI()

    def initVars(self):
        self.symbol = ''
        self.start = ''
        self.end = ''

    def initUI(self):
        listLabel = QLabel('Symbol(s): ')
        self.symbolEntry = QLineEdit()
        self.symbolEntry.textChanged.connect(self.updateSymbol)
        startLabel = QLabel('Start Date: ')
        self.startEntry = QLineEdit()
        self.startEntry.textChanged.connect(self.updateStart)
        endLabel = QLabel('End Date:')
        self.endEntry = QLineEdit()
        self.endEntry.textChanged.connect(self.updateEnd)


        mainLayout = QGridLayout()
        mainLayout.addWidget(listLabel,0,0)
        mainLayout.addWidget(self.symbolEntry,0,1)
        mainLayout.addWidget(startLabel,1,0)
        mainLayout.addWidget(self.startEntry,1,1)
        mainLayout.addWidget(endLabel,2,0)
        mainLayout.addWidget(self.endEntry,2,1)

        self.setLayout(mainLayout)

    def updateSymbol(self,text):
        pass
        # self.parent.setSymbol(text)

    def updateStart(self,text):
        pass
        # self.parent.setStart(text)

    def updateEnd(self,text):
        pass
        # self.parent.setEnd(text)

class NewsList(CustomListView):
    def __init__(self,parent=None):
        super(NewsList,self).__init__(parent=parent)
        self.initUI()
        self.fillModel()
        # self.show()

    def fillModel(self):
        newsList = Newser.getStockNewsDict(self=Newser,symbol='aapl')

        for item in newsList:
            newItem = CustomListItem()#item['source'])
            newItem.setText(item['source'])
            self.model.appendRow(newItem)

        self.setModel(self.model)


    def initUI(self):
        self.model = CustomListModel(self)

class DataPlot(QWidget):
    def __init__(self):
        super().__init__()
    pass

class MainLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initVars()
        self.initObjects()
        self.initLayout()
        print('end')

    # def setSymbol(text):
    #     self.symbol=text
    # def setStart(text):
    #     self.start=text
    # def setEnd(text):
    #     self.end=text

    def initLayout(self):
        self.grid.addWidget(self.Parameters,0,0)
        self.grid.addWidget(self.News,1,0,1,2)
        self.grid.addWidget(self.Plot,0,1)

    def initObjects(self):
        self.Parameters = ParameterGrid(self)
        self.News = NewsList(self)
        self.Plot = DataPlot()
        self.grid = QGridLayout()
        self.CentralLayout = QWidget()
        self.CentralLayout.setLayout(self.grid)
        self.setCentralWidget(self.CentralLayout)

    def initVars(self):
        self.symbol = ''
        self.start = ''
        self.end = ''

    def initUI(self):
        self.resize(600,600)
        self.move(300,300)
        self.setWindowTitle('Newser')
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main =  MainLayout()
    main.show()

    # w = QtWidgets.QWidget()
    # w.resize(250,150)
    # w.move(300,300)
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec_())
