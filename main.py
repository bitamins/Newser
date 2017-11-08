from gister import MainLayout
import logging
import logging.config
from PyQt5 import QtWidgets
import sys

def createLogger(filename):
    logging.config.fileConfig(filename)
    logger = logging.getLogger(__name__)
    print('one')
    logger.debug("Initialized Handler: SUCCESS")

if __name__ == "__main__":
    createLogger('logging.conf')
    app = QtWidgets.QApplication(sys.argv)
    main =  MainLayout()
    main.show()
    sys.exit(app.exec_())
