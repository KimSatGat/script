import UI
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
    url = "http://openapi.forest.go.kr/openapi/service/trailInfoService/getforestservice?ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("M_Info.xml", "wb")
    f.write(data)
    f.close()