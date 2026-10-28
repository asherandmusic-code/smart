import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class StudentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Student Marks & Analysis App")
        self.resize(800, 600)
        
        self.central_container = QWidget()
        self.setCentralWidget(self.central_container)
        self.master_layout = QVBoxLayout(self.central_container)
        self.master_layout.setContentsMargins(25, 25, 25, 25)
        self.master_layout.setSpacing(20)
        
        self.welcome_label = QLabel("Welcome back, Student! Ready to track your progress.")
        self.welcome_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #2e3440;
            background-color: #e5e9f0;
            padding: 15px;
            border-radius: 8px;
        """)
        self.master_layout.addWidget(self.welcome_label)
        
        self.card_grid = QGridLayout()
        self.card_grid.setSpacing(15)
    
        self.btn_view = QPushButton("View Marks")
        self.btn_analyze = QPushButton("Analyze")
        self.btn_improve = QPushButton("Improvement Data")
        self.btn_new = QPushButton("New Entry")
        
        card_style = """
            QPushButton {
                background-color: #ffffff;
                color: #2e3440;
                border: 2px solid #d8dee9;
                border-radius: 12px;
                font-size: 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #eceff4;
                border-color: #5e81ac;
            }
        """
        
        self.btn_view.setStyleSheet(card_style)
        self.btn_analyze.setStyleSheet(card_style)
        self.btn_improve.setStyleSheet(card_style)
        self.btn_new.setStyleSheet(card_style)
        
        self.btn_view.setMinimumHeight(120)
        self.btn_analyze.setMinimumHeight(120)
        self.btn_improve.setMinimumHeight(120)
        self.btn_new.setMinimumHeight(120)
        
        self.card_grid.addWidget(self.btn_view, 0, 0)     
        self.card_grid.addWidget(self.btn_analyze, 0, 1)  
        self.card_grid.addWidget(self.btn_improve, 1, 0)  
        self.card_grid.addWidget(self.btn_new, 1, 1)      
        
        self.master_layout.addLayout(self.card_grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec())
