import os
import tkinter as tk
from tkinter import Label, Toplevel, Text, Scrollbar, RIGHT, Y, BOTH
from tkinter import messagebox  # messageboxを正しくインポート
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk, PngImagePlugin

class ImageApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Viewer and Metadata Extractor")
        self.geometry("600x400")

        # ラベルとキャンバスを配置
        self.label = Label(self, text="Drag and drop a PNG image here")
        self.label.pack(pady=20)

        self.canvas = tk.Canvas(self, width=500, height=300, bg="white")
        self.canvas.pack()

        # ドラッグ&ドロップを有効にする
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.on_drop)

    # ドロップされたファイルを処理する関数
    def on_drop(self, event):
        file_path = event.data
        print(file_path)

        # Windows環境のファイルパス処理
        file_path = file_path.strip('{}')  # {}で囲まれている可能性があるので除去
        file_path = file_path.replace('/', '\\')  # 正しいファイルパス形式に変換

        # ファイルの存在確認と拡張子の検証
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "ファイルが存在しません。")
            return

        # ファイル拡張子が.pngかどうかを確認
        if not file_path.lower().endswith(".png"):
            messagebox.showerror("Invalid File", "PNGファイルをドラッグ＆ドロップしてください。")
            return

        # ファイルの表示処理
        try:
            self.display_image(file_path)
            self.show_metadata(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"ファイルを処理中にエラーが発生しました: {e}")

    # 画像を表示する関数
    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((500, 300))  # キャンバスに合わせて画像を縮小
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(250, 150, image=self.photo)

    # PNGメタデータを表示する関数
    def show_metadata(self, file_path):
        image = Image.open(file_path)
        if isinstance(image, PngImagePlugin.PngImageFile):
            metadata = image.info  # メタデータの取得
            self.show_metadata_window(metadata)
        else:
            messagebox.showerror("Error", "PNGメタデータを読み込めません。")

    # メタデータを表示するウィンドウ
    def show_metadata_window(self, metadata):
        window = Toplevel(self)
        window.title("PNG Metadata")
        window.geometry("600x500")  # ウィンドウのサイズ

        # テキストウィジェットとスクロールバーを作成
        text_area = Text(window, wrap="word", padx=10, pady=10, font=("Arial", 10), undo=True)
        scrollbar = Scrollbar(window, command=text_area.yview)
        text_area['yscrollcommand'] = scrollbar.set

        # テキストウィジェットとスクロールバーをパック
        scrollbar.pack(side=RIGHT, fill=Y)
        text_area.pack(expand=True, fill=BOTH)

        # メタデータを整形して表示
        for key, value in metadata.items():
            text_area.insert(tk.END, f"{key}:\n{value}\n\n")

        # テキストウィジェットをリードオンリーにする
        text_area.config(state="disabled")

# アプリケーションの起動
if __name__ == "__main__":
    app = ImageApp()
    app.mainloop()
