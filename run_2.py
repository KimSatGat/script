import UI
import code2institutions
from tkinter import *
from tkinter import font


def Mountain_Click_Action():
    import urllib.request
    from xml.dom.minidom import parse, parseString
    import tkinter.messagebox
    global num3
    g_Tk_son3 = Tk()
    g_Tk_son3.title("산정보 조회")
    g_Tk_son3.geometry('400x600+900+130')
    TempFont = font.Font(g_Tk_son3, size=17, weight='bold', family='Consolas')
    MainText = Label(g_Tk_son3, font=TempFont, text="산정보 조회")
    MainText.pack()
    MainText.place(x=14, y=60)
    TempFont2 = font.Font(g_Tk_son3, size=8, weight='bold', family='Consolas')

    key = "xMZX0AJTnhtS5z%2BxQ0HF%2FIZF6tYHuGHB3NIuE%2BSsZDt7WQOZfxhTMoopvM1AH7VlwXFSZgmCjUnxszbjM58YsA%3D%3D"
    url = "http://openapi.forest.go.kr/openapi/service/forestDisasterService/fFireOpenAPI?ffDt=2013122410&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("M_Info.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("M_Info.xml")
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

        RenderTextScrollbar = Scrollbar(g_Tk_son3)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(g_Tk_son3, size=10, family='Consolas')
        RenderText = Text(g_Tk_son3, width=49, height=30, borderwidth=12, relief='ridge',
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