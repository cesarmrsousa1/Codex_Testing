"""Entry point for the dashboard application."""

from .app import DashboardApp


def main():
    app = DashboardApp()
    return app.run()


if __name__ == "__main__":
    main()
