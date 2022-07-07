import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import Text
import os
import json

userleng = ""
userfilepath = ""

#init gui
root = tk.Tk()
root.title('Conver Charm Json to text')
root.resizable(False, False)
root.geometry('600x250')
guidetexteng="""
Step one: Choose the language you would like to output
Step two: Click on select Json to convert your Charm json to txt file

!! When the converter finish it will save in the same location
   with the same name in txt format !!
   

"""
guidetextzht = """
第一步: 選擇你的輸出語言
第二步: 點選按此選擇Json並執行轉換，轉換器會自動把護石Json變為txt檔案

!! 當轉換器完成以後將會以txt格式自動把Json在同一路徑儲存成一樣的檔案名稱 !!


"""

guidetextjpn="""
ステップ1: 使用する言語を選択してください。
ステップ2: 「Jsonファイルを選択」をクリックし、json形式のお守りデータを選択したらtxt形式に変換されます。

!! 変換されたお守りデータは変換前と同じ場所に同じ名前で保存されます。!!
   
~ 日本語に翻訳したL4Mon69感謝します ~

"""

#Gui action
def select_file():
    filetypes = (
        ('Json files', '*.json'),
        ('All files', '*.*')
    )
    userfilepath = fd.askopenfilename(
        title='Convert Json',
        initialdir='/',
        filetypes=filetypes)
    conver_json_to_string(userfilepath)


def menu_updated_eng():
    global userleng
    userleng = "eng"
    mb.configure(text="English")
    open_button.configure(text="Click to select Json and convert")
    text_box.config(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', guidetexteng)
    text_box.config(state='disabled')

def menu_updated_zht():
    global userleng
    userleng = "zht"
    mb.configure(text="中文(zh-CHT)")
    open_button.configure(text="按此選擇Json檔案並執行轉換")
    text_box.config(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', guidetextzht)
    text_box.config(state='disabled')

def menu_updated_jpn():
    global userleng
    userleng = "jpn"
    mb.configure(text="日本語")
    open_button.configure(text="Jsonファイルを選択")
    text_box.config(state='normal')
    text_box.delete(1.0, 'end')
    text_box.insert('end', guidetextjpn)
    text_box.config(state='disabled')

def conver_json_to_string(userfilepath):
    # start script
    print("Read file path = " + userfilepath)
    datafile = open(userfilepath)
    if userleng == "zht":
        skilljson = open("leng/skills_zht.json" , encoding="utf8")
    elif userleng == "eng":
        skilljson = open("leng/skills_eng.json" , encoding="utf8")
    elif userleng == "jpn":
        skilljson = open("leng/skills_jpn.json" , encoding="utf8")


    data = json.load(datafile)
    skilltable = json.load(skilljson)
    head, tail = os.path.split(userfilepath)
    name = tail.split(".")
    outputtxt = head + "/" + name[0] + ".txt"
    f= open(outputtxt, "w" , encoding="utf8")

    for i in data:
        SkillID = i["Skills"]
        Skill1 = skilltable[str(SkillID[0])]
        print("Skill1 = "+Skill1)
        Skill2 = skilltable[str(SkillID[1])]
        print("Skill2 = " + Skill2)
        SkillLevel1 = str(i["SkillLevels"][0])
        SkillLevel2 = str(i["SkillLevels"][1])
        Slot = str(i["Slots"][0])+","+str(i["Slots"][1])+","+str(i["Slots"][2])
        Rarity = str(i["Rarity"])
        out = Skill1+","+SkillLevel1+","+Skill2+","+SkillLevel2+","+Slot+","+Rarity+"\n"
        f.write(out)
        print(out)

    f.close()
    datafile.close()
    skilljson.close()

    # script finish, close window
    os.startfile(outputtxt)
    root.destroy


# Gui placment
mb= ttk.Menubutton(root, text="Language")
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu
mb.menu.add_command(label="English", command=menu_updated_eng)
mb.menu.add_command(label="中文(zh-CHT)", command=menu_updated_zht)
mb.menu.add_command(label="日本語", command=menu_updated_jpn)
mb.pack()
open_button = ttk.Button(
    root,
    text='Click to select Json',
    command=select_file
)
open_button.pack()
text_box = Text(root,height=200,width=600)
text_box.pack(expand=True)
text_box.insert('end', guidetexteng)
text_box.config(state='disabled')

#set default to english
mb.menu.invoke(0)

#start GUI
root.mainloop()

