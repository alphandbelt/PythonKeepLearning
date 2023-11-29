import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

if __name__ == "__main__":
    # 1.
    app = QApplication(sys.argv)

    # 2.
    window = QWidget()
    layout = QVBoxLayout()

    # 3.
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("mydatabase.db")
    db.open()


    # 4.
    model = QSqlTableModel()
    model.setTable("mytable")
    model.select()

    table_view = QTableView()
    table_view.setModel(model)

    #
    layout.addWidget(table_view)
    window.setLayout(layout)
    window.show()

    #
    sys.exit(app.exec_())
