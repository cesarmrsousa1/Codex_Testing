"""Application module for the Dashboard."""

from PyQt5.QtWidgets import QApplication


class DashboardApp:
    """Encapsulates the QApplication to allow easier testing and extension."""

    def __init__(self):
        self.app = QApplication([])

    def run(self, window_factory=None):
        """Starts the Qt application.

        Parameters
        ----------
        window_factory : callable, optional
            A factory function that returns a QMainWindow instance. This allows
            customizing the window used for the dashboard.
        """
        if window_factory is None:
            from .main_window import DashboardWindow

            window_factory = DashboardWindow

        window = window_factory()
        window.show()
        return self.app.exec_()
