# -*- coding: utf-8 -*-
from tkinter import font
from tkinter import *



def InitButton4(window):  # 산불예방서비스 버튼
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    Button4 = Button(window, font=TempFont, text="산불예방서비스 조회", command=Button4_Click)
    Button4.pack()
    Button4.place(x=50, y=180)

def Button4_Click():  # 산불예방서비스
    global  b4_window
    b4_window = Tk()
    TempFont = font.Font(b4_window, size=18, weight='bold', family='Consolas')
    TempFontex = font.Font(b4_window,size=12,weight='bold', family='Consolas')
    MainText = Label(b4_window, font=TempFont, text="날짜와 시간을 입력해주세요")
    exText = Label(b4_window, font=TempFontex, text="(예:2013122410)")
    MainText.pack()
    exText.pack()
    MainText.place(x=20, y=50)
    exText.place(x=414,y=55)
    b4_window.title("산불예방서비스 조회")
    b4_window.geometry("600x800")

    global InputLabel
    TempFont = font.Font(b4_window, size=15, weight='bold', family='Consolas')
    InputLabel = Entry(b4_window, font=TempFont, width=21, borderwidth=12, relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

    TempFont_B = font.Font(b4_window, size=12, weight='bold', family='Consolas')
    Button4Action = Button(b4_window, font=TempFont_B, text="검색", command=Button4_Click_Action)
    Button4Action.pack()
    Button4Action.place(x=330, y=110)

def Button4_Click_Action():
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import tkinter.messagebox
    global num3
    date = str(InputLabel.get())
    key = "xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D"
    url = "http://openapi.forest.go.kr/openapi/service/forestDisasterService/fFireOpenAPI?ffDt="+date+"&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("FP_Info.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("FP_Info.xml")
    ffclscd = doc.getElementsByTagName("ffclscd")
    ffclsnm = doc.getElementsByTagName("ffclsnm")
    ffdt = doc.getElementsByTagName("ffdt")
    ffid = doc.getElementsByTagName("ffid")
    ffquot = doc.getElementsByTagName("ffquot")

    num3 = ffclscd.length



    if num3 == 0:
        tkinter.messagebox.showwarning("알림", "정보가 최신화 되지 않았습니다.")
    else:
        _ffclscd = []
        _ffclsnm = []
        _ffdt = []
        _ffid = []
        _ffquot = []

        index = 0
        while index < num3:
            tmp1 = str(ffclscd[index].firstChild.data)
            tmp2 = str(ffclsnm[index].firstChild.data)
            tmp3 = str(ffdt[index].firstChild.data)
            tmp4 = str(ffid[index].firstChild.data)
            tmp5 = str(ffquot[index].firstChild.data)

            if tmp4 == "11680":
                tmp4 = "서울특별시 강남구"
            elif tmp4 == "11110":
                tmp4 = "서울특별시 종로구"
            elif tmp4 == "11740":
                tmp4 = "서울특별시 강동구"
            elif tmp4 == "11305":
                tmp4 = "서울특별시 강북구"
            elif tmp4 == "11500":
                tmp4 = "서울특별시 강서구"
            elif tmp4 == "11620":
                tmp4 = "서울특별시 관악구"
            elif tmp4 == "11215":
                tmp4 = "서울특별시 광진구"
            elif tmp4 == "11530":
                tmp4 = "서울특별시 구로구"
            elif tmp4 == "11545":
                tmp4 = "서울특별시 금천구"
            elif tmp4 == "11350":
                tmp4 = "서울특별시 노원구"
            elif tmp4 == "11320":
                tmp4 = "서울특별시 도봉구"
            elif tmp4 == "11230":
                tmp4 = "서울특별시 동대문구"
            elif tmp4 == "11590":
                tmp4 = "서울특별시 동작구"
            elif tmp4 == "11440":
                tmp4 = "서울특별시 마포구"
            elif tmp4 == "11410":
                tmp4 = "서울특별시 서대문구"
            elif tmp4 == "11650":
                tmp4 = "서울특별시 서초구"
            elif tmp4 == "11200":
                tmp4 = "서울특별시 성동구"
            elif tmp4 == "11290":
                tmp4 = "서울특별시 성북구"
            elif tmp4 == "11710":
                tmp4 = "서울특별시 송파구"
            elif tmp4 == "11470":
                tmp4 = "서울특별시 양천구"
            elif tmp4 == "11560":
                tmp4 = "서울특별시 영등포구"
            elif tmp4 == "11170":
                tmp4 = "서울특별시 용산구"
            elif tmp4 == "11380":
                tmp4 = "서울특별시 은평구"
            elif tmp4 == "11140":
                tmp4 = "서울특별시 중구"
            elif tmp4 == "11260":
                tmp4 = "서울특별시 중랑구"
            elif tmp4 == "26440":
                tmp4 = "부산광역시 강서구"
            elif tmp4 == "26410":
                tmp4 = "부산광역시 금정구"
            elif tmp4 == "26710":
                tmp4 = "부산광역시 기장군"
            elif tmp4 == "26290":
                tmp4 = "부산광역시 남구"
            elif tmp4 == "26170":
                tmp4 = "부산광역시 동구"
            elif tmp4 == "26260":
                tmp4 = "부산광역시 동래구"
            elif tmp4 == "26230":
                tmp4 = "부산광역시 부산진구"
            elif tmp4 == "26530":
                tmp4 = "부산광역시 사상구"
            elif tmp4 == "26380":
                tmp4 = "부산광역시 사하구"
            elif tmp4 == "26140":
                tmp4 = "부산광역시 서구"
            elif tmp4 == "26500":
                tmp4 = "부산광역시 수영구"
            elif tmp4 == "26470":
                tmp4 = "부산광역시 연제구"
            elif tmp4 == "26200":
                tmp4 = "부산광역시 영도구"
            elif tmp4 == "26110":
                tmp4 = "부산광역시 중구"
            elif tmp4 == "26350":
                tmp4 = "부산광역시 해운대구"


            _ffclscd.append(tmp1)
            _ffclsnm.append(tmp2)
            _ffdt.append(tmp3)
            _ffid.append(tmp4)
            _ffquot.append(tmp5)
            index += 1

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(b4_window)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)
        TempFont = font.Font(b4_window, size=10, family='Consolas')
        RenderText = Text(b4_window, width=49, height=30, borderwidth=12, relief='ridge',
                         yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        for i in range(num3):
            RenderText.insert(INSERT, "\n(")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, ")")
            RenderText.insert(INSERT, "산불위험구분 : ")
            RenderText.insert(INSERT, _ffclsnm[i])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산불위험예보일자 : ")
            RenderText.insert(INSERT, _ffdt[i])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "행정기관 : ")
            RenderText.insert(INSERT, _ffid[i])
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산불위험지수 : ")
            RenderText.insert(INSERT, _ffquot[i])
            RenderText.insert(INSERT, "\n\n")
            i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
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
    b1_window.geometry("600x800")

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
    name = quote(str(InputLabel.get()))
    key = "xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D"
    url = urlopen("http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI?searchWrd="+name+"&ServiceKey="+key)

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

    num3 = mntiadd.length

    if num3 == 0:
        tkinter.messagebox.showwarning("알림", "정보가 최신화 되지 않았습니다.")
    else:
        _mntiadd = []
        _mntihigh = []
        _mntiname = []
        _mntisummary = []
        _mntidetails = []

        index = 0
        while index < num3:
            tmp1 = str(mntiadd[index].firstChild.data)
            tmp2 = str(mntihigh[index].firstChild.data)
            tmp3 = str(mntiname[index].firstChild.data)
            tmp4 = str(mntisummary[index].firstChild.data)
            tmp5 = str(mntidetails[index].firstChild.data)

            _mntiadd.append(tmp1)
            _mntihigh.append(tmp2)
            _mntiname.append(tmp3)
            _mntisummary.append(tmp4)
            _mntidetails.append(tmp5)
            index += 1



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

            for i in range(num3):
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "소재지 : ")
                RenderText.insert(INSERT, _mntiadd[i])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "높이 : ")
                RenderText.insert(INSERT, _mntihigh[i])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "산 이름 : ")
                RenderText.insert(INSERT, _mntiname[i])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "산 정보 : ")
                RenderText.insert(INSERT, _mntisummary[i])
                RenderText.insert(INSERT, "\n\n")
                RenderText.insert(INSERT, "산 상세정보 : ")
                RenderText.insert(INSERT, _mntidetails[i])
                RenderText.insert(INSERT, "\n\n")
                i += 1
                RenderText.configure(state='disabled')
        InitRenderText()

window = Tk()
window.title("전국 등산 정보 조회")
window.geometry("400x600+750+200")

InitButton1(window)
InitButton4(window)

window.mainloop()