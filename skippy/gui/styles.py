######################################################################
### From https://github.com/gmarull/qtmodern
######################################################################

from PyQt5 import QtGui

from skippy.gui import utils, themes

import skippy.config

import os

_STYLESHEET = os.path.join(skippy.config.RESOURCES_FOLDER, "stylesheet", "style.qss")
""" str: Main stylesheet. """


def _apply_base_theme(app):
    """Apply base theme to the application.
    Args:
            app (QApplication): QApplication instance.
    """

    app.setStyle("Fusion")

    with open(_STYLESHEET) as stylesheet:
        app.setStyleSheet(stylesheet.read())


def dark():
    """Apply Dark Theme to the Qt application instance."""
    app = utils.getApplication()

    darkPalette = QtGui.QPalette()

    themes.DARK_THEME.apply(darkPalette)

    app.setPalette(darkPalette)

    _apply_base_theme(app)


def light():
    """Apply Light Theme to the Qt application instance."""
    app = utils.getApplication()

    lightPalette = QtGui.QPalette()

    themes.LIGHT_THEME.apply(lightPalette)

    app.setPalette(lightPalette)

    _apply_base_theme(app)
