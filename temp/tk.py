# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import font
import csv
import os




def read_csv_to_list(filename):
    """
    讀取 CSV 檔案到列表

    Args:
    filename (str): 檔案名稱

    Returns:
    list: 讀取到的資料，每一行為一個列表
    """

    

    data = []
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    else:
        # 如果檔案不存在，創建一個新的檔案 (可以加入預設的表頭)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['user_id', 'username', 'email'])  # 範例表頭
    return data

csv01 = read_csv_to_list('user.csv')
csv02 = read_csv_to_list('package.csv')

#=========================全域==============================
root = tk.Tk()
root.title('sono超音波檢查紀錄單')        # 設定標題
root.iconbitmap('001.ico')  # 設定 icon ( 格式限定 .ico )



root.minsize(720, 750)    # 設定視窗最小為 200x200
root.maxsize(720, 750)    # 設定視窗最大為 500x500

root.resizable(False, False)   # 設定 x 方向和 y 方向都不能縮放

window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度

print(window_height)
print(window_width)


height = 720
width = 750

left = int((window_width - height)/2)       # 計算左上 x 座標
top = int((window_height - width)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')



#=========================內容==============================

date_= datetime.datetime.now()
date_=date_.strftime("%Y-%m-%d ")

#-----------------Frame-----------------
frame01 = tk.Frame(root)                  # 操作者
frame02 = tk.Frame(root)                  # 姓名
frame03 = tk.Frame(root)                  # 性別
frame04 = tk.Frame(root)                  # 套組

frame05 = tk.Frame(root,bd=1, relief="solid")                  #內文

#~~~~~~~~~~腹部超音波~~~~~~~~~~~
lableframe01 = tk.LabelFrame(frame05, text='',)
lableframe01.pack(fill='x')

var01 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton01 = tk.Checkbutton(lableframe01, text="腹部超音波", variable=var01,font=('微軟正黑體',13,'bold'))
checkbutton01.pack(side="left", anchor="nw")

var01_01 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton01_01 = tk.Checkbutton(lableframe01, text="無明顯異常", variable=var01_01,font=('微軟正黑體',10,))
checkbutton01_01.pack(side="left", anchor="center")

var01_02 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton01_02 = tk.Checkbutton(lableframe01, text="已告知回診", variable=var01_02,font=('微軟正黑體',10,))
checkbutton01_02.pack(side="left", anchor="center")

var01_03 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton01_03 = tk.Checkbutton(lableframe01, text="備註", variable=var01_03,font=('微軟正黑體',10,))
checkbutton01_03.pack(side="left", anchor="center")

#~~~~~~~~~~肝臟~~~~~~~~~~~
lableframe02 = tk.LabelFrame(frame05, text='肝臟',font=('微軟正黑體',10,))
lableframe02.pack(side="left",anchor="w", padx=5, pady=5,fill='y')

varcheckbutton_lableframe02_01 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_01 = tk.Checkbutton(lableframe02, text="脂肪肝(輕 中度以上)", variable=varcheckbutton_lableframe02_01,font=('微軟正黑體',10,))
checkbutton_lableframe02_01.pack(side="top", anchor="w")

varcheckbutton_lableframe02_02 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_02 = tk.Checkbutton(lableframe02, text="肝囊腫", variable=varcheckbutton_lableframe02_02,font=('微軟正黑體',10,))
checkbutton_lableframe02_02.pack(side="top", anchor="w")

varcheckbutton_lableframe02_03 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_03 = tk.Checkbutton(lableframe02, text="疑似血管瘤", variable=varcheckbutton_lableframe02_03,font=('微軟正黑體',10,))
checkbutton_lableframe02_03.pack(side="top", anchor="w")

varcheckbutton_lableframe02_04 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_04 = tk.Checkbutton(lableframe02, text="疑似脂肪分布不均", variable=varcheckbutton_lableframe02_04,font=('微軟正黑體',10,))
checkbutton_lableframe02_04.pack(side="top", anchor="w")

varcheckbutton_lableframe02_05 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_05 = tk.Checkbutton(lableframe02, text="肝內鈣化", variable=varcheckbutton_lableframe02_05,font=('微軟正黑體',10,))
checkbutton_lableframe02_05.pack(side="top", anchor="w")

varcheckbutton_lableframe02_06 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_06 = tk.Checkbutton(lableframe02, text="肝實質疾病", variable=varcheckbutton_lableframe02_06,font=('微軟正黑體',10,))
checkbutton_lableframe02_06.pack(side="top", anchor="w")

varcheckbutton_lableframe02_07 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe02_07 = tk.Checkbutton(lableframe02, text="(高/同/低)回音疾病", variable=varcheckbutton_lableframe02_07,font=('微軟正黑體',10,))
checkbutton_lableframe02_07.pack(side="top", anchor="w")



#~~~~~~~~~~膽囊~~~~~~~~~~~
lableframe03 = tk.LabelFrame(frame05, text='膽囊')
lableframe03.pack(side="left",anchor="n", padx=5, pady=5)

varcheckbutton_lableframe03_01 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe03_01 = tk.Checkbutton(lableframe03, text="切除術後　　　　　", variable=varcheckbutton_lableframe03_01,font=('微軟正黑體',10,))
checkbutton_lableframe03_01.pack(side="top", anchor="w")

varcheckbutton_lableframe03_02 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe03_02 = tk.Checkbutton(lableframe03, text="結石", variable=varcheckbutton_lableframe03_02,font=('微軟正黑體',10,))
checkbutton_lableframe03_02.pack(side="top", anchor="w")

entry_checkbutton_lableframe03_02 = tk.Entry(lableframe03,width=5)  # 放入單行輸入框
entry_checkbutton_lableframe03_02.place(x=55,y=31)

label_lableframe03_01 = tk.Label(lableframe03, text='mm')
label_lableframe03_01.place(x=90,y=31)

varcheckbutton_lableframe03_03 = tk.IntVar()  # 用來儲存 Checkbutton 的狀態
checkbutton_lableframe03_03 = tk.Checkbutton(lableframe03, text="結石(多發性)", variable=varcheckbutton_lableframe03_03,font=('微軟正黑體',10,))
checkbutton_lableframe03_03.pack(side="top", anchor="w")





#c = tk.Label(lableframe01, text='CCC').pack(side="right")
#lableframe01_lableframe01 = tk.LabelFrame(lableframe01, text='test', padx=10, pady=10)
#a = tk.Label(lableframe01_lableframe01, text='AAA').pack()
#b = tk.Label(lableframe01_lableframe01, text='BBB').pack()
#c = tk.Label(lableframe01_lableframe01, text='CCC').pack()
#lableframe01_lableframe01.pack()






#-----------------label-----------------
label01 = tk.Label(root, text=' 超音波檢查紀錄單　',font=('微軟正黑體',25,'bold'))
label02 = tk.Label(root, text=f'檢查日期：{date_}　',font=('微軟正黑體',13))
label03 = tk.Label(frame01, text='操作者：',font=('微軟正黑體',13))
label03.pack(side="left")
label04 = tk.Label(frame02, text=' 姓名/ID：',font=('微軟正黑體',13),anchor='e')
label04.pack(side="left")
label05 = tk.Label(frame04, text='套組：', font=('微軟正黑體',13))
label05.pack(side="left")

#-----------------下拉式選單-----------------
optionList01 = csv01   # 選項
value01 = tk.StringVar()                                        # 取值
value01.set('選取操作者')
menu01 = tk.OptionMenu(frame01, value01, *optionList01)                # 第二個參數是取值，第三個開始是選項，使用星號展開
menu01.config(width=10)
menu01.pack(side="right")

optionList02 = csv02   # 選項
value02 = tk.StringVar()                                        # 取值
value02.set('選取套組')
menu02 = tk.OptionMenu(frame04, value02, *optionList02)                # 第二個參數是取值，第三個開始是選項，使用星號展開
menu02.config(width=10)
menu02.pack(side="right")

#-----------------entry-----------------
entry1_1 = tk.Entry(frame02)  # 放入單行輸入框
entry1_1.pack(side="right")

#-----------------單選-----------------
val = tk.StringVar()

radio_btn1 = tk.Radiobutton(frame03, text='男性',variable=val, value='Apple')
radio_btn1.pack(side="left")
radio_btn1.select()  # 搭配 select() 方法選取 radio_btn1

radio_btn2 = tk.Radiobutton(frame03, text='女性',variable=val, value='Banana')
radio_btn2.pack(side="right")



label01.grid(column=0, row=0)  # 放在 (0,0)
#label01.grid_propagate(0)   讓布局大小不變

label02.grid(column=1, row=0)  # 放在 (1,0)
frame01.grid(column=2, row=0,sticky=tk.W) 


frame02.grid(column=0, row=1,sticky=tk.W)  # 放在 (1,1)
frame03.grid(column=1, row=1,sticky=tk.W)
frame04.grid(column=2, row=1,sticky=tk.W)

frame05.grid(column=0, row=3,columnspan=3,sticky = "news",padx=10)




#=========================測試==============================
print(font.families())


print(csv01)


root.mainloop()