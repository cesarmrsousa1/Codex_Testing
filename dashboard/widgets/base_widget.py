"""Base classes for dashboard widgets."""

from PyQt5.QtWidgets import QWidget


class DashboardWidget(QWidget):
    """Base class for widgets displayed in the dashboard."""

    def refresh(self):
        """Refreshes the widget data. Override in subclasses."""
        raise NotImplementedError
