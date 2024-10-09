import tkinter as tk
from tkinter import Label, Toplevel, Text, Scrollbar, RIGHT, Y, BOTH
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk, PngImagePlugin
import json  # JSON整形用

# メインアプリケーションクラス
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
        if file_path.lower().endswith(".png"):
            self.display_image(file_path)
            self.show_metadata(file_path)
        else:
            tk.messagebox.showerror("Invalid File", "Please drop a PNG image.")

    # 画像を表示する関数
    def display_image(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((500, 300))  # キャンバスに合わせて画像を縮小
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(250, 150, image=self.photo)

    # ネストされたJSONをフラットに表示する関数
    def format_flat_json(self, data, parent_key=""):
        formatted_text = ""
        if isinstance(data, dict):
            for key, value in data.items():
                full_key = f"{parent_key}.{key}" if parent_key else key
                formatted_text += self.format_flat_json(value, full_key)
        elif isinstance(data, list):
            for idx, item in enumerate(data):
                full_key = f"{parent_key}[{idx}]"
                formatted_text += self.format_flat_json(item, full_key)
        else:
            formatted_text += f"{parent_key}: {data}\n"
        return formatted_text

    # PNGメタデータを表示する関数
    def show_metadata(self, file_path):
        image = Image.open(file_path)
        if isinstance(image, PngImagePlugin.PngImageFile):
            metadata = image.info  # メタデータの取得

            # メタデータがJSON文字列の場合は展開する
            for key, value in metadata.items():
                if isinstance(value, str):
                    try:
                        # 値がJSON形式か確認して展開
                        parsed_json = json.loads(value)
                        formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
                        metadata[key] = formatted_json  # 展開したJSONを整形して表示
                    except json.JSONDecodeError:
                        pass

            self.show_metadata_window(metadata)
        else:
            tk.messagebox.showerror("Error", "Unable to extract metadata.")

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
            # キー部分を強調表示 (太字)
            text_area.insert(tk.END, f"{key}:\n", "title")
            if isinstance(value, str):
                try:
                    parsed_json = json.loads(value)
                    formatted_json = self.format_flat_json(parsed_json)
                    text_area.insert(tk.END, f"{formatted_json}\n", "body")
                except json.JSONDecodeError:
                    text_area.insert(tk.END, f"{value}\n\n", "body")
            else:
                text_area.insert(tk.END, f"{value}\n\n", "body")

        # テキストウィジェットのスタイル設定
        text_area.tag_configure("title", font=("Arial", 12, "bold"))
        text_area.tag_configure("body", font=("Arial", 10))

        # テキストウィジェットをリードオンリーにする
        text_area.config(state="normal")  # テキスト編集を許可
        text_area.config(state="disabled")  # テキストを表示後に編集不可にする

# アプリケーションの起動
if __name__ == "__main__":
    app = ImageApp()
    app.mainloop()
