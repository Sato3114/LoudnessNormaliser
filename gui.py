from tkinter import *
from tkinter import ttk, filedialog, messagebox


def getparamgui():
    root = Tk()
    path_audio, tp_want, ldnss_want = '', 0, 0
    pathaudio, tpwant, ldnsswant = StringVar(), StringVar(), StringVar(),

    # When the "選択" button is pushed
    def selfile():
        ftype = [('Supported File', '*.wav *.mp3')]
        path = filedialog.askopenfilename(filetypes=ftype)
        pathaudio.insert(0, path)

    # When the "処理開始" button is pushed
    def start():
        nonlocal path_audio, tp_want, ldnss_want
        if entry_pathaudio.get() == '':
            messagebox.showerror('ERROR', 'ファイルが指定されていません')
        else:
            path_audio = entry_pathaudio.get()
            tp_want = float(entry_tp.get())
            ldnss_want = float(entry_ldnss.get())
            root.quit()

    # Define window
    root.maxsize(width=400, height=130)
    # root.minsize(width=400, height=130)
    # root.geometry('400x130')
    root.title('Loudness Normalizer')
    frame = ttk.Frame(root, padding=16)
    frame.grid()

    # Define widgets
    label_sel = ttk.Label(frame, text='処理ファイル', font=('', 12))
    label_tp = ttk.Label(frame, text='目標ピーク値', font=('', 12))
    label_ldnss = ttk.Label(frame, text='目標ラウドネス値', font=('', 12))
    label_unittp = ttk.Label(frame, text='dBTP', font=('', 12))
    label_unitldnss = ttk.Label(frame, text='LKFS', font=('', 12))
    entry_pathaudio = ttk.Entry(frame)
    entry_tp = ttk.Entry(frame)
    entry_ldnss = ttk.Entry(frame)
    button_filesel = ttk.Button(frame, text='選択', command=selfile)  # File select button
    button_start = ttk.Button(frame, text='処理開始', command=start)  # Start button

    # Default setting for parameter entries
    entry_tp.insert(0, '-1.0')
    entry_ldnss.insert(0, '-13.0')

    # Place widgets
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

    # Run mainloop
    root.mainloop()

    return path_audio, tp_want, ldnss_want


if __name__ == '__main__':
    x, y, z = getparamgui()
    print(x)
    print(y)
    print(z)
