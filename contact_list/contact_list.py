from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot, Signal


class ContactList(QMainWindow):
    """
    Contact List Class (QMainWindow). Provides users a 
    way to manage their contacts.
    """
    def __init__(self):
        """
        Initializes a Contact List window in which 
        users can add and remove contact data.
        """
        super().__init__()
        self.__initialize_widgets()    
        self.add_button.clicked.connect(self.__on_add_contact)  
        self.remove_button.clicked.connect(self.__on_remove_contact)  


    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot(Signal)
    def __on_add_contact(self):
        """
        adds name and phone number as a contact
        
        Args:
            none
        """
        name = self.contact_name_input.text()
        phone = self.phone_input.text()

        len(name.strip())
        len(phone.strip())

        try:
            if name and phone: 
                row_position = self.contact_table.rowCount()
                self.contact_table.insertRow(row_position)
                name_item = QTableWidgetItem(name)
                phone_item = QTableWidgetItem(phone)
                self.contact_table.setItem(row_position, 0, name_item)
                self.contact_table.setItem(row_position, 1, phone_item)
                self.status_label.setText(f"Added contact: {name}")
            else:
                self.status_label.setText("Please enter a contact name and phone number")
        except ValueError as e:
            self.status_label.setText(e)

    @Slot(Signal)
    def __on_remove_contact(self):
        """
        Removes the selected contact from the contact table.
    
        Args:
            none
        """

        selected_row = self.contact_table.currentRow()

        try:
            if selected_row >= 0:
                reply = QMessageBox.question(self, "Remove Contact", "Are you sure you want to remove the selected contact?", 
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.contact_table.removeRow(selected_row)
                    self.status_label.setText("Contact removed.")
            else:
                self.status_label.setText("Please select a row to be removed")
        except ValueError as e:
            self.status_label.setText(e)







