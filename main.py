import database.models as models
import gui.login as login
from gui.main_window import MainWindow

if __name__ == "__main__":
    models.create_table()
    models.insert_test_user()
    login.create_login_window()
