from tkinter import font
from tkinter import *



def InitButton1(window):  # 산정보조회 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, text="산 정보 조회", command=Button1_Click)
    SearchButton.pack()
    SearchButton.place(x=50, y=110)

def Button1_Click():  # 산
    global  b1_window
    b1_window = Tk()
    TempFont = font.Font(b1_window, size=18, weight='bold', family='Consolas')
    TempFont_B = font.Font(b1_window, size=12, weight='bold', family='Consolas')
    MainText = Label(b1_window, font=TempFont, text="산 이름을 입력 해주세요")
    MainText.pack()
    MainText.place(x=20, y=50)
    b1_window.title("산 정보 조회")
    b1_window.geometry("430x600")

    global InputLabel
    TempFont = font.Font(b1_window, size=15, weight='bold', family='Consolas')
    InputLabel = Entry(b1_window, font=TempFont, width=21, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

    TempFont_B = font.Font(b1_window, size=12, weight='bold', family='Consolas')
    Button1Action = Button(b1_window, font=TempFont_B, text="검색", command=Button1_Click_Action)
    Button1Action.pack()
    Button1Action.place(x=330, y=110)

def Button1_Click_Action():
    import urllib.request
    from xml.dom.minidom import parse, parseString
    from urllib.request import urlopen
    from urllib.parse import quote
    import tkinter.messagebox

    global num3
    #name = str(InputLabel.get())
    test = quote("북한산")
    key = "xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D"
    url = urlopen("http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI?searchWrd="+test+"&ServiceKey="+key)

    data = url.read()

    f = open("M_Info.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("M_Info.xml")
    mntiadd = doc.getElementsByTagName("mntiadd") #소재지
    mntihigh = doc.getElementsByTagName("mntihigh") #높이
    mntiname = doc.getElementsByTagName("mntiname") #산 이름
    mntisummary = doc.getElementsByTagName("mntisummary") #산 정보
    mntidetails = doc.getElementsByTagName("mntidetails") #산 상세정보

    _mntiadd = []
    _mntihigh = []
    _mntiname = []
    _mntisummary = []
    _mntidetails = []

    num3 = mntiadd.length

    if num3 == 0:
        tkinter.messagebox.showwarning("알림", "정보가 최신화 되지 않았습니다.")
    else:
        tmp1 = mntiadd
        tmp2 = mntihigh
        tmp3 = mntiname
        tmp4 = mntisummary
        tmp5 = mntidetails

        _mntiadd.append(tmp1)
        _mntihigh.append(tmp2)
        _mntiname.append(tmp3)
        _mntisummary.append(tmp4)
        _mntidetails.append(tmp5)



        def InitRenderText():
            global RenderText

            RenderTextScrollbar = Scrollbar(b1_window)
            RenderTextScrollbar.pack()
            RenderTextScrollbar.place(x=375, y=200)
            TempFont = font.Font(b1_window, size=10, family='Consolas')
            RenderText = Text(b1_window, width=49, height=30, borderwidth=12, relief='ridge',
                                yscrollcommand=RenderTextScrollbar.set)
            RenderText.pack()
            RenderText.place(x=10, y=157)
            RenderTextScrollbar.config(command=RenderText.yview)
            RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "소재지 : ")
            RenderText.insert(INSERT, _mntiadd[0])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "높이 : ")
            RenderText.insert(INSERT, _mntihigh[0])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산 이름 : ")
            RenderText.insert(INSERT, _mntiname[0])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산 정보 : ")
            RenderText.insert(INSERT, _mntisummary[0])
            RenderText.insert(INSERT, "\n\n")
            RenderText.configure(state='disabled')

        InitRenderText()
