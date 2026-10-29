import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QGridLayout, QLabel, QPushButton, QStackedWidget)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon 

class StudentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Student Marks & Analysis App")
        self.resize(800, 600)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.dashboard_page = QWidget()
        self.init_dashboard_ui()
        self.stacked_widget.addWidget(self.dashboard_page)
        
        self.new_entry_page = QWidget()
        self.init_sub_page_ui(self.new_entry_page, "New Marks Entry Form", "#0165fc")
        self.stacked_widget.addWidget(self.new_entry_page)

        self.view_marks_page = QWidget()
        self.init_sub_page_ui(self.view_marks_page, "View Student Marks", "#00cc00")
        self.stacked_widget.addWidget(self.view_marks_page)

        self.analyze_page = QWidget()
        self.init_sub_page_ui(self.analyze_page, "Performance Analysis", "#ffed29")
        self.stacked_widget.addWidget(self.analyze_page)

        self.improve_page = QWidget()
        self.init_sub_page_ui(self.improve_page, "Improvement Data & Insights", "#ff6e00")
        self.stacked_widget.addWidget(self.improve_page)

    def init_dashboard_ui(self):
        self.master_layout = QVBoxLayout(self.dashboard_page)
        self.master_layout.setContentsMargins(100, 25, 100, 25)
        self.master_layout.setSpacing(20)
        
        self.welcome_label = QLabel("Welcome back, Student! Ready to track your progress.")
        self.welcome_label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #2e3440;
            border: 3px solid #d8dee9;
            background-color: #e5e9f0;
            padding: 15px;
            border-radius: 8px;
            qproperty-alignment: 'AlignCenter';
        """)
        self.welcome_label.setFixedHeight(75)
        self.welcome_label.setFixedWidth(800)
        self.master_layout.addWidget(self.welcome_label, alignment = Qt.AlignmentFlag.AlignHCenter)
        
        self.card_grid = QGridLayout()
        self.card_grid.setSpacing(50)

        self.btn_new = QPushButton("New Entry")
        self.btn_view = QPushButton("View Marks")
        self.btn_analyze = QPushButton("Analyze")
        self.btn_improve = QPushButton("Improvement Data")

        #Blue - New Entry
        card_style1 = """
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #0165fc, 
                    stop:1 #b3e5fc
                );
                color: #333333;
                border: 2px solid #d8dee9;
                border-radius: 12px;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #0165fc, 
                    stop:1 #b3e5fc
                );
                border-color: #5e81ac;
            }
        """

        #Green - View Marks       
        card_style2 = """
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #00cc00, 
                    stop:1 #88e788
                );
                color: #333333;
                border: 2px solid #d8dee9;
                border-radius: 12px;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color:  qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #00cc00, 
                    stop:1 #88e788
                );
                border-color: #5e81ac;
            }
        """

        #Yellow - Analysis
        card_style3 = """
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ffed29, 
                    stop:1 #f9e79f
                );
                color: #333333;
                border: 2px solid #d8dee9;
                border-radius: 12px;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ffed29, 
                    stop:1 #f9e79f
                );
                border-color: #5e81ac;
            }
        """

        #Orange - Improvement
        card_style4 = """
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ff6e00, 
                    stop:1 #ffd3a5
                );
                color: #333333;
                border: 2px solid #d8dee9;
                border-radius: 12px;
                font-size: 22px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ff6e00, 
                    stop:1 #ffd3a5
                );
                border-color: #5e81ac;
            }
        """

        self.btn_new.setStyleSheet(card_style1)
        self.btn_view.setStyleSheet(card_style2)
        self.btn_analyze.setStyleSheet(card_style3)
        self.btn_improve.setStyleSheet(card_style4)

        self.btn_new.setMaximumSize(400, 200)
        self.btn_view.setMaximumSize(400, 200)
        self.btn_analyze.setMaximumSize(400, 200)
        self.btn_improve.setMaximumSize(400, 200)

        self.card_grid.addWidget(self.btn_new, 0, 0)
        self.card_grid.addWidget(self.btn_view, 0, 1)     
        self.card_grid.addWidget(self.btn_analyze, 1, 0)  
        self.card_grid.addWidget(self.btn_improve, 1, 1)

        self.btn_new.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.btn_view.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.btn_analyze.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.btn_improve.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        
        self.master_layout.addLayout(self.card_grid)

    def init_sub_page_ui(self, page_widget, title_text, accent_color):
        layout = QVBoxLayout(page_widget)
        layout.setContentsMargins(50, 50, 50, 50)
        
        btn_back = QPushButton("← Back to Dashboard")
        btn_back.setFixedSize(180, 40)
        btn_back.setStyleSheet("""
            QPushButton {
                background-color: #e5e9f0;
                color: #2e3440;
                border: 2px solid #d8dee9;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d8dee9;
            }
        """)
        btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignLeft)
        
        title = QLabel(title_text)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"""
            font-size: 24px;
            font-weight: bold;
            color: #2e3440;
            background-color: #ffffff;
            border-left: 6px solid {accent_color};
            padding: 20px;
            border-radius: 8px;
        """)
        layout.addWidget(title)
        
        placeholder = QLabel("Content and tools for this section will go here...")
        placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        placeholder.setStyleSheet("font-size: 16px; color: #4c566a; margin-top: 40px;")
        layout.addWidget(placeholder)
        
        layout.addStretch()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentApp()
    window.show()
    sys.exit(app.exec())
