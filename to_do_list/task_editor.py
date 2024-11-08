from PySide6.QtWidgets import  QPushButton,  QVBoxLayout,  QComboBox, QDialog
from PySide6.QtCore import Slot, Signal
class TaskEditor(QDialog):
    signal_name = Signal(int, str)

    def __init__(self, row: int, status: str):
        super().__init__()
        self.initialize_widgets(row, status)
        self.status_combo.setCurrentText(status)
        self.save_button.clicked.connect(self.__on_save_status)


    def initialize_widgets(self, row: int, status: str):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Edit Task Status")

        self.row = row

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])
        

        self.save_button = QPushButton("Save", self)


        layout = QVBoxLayout()
        layout.addWidget(self.status_combo)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.setFixedWidth(150)

    @Slot(Signal)
    def __on_save_status(self):
        """
        Saves the selected status from the status_combo
        
        Args:
            none
        """
        current_text = self.status_combo.currentText()
        self.signal_name.emit(self.row, current_text)

        self.accept()






    

