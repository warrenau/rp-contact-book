# -*- coding: utf-8 -*-
# rpcontacts/main.py

"""This module provides RP Contacts application."""

import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window

def main():
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv)
    # connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # create the main window
    win = Window()
    win.show()
    # run the event loop
    sys.exit(app.exec())