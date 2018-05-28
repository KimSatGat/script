from tkinter import *
from tkinter import font
import tkinter.messagebox

window = Tk()
window.title("전국 등산 정보 조회")
window.geometry("400x600+750+200")

def InitTopText(): #제목
    TempFont = font.Font(window,size=20,weight='bold',family='Consolas')
    MainText = Label(window, font=TempFont,text="전국 등산 정보 조회")
    MainText.pack()
    MainText.place(x=20)

def InitInputLabel(_window):
    global InputLabel
    TempFont = font.Font(_window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(_window, font=TempFont, width=21, borderwidth=12, relief ='ridge')
    InputLabel.pack()
    InputLabel.place(x=10,y=105)
    
def InitSearchButton(_window, _clickAction): #검색 버튼
    TempFont = font.Font(_window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(_window, font = TempFont, text="검색", command=_clickAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def InitMountainButton(): #산정보조회 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="산 정보 조회", command=Mountain_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=110)

def InitTrailPosButton(): #등산로위치정보조회 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="등산로 위치 정보 조회", command=Trail_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=390)

def InitFamousMountainPosPosButton(): #명산등산로조회 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="명산등산로 조회", command=F_Mountain_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=320)

def InitplantsButton(): #숲에사는 식물정보 서비스 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="식물정보 조회", command=plants_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=250)

def InitMountainDetailsButton(): #산 정보 조회(상세검색) 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="산 정보 조회(상세검색)", command=D_Mountain_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=180)

def InitSendButton(): #메일 보내기 버튼
    TempFont = font.Font(window, size=8, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="메일 보내기", command='SearchButtonAction')
    SearchButton.pack()
    SearchButton.place(x=300, y=60)

def InitRenderText(_window):
    global RenderText
    RenderTextScrollbar = Scrollbar(_window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375,y=200)
    TempFont = font.Font(_window, size=10,family='Consolas')
    RenderText = Text(_window, width=35, height=20, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=200)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')

def Mountain_Click(): #산
    m_window = Tk()
    TempFont = font.Font(m_window, size=18, weight='bold', family='Consolas')
    MainText = Label(m_window, font=TempFont, text="산 이름을 입력 해주세요")
    MainText.pack()
    MainText.place(x=20,y=50)
    m_window.title("산 정보 조회")
    m_window.geometry("400x600")
    InitInputLabel(m_window)
    InitSearchButton(m_window, Mountain_Click_Action)
    InitRenderText(m_window)

def Trail_Click(): #등산로
    t_window = Tk()
    TempFont = font.Font(t_window, size=18, weight='bold', family='Consolas')
    MainText = Label(t_window, font=TempFont, text="등산로를 입력 해주세요")
    MainText.pack()
    MainText.place(x=20, y=50)
    t_window.title("등산로 정보 조회")
    t_window.geometry("400x600")
    InitInputLabel(t_window)
    InitSearchButton(t_window)
    InitRenderText(t_window)

def F_Mountain_Click(): #명산
    f_window = Tk()
    TempFont = font.Font(f_window, size=18, weight='bold', family='Consolas')
    MainText = Label(f_window, font=TempFont, text="명산을 입력 해주세요")
    MainText.pack()
    MainText.place(x=20, y=50)
    f_window.title("명산등산로 정보 조회")
    f_window.geometry("400x600")
    InitInputLabel(f_window)
    InitSearchButton(f_window)
    InitRenderText(f_window)

def plants_Click(): #식물
    p_window = Tk()
    TempFont = font.Font(p_window, size=18, weight='bold', family='Consolas')
    MainText = Label(p_window, font=TempFont, text="번호를 입력 해주세요")
    MainText.pack()
    MainText.place(x=20, y=50)
    p_window.title("숲에 사는 식물 정보 조회")
    p_window.geometry("400x600")
    InitInputLabel(p_window)
    InitSearchButton(p_window)
    InitRenderText(p_window)

def D_Mountain_Click(): #산 상세검색
    d_window = Tk()
    TempFont = font.Font(d_window, size=18, weight='bold', family='Consolas')
    MainText = Label(d_window, font=TempFont, text="산 이름을 입력 해주세요")
    MainText.pack()
    MainText.place(x=20, y=50)
    d_window.title("산 정보 조회(상세검색)")
    d_window.geometry("400x600")
    InitInputLabel(d_window)
    InitSearchButton(d_window)
    InitRenderText(d_window)

#def Mountain_Click_Action():
    


def main():
    InitTopText()
    InitMountainButton()
    InitMountainDetailsButton()
    InitplantsButton()
    InitFamousMountainPosPosButton()
    InitTrailPosButton()
    InitSendButton()


main()
window.mainloop()

key = 'xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D'