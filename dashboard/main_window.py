"""Main window of the Dashboard."""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from .widgets.example_widget import ExampleWidget


class DashboardWindow(QMainWindow):
    """Main window that hosts all dashboard widgets."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self._init_ui()

    def _init_ui(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(ExampleWidget())
        container.setLayout(layout)
        self.setCentralWidget(container)
