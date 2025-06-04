"""An example dashboard widget."""

from PyQt5.QtWidgets import QLabel, QVBoxLayout

from .base_widget import DashboardWidget


class ExampleWidget(DashboardWidget):
    """Simple widget showing a greeting message."""

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        self.label = QLabel("Bem-vindo ao dashboard!")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def refresh(self):
        """Update the widget. No-op for now."""
        pass
