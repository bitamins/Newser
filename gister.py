import sys
import logging
from newser import Newser
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QListView, QTableView, QTextEdit, QGridLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class CustomItemModel(QStandardItemModel):
    def __init__(self,parent=None):
        super(CustomItemModel,self).__init__()
        self.setColumnCount(5)
        pass

class CustomListView(QTableView):
    def __init__(self,parent=None):
        super(CustomListView,self).__init__()
        self.model = CustomItemModel(self)


class CustomListItem(QStandardItem):
    def __init__(self,parent=None):
        super(CustomListItem,self).__init__()
        pass
        # self.initLayout()

    def initLayout(self):
        self.vLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.vLayout)

    def setValues(self,symDict):
        for key,val in symDict.items():
            tempWidget = QtGui.QLabel()
            tempWidget.setText(val)
            self.vLayout.addwidget(tempWidget)

class ParameterGrid(QWidget):
    def __init__(self,parent=None):
        super(ParameterGrid,self).__init__(parent=parent)
        # self.initVars()
        self.parent=parent
        self.initUI()

    def initVars(self):
        self.symbol = ''
        self.start = ''
        self.end = ''

    def initUI(self):
        listLabel = QLabel('Symbol(s): ')
        self.symbolEntry = QLineEdit()
        self.symbolEntry.textChanged.connect(self.updateSymbol)
        startLabel = QLabel('Amount of News: ')
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
        self.parent.setSymbol(text)

    def updateStart(self,text):
        self.parent.setStart(text)

    def updateEnd(self,text):
        self.parent.setEnd(text)

class NewsList(CustomListView):
    def __init__(self,parent=None):
        super(NewsList,self).__init__(parent=parent)
        self.initUI()
        self.stocks = ['aapl','googl','ntfx','fb','amzn','tsla','intc','nvda','ibm','amd','chgg','msft','vsat','mu','el','aeiq']
        self.fillModel('aapl',5)
        self.setModel(self.model)

        # self.show()

    def update(self,symbol,num):
        if symbol in self.stocks:
            self.fillModel(symbol,num)

    def fillModel(self,symbol,num):
        newsList = Newser.getStockNewsDict(self=Newser,symbol=symbol,num=num)
        self.model.clear()
        for row,item in enumerate(newsList):
            itemList=[]
            col=0
            print('\n')
            print(row)
            for key,val in item.items():
                print(key)
                newItem = CustomListItem()
                newItem.setText(str(val))
                self.model.setItem(row,col,newItem)
                col+=1

    def initUI(self):
        self.model = CustomItemModel(self)

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

    def updateNews(self,symbol,num):
        self.News.update(symbol,num)

    def setSymbol(self,text):
        self.symbol=text
        self.updateNews(self.symbol,self.start)

    def setStart(self,text):
        self.start=text
        self.updateNews(self.symbol,self.start)
        # self.updateNews()

    def setEnd(text):
        self.end=text
        # self.updateNews()

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
