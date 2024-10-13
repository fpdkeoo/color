import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#判斷程式

def start_btn_action():
    global np0; global np10; global np11; global np20; global np21
    if location.get() == '請選擇' :
        message_label.config(text='位置不可為空白')
    elif color.get() == '請選擇' :
        message_label.config(text='顏色不可為空白')
    elif s_and_h.get() == '請選擇' :
        message_label.config(text='方向不可為空白')
    elif depth.get() == '請選擇' :
        message_label.config(text='漸層不可為空白')
    else:
        message_label.config(text='')
        new_np0 = np0.copy()
        for i, j in enumerate(color_dict[color.get()]):
            if j == 0:
                new_np0[:, :, i] = 0
        if depth.get() == '淺到深' :
            new_np0 = new_np0[::-1]
        if s_and_h.get() == '直' :
            new_np0 = np.rot90(new_np0, k=1, axes=(0, 1))
        if location.get() == '左上':
            np10 = new_np0
        elif location.get() == '右上':
            np11 = new_np0
        elif location.get() == '左下':
            np20 = new_np0
        else:
            np21 = new_np0
        np1 = np.hstack((np10, np11))
        np2 = np.hstack((np20, np21))
        npt = np.vstack((np1, np2))
        change(npt)

#更換圖片
def change(npt):
    fig = Figure(figsize=(5.1, 5.1), facecolor='whitesmoke', layout='constrained')
    ax = fig.add_subplot(111)
    ax.imshow(npt)
    ax.axis("off")
    canvas = FigureCanvasTkAgg(fig, master=root)  # 創建畫布
    canvas.draw()  # 繪製圖形
    canvas.get_tk_widget().place(x=5, y=60)  # 將畫布放入窗口

# 定義點擊超連結的函數
def open_link(event):
    webbrowser.open('https://github.com/fpdkeoo/color')

#======================================================================
#顏色
np0=np.ndarray(shape=(256,256,3), dtype="uint8") #三維(256列256行3個)
data = [[row for col in range(256)] for row in range(0, 256, 4)]
color_dict = {'紅色':[255,0,0], '綠色':[0,255,0], '藍色':[0,0,255], '黃色':[255,255,0], '洋紅色':[255,0,255], '青色':[0,255,255], '灰階':[255,255,255]}

for i in range(3):
    np0[:,:,i] = data * 4
np10 = np0.copy()
np11 = np10[::-1]
np20 = np.rot90(np10, k=1, axes=(1,0))
np21 = np.rot90(np10, k=1, axes=(0,1))
np1= np.hstack((np10,np11))
np2 = np.hstack((np20,np21))
npt = np.vstack((np1,np2))

#======================================================================
# 視窗
root = tk.Tk()
root.title('顏色漸層')

#視窗大小位置
window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度
width = 520
height = 600
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')

#文字label
location_label=tk.Label(root,text='位置:',font=('Arial',12,'bold'))
location_label.place(x=5, y=10)

color_label=tk.Label(root,text='顏色:',font=('Arial',12,'bold'))
color_label.place(x=115, y=10)

s_and_h_label=tk.Label(root,text='方向:',font=('Arial',12,'bold'))
s_and_h_label.place(x=225, y=10)

depth_label=tk.Label(root,text='漸層',font=('Arial',12,'bold'))
depth_label.place(x=335, y=10)

message_label=tk.Label(root,text='',font=('Arial',15,'bold'),fg='#f00')
message_label.place(x=5, y=35)

#下拉式選單
location = ttk.Combobox(root, values=['左上', '右上', '左下', '右下'], width=5)
location.set('請選擇')
location.place(x=50, y=10)

color = ttk.Combobox(root, values=list(color_dict.keys()), width=5)
color.set('請選擇')
color.place(x=160, y=10)

s_and_h = ttk.Combobox(root, values=['橫','直'], width=5)
s_and_h.set('請選擇')
s_and_h.place(x=270, y=10)

depth = ttk.Combobox(root, values=['淺到深','深到淺'], width=5)
depth.set('請選擇')
depth.place(x=380, y=10)

#按鈕
start_btn = tk.Button(root,text='確定',font=('Arial',12,'bold'), width=5 ,command=start_btn_action)
start_btn.place(x=450, y=5)

#===========================================================================
#圖片
change(npt)

#===========================================================================
#出處
by_label=tk.Label(root,text='by: 點擊這裡訪問 fpdkeoo github',font=('Arial',10), fg='blue', cursor="hand2" )
by_label.place(x=5, y=570)
by_label.bind("<Button-1>", open_link)

root.mainloop()