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
    import tkinter.messagebox
    global num3
    #name = str(InputLabel.get())

    key = "xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D"
    url = "http://openapi.forest.go.kr/openapi/service/trailInfoService/getforeststoryservice?mntnNm=가리왕산&serviceKey="+key
    data = urllib.request.urlopen(url).read()
    f = open("M_Info.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("M_Info.xml")
    crcmrsghtnginfodscrt = doc.getElementsByTagName("crcmrsghtnginfodscrt") #주변관광정보설명
    crcmrsghtnginfoetcdscrt = doc.getElementsByTagName("crcmrsghtnginfoetcdscrt") #산정보주변관광정보기타코스설명
    #hndfmsmtnmapimageseq = doc.getElementsByTagName("hndfmsmtnmapimageseq") #100대명산 지도명(이미지) jpg파일
    hndfmsmtnslctnrson = doc.getElementsByTagName("hndfmsmtnslctnrson") #100대명산 선정이유
    #mntnattchimageseq = doc.getElementsByTagName("mntnattchimageseq") #산정보이미지
    mntnid = doc.getElementsByTagName("mntnid") #산코드
    mntninfodscrt = doc.getElementsByTagName("mntninfodscrt") #산정보개관
    mntninfodtlinfocont = doc.getElementsByTagName("mntninfodtlinfocont") #상세정보내용
    mntninfohght = doc.getElementsByTagName("mntninfohght") #산정보 높이
    mntninfopoflc = doc.getElementsByTagName("mntninfopoflc") #산정보소재지
    mntnnm = doc.getElementsByTagName("mntnnm") #산이름
    mntnsbttlinfo = doc.getElementsByTagName("mntnsbttlinfo") #산정보부제
    pbtrninfodscrt = doc.getElementsByTagName("pbtrninfodscrt") #대중교통정보설명

    num3 = crcmrsghtnginfodscrt.length

    if num3 == 0:
        tkinter.messagebox.showwarning("알림", "정보가 최신화 되지 않았습니다.")
    else:
        tmp2 = str(crcmrsghtnginfodscrt.firstChild.data)
        tmp3 = str(crcmrsghtnginfoetcdscrt.firstChild.data)
        #tmp4 = str(hndfmsmtnmapimageseq[index].firstChild.data)
        tmp5 = str(hndfmsmtnslctnrson.firstChild.data)
        #tmp6 = str(mntnattchimageseq[index].firstChild.data)
        tmp7 = str(mntnid.firstChild.data)
        tmp8 = str(mntninfodscrt.firstChild.data)
        tmp9 = str(mntninfodtlinfocont.firstChild.data)
        tmp10 = str(mntninfohght.firstChild.data)
        tmp11 = str(mntninfopoflc.firstChild.data)
        tmp12 = str(mntnnm.firstChild.data)
        tmp13 = str(mntnsbttlinfo.firstChild.data)
        tmp14 = str(pbtrninfodscrt.firstChild.data)


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
            RenderText.insert(INSERT, "산불위험구분 : ")
            RenderText.insert(INSERT, tmp11)
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산불위험예보일자 : ")
            RenderText.insert(INSERT, tmp10)
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "행정기관 : ")
            RenderText.insert(INSERT, tmp5)
            RenderText.insert(INSERT, "\n\n")
            RenderText.insert(INSERT, "산불위험지수 : ")
            RenderText.insert(INSERT, tmp12)
            RenderText.insert(INSERT, "\n\n")
            RenderText.configure(state='disabled')

        InitRenderText()
