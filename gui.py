import PySimpleGUI as sg

# Define layout
layout = [
    [sg.Text('ラウドネス調整', font=('游ゴシック', 20))],
    [sg.Text('処理するファイルを選択', font=('游ゴシック', 12), size=(15, 1)), sg.InputText(font=('游ゴシック', 12)), sg.FileBrowse(font=('游ゴシック', 12))],
    [sg.Text('ピーク値を設定', font=('游ゴシック', 12), size=(15, 1)), sg.InputText(-1.0, font=('游ゴシック', 12)), sg.Text('dBTP', font=('游ゴシック', 12))],
    [sg.Text('ラウドネス値を設定', font=('游ゴシック', 12), size=(15, 1)), sg.InputText(-13.0, font=('游ゴシック', 12)), sg.Text('LKFS', font=('游ゴシック', 12))],
    [sg.Submit(button_text='変換', font=('游ゴシック', 12))]]


def getparam():
    window = sg.Window('Loudness Normalizer', layout, size=(630, 170))
    while True:
        event, values = window.read()
        if event is None:
            break
        if event == '変換':
            return values


if __name__ == '__main__':
    returns = getparam()
    print(returns[0])
    print(returns[1])
    print(returns[2])
