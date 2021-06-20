"""
Name : Tejas Bhausaheb Borde
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
       
        self.setWindowTitle("TIC-TAC-TOE") 
  
        self.setGeometry(100, 100,  
                         300, 560) 

        self.Ui()

        self.show()
    
    
    def Ui(self):
        self.turn=0
        self.times=0
        self.push_list=[]
        
        for i in range(3):
            temp=[]
            for j in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        x = 90
        y = 90
        
        for i in range(3): 
            for j in range(3): 
  
                
                self.push_list[i][j].setGeometry(x*i + 20,  
                                                 y*j + 20, 
                                                 80, 80) 
  
                
                self.push_list[i][j].setFont(QFont('Times', 17)) 
                self.push_list[i][j].setStyleSheet("QPushButton\n"
                                 "{\n"
                                 "    \n"
                                 
                                 "border-radius : 10% ;"
                                 "border : 1px solid black;"
                                 "}")
               
                self.push_list[i][j].clicked.connect(self.action_called)
        
        
        self.label = QLabel(self) 
        self.label.setGeometry(20, 300, 260, 60)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "border-radius : 12% ;"
                                 "}") 
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Times', 15)) 
        
        
        self.label1 = QLabel(self) 
        self.label1.setGeometry(20, 380, 260,60)
        self.label1.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "border-radius : 12% ;"
                                 "}") 
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont('Times', 15)) 
        self.label1.setText("X-Turn") 
        
        reset_game = QPushButton("Reset-Game", self) 
  
        
        reset_game.setGeometry(50, 470, 200, 50) 
        reset_game.setFont(QFont('Times', 15)) 
        reset_game.setStyleSheet("QPushButton\n"
                                 "{\n"
                                 "    \n"
                                 "    background-color: rgb(194, 188, 255);\n"
                                 "border-radius : 12% ;"
                                 "border : 2px solid black;"
                                 "}")
  
        
        reset_game.clicked.connect(self.reset_game)
        
        
    def reset_game(self): 
  
       
        self.turn = 0
        self.times = 0
  
        
        self.label.setText("") 
  
         
        for buttons in self.push_list: 
            for button in buttons:           
                button.setEnabled(True) 
                button.setText("")
                
        self.label1.setText("X-Turn")        
    def action_called(self): 
  
        self.times += 1
        button = self.sender() 
        
        if(self.turn==0):
            button.setStyleSheet("QPushButton\n"
                                 "{\n"
                                 "    \n"
                                 "border-radius : 10% ;"
                                 "border : 1px solid black;"
                                 "  color: rgb(255, 83, 49);\n"
                                 "}")
        else:
            button.setStyleSheet("QPushButton\n"
                                 "{\n"
                                 "    \n"
                                 "border-radius : 10% ;"
                                 "border : 1px solid black;"
                                 "  color: rgb(0, 0, 0);\n"
                                 "}")
            
        button.setEnabled(False) 
  
        if self.turn == 0: 
            button.setText("X") 
            self.label1.setText("O-Turn Now")
            self.turn = 1
        else: 
            button.setText("O") 
            self.label1.setText("X-Turn Now")
            self.turn = 0
  

        winner= self.who_wins() 
          
        
  
        # if winner is decided 
        if winner== True: 
            # if current chance is 0 
            if self.turn == 0: 
                # O has won 
                text = "O Won!!!"
            # X has won 
            else: 
                text = "X Won!!!"
            self.label1.setText("")
            # disabling all the buttons 
            for buttons in self.push_list: 
                for push in buttons: 
                    push.setEnabled(False) 
  
        # if winner is not decided 
        # and total times is 9 
        elif self.times == 9: 
            text = "Match Drawn!!!"
            self.label1.setText("")
        else:
            text=""
        # setting text to the label 
        self.label.setText(text)  
        
        
    def who_wins(self): 
  
        # checking if any row crossed 
        for i in range(3): 
            if self.push_list[0][i].text() == self.push_list[1][i].text() and self.push_list[0][i].text() == self.push_list[2][i].text() and self.push_list[0][i].text() != "": 
                return True
  
        # checking if any column crossed 
        for i in range(3): 
            if self.push_list[i][0].text() == self.push_list[i][1].text() and self.push_list[i][0].text() == self.push_list[i][2].text() and self.push_list[i][0].text() != "": 
                return True
  
        # checking if diagonal crossed 
        if self.push_list[0][0].text() == self.push_list[1][1].text() and self.push_list[0][0].text() == self.push_list[2][2].text()  and self.push_list[0][0].text() != "": 
            return True
  
        # if other diagonal is crossed 
        if self.push_list[0][2].text() == self.push_list[1][1].text() and self.push_list[1][1].text() == self.push_list[2][0].text() and self.push_list[0][2].text() != "": 
            return True
  
  
        #if nothing is crossed 
        return False
        

if __name__ == "__main__":  
    App = QApplication(sys.argv) 
  

    window = Window() 
  
 
    sys.exit(App.exec()) 
