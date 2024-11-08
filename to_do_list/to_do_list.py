from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QComboBox
from PySide6.QtCore import Slot, Signal
from to_do_list.task_editor import TaskEditor
import csv

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initialize_widgets()
        self.__on_add_task
        self.add_button.clicked.connect(self.__on_add_task)
        self.task_table.cellClicked.connect(self.__on_edit_task)

    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("To-Do List")

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("New Task")

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])

        self.add_button = QPushButton("Add Task", self)

        self.save_button = QPushButton("Save to CSV", self)
        

        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task", "Status"])


        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.status_combo)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_table)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Part 3
    def __load_data(self, file_path: str):
        """
        Reads data from the .csv file provided.
        Calls the __add_table_row method (to be implemented) 
        for each row of data.
        Args:
            file_path (str): The name of the file (including relative path).
        """
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            header = next(reader)  
            for row in reader:
                self.__add_table_row(row)
    
    def __add_table_row(self, row_data):
        """
        Remove the pass statement below to implement this method.
        """
        pass
    
    def __save_to_csv(self):
        """
        Saves the QTable data to a file.
        """
        file_path = 'output/todos.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(["Task", "Status"])

    @Slot(Signal)
    def __on_add_task(self):
        """
        Adds a new task to the task table with input data

        Args:
            none
        """

        task = self.task_input.text()
        status_combo = self.status_combo.currentText()

        try:
            if task:
                table_count = self.task_table.rowCount()
                self.task_table.insertRow(table_count)

                task_item = QTableWidgetItem(task)
                status_item = QTableWidgetItem(status_combo)

                self.task_table.setItem(table_count, 0, task_item)
                self.task_table.setItem(table_count, 1, status_item)

                self.status_label.setText(f"Added task: {task}")
            else:
                self.status_label.setText("Please enter a task and select its status.")
        except ValueError as e:
            self.status_label.setText(e)

    @Slot(Signal)
    def __on_edit_task(self, row, column):
        """
        Edits the status of the task in the task table

        Args:
            row (int): row that has been clicked on
            column (int): column that has been clicked on
        """
        current_status = self.task_table.item(row, 1).text()

        editor = TaskEditor(row, current_status)

        editor.signal_name.connect(self.__update_task_status)
    
        if editor.exec_():
            new_status = editor.status_combo.currentText()
            self.task_table.item(row, 1).setText(new_status)
        
    @Slot(Signal)
    def __update_task_status(self, row: int, new_status: str):
        """
        Updates the status of a task in the task table

        Args:
            row (int): The row of the task to update in the task_table
            new_status (str): The new status value to set for the task
        """
        status_item = QTableWidgetItem(new_status)
        self.task_table.setItem(row, 1, status_item) 
        
        self.status_label.setText(f"Task status updated to: {new_status}")
