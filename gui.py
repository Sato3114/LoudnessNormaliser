from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class Application(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        # 変数定義
        self.pathaudio = StringVar()
        self.tpwant = StringVar()
        self.ldnsswant = StringVar()

        # ウィンドウの定義
        master.geometry('400x130')
        master.title('Loudness Normalizer')
        master.minsize(width=400, height=130)
        master.maxsize(width=400, height=130)

        # ウィジェットの定義
        frame = ttk.Frame(master, padding=16)
        label_sel = ttk.Label(frame, text='処理ファイル', font=('', 12))
        label_tp = ttk.Label(frame, text='目標ピーク値', font=('', 12))
        label_ldnss = ttk.Label(frame, text='目標ラウドネス値', font=('', 12))
        label_unittp = ttk.Label(frame, text='dBTP', font=('', 12))
        label_unitldnss = ttk.Label(frame, text='LKFS', font=('', 12))
        entry_pathaudio = ttk.Entry(frame, textvariable=self.pathaudio)
        entry_tp = ttk.Entry(frame, textvariable=self.tpwant)
        entry_ldnss = ttk.Entry(frame, textvariable=self.ldnsswant)
        button_filesel = ttk.Button(frame, text='選択', command=self.selfile)
        button_start = ttk.Button(frame, text='処理開始', command=self.start)

        # パラメータentryのデフォルト値設定
        entry_tp.insert(0, '-1.0')
        entry_ldnss.insert(0, '-13.0')

        # ウィジェットの配置
        frame.grid()
        label_sel.grid(row=0, column=0, sticky=W)
        entry_pathaudio.grid(row=0, column=1)
        button_filesel.grid(row=0, column=2)
        label_tp.grid(row=1, column=0, sticky=W)
        entry_tp.grid(row=1, column=1)
        label_unittp.grid(row=1, column=2, sticky=W)
        label_ldnss.grid(row=2, column=0, sticky=W)
        entry_ldnss.grid(row=2, column=1)
        label_unitldnss.grid(row=2, column=2, sticky=W)
        button_start.grid(row=4, column=0, columnspan=5)

    def selfile(self):  # ファイル選択ボタン押下時
        ftype = [('Supported File', '*.wav *.mp3')]
        file = filedialog.askopenfilename(filetypes=ftype)
        self.pathaudio.set(file)

    def start(self):  # 処理開始ボタン押下時
        if self.pathaudio.get() == '':
            messagebox.showerror('ERROR', 'ファイルが指定されていません')
        else:
            self.master.destroy()


def getparam():
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    path_audio = app.pathaudio.get()
    truepeak = float(app.tpwant.get())
    loudness = float(app.ldnsswant.get())
    # print(path_audio)
    # print(truepeak)
    # print(loudness)
    return path_audio, truepeak, loudness


if __name__ == '__main__':
    y = getparam()
    print(y)
