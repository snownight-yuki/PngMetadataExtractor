
# 画像表示＆メタデータ抽出ツール / Image Viewer & Metadata Extractor Tool

### アプリケーション名: 画像表示＆メタデータ抽出ツール

### 概要
このアプリケーションは、ドラッグ＆ドロップでPNG画像をウィンドウ内に追加し、その画像を表示するとともに、PNGのメタデータを抽出してフラットな形式で表示するツールです。画像の詳細なメタデータが表示されます。

### 特徴
- 画像のドラッグ＆ドロップ対応。
- 画像の表示。
- PNG画像のメタデータを読み取り、フラットな形式で表示。
- ネストされたJSONデータもインデントなしで見やすく表示。
- テキスト領域にスクロールバーを追加し、大量のメタデータでも快適に操作可能。

### 必要な環境
- Python 3.x
- tkinter
- tkinterDnD2
- Pillow
- PyInstaller（exeファイルを作成する場合）

### インストール方法

1. 必要な依存ライブラリをインストールします。

   ```bash
   pip install pillow tkinterdnd2
   ```

2. アプリケーションのスクリプトを実行します。

   ```bash
   python PngMetaExtractor.py
   ```

3. exeファイルを作成する場合は、以下のコマンドを使用します。

   ```bash
   pyinstaller --onefile --windowed --collect-data tkinterdnd2 PngMetaExtractor.py
   ```

4. 実行ファイルが作成されたら、`dist`フォルダ内の `.exe` ファイルを実行します。

### 使い方
1. アプリケーションを起動します。
2. PNG画像をウィンドウ内にドラッグ＆ドロップします。
3. 画像がウィンドウ内に表示され、メタデータが自動的に抽出されます。
4. メタデータは別のウィンドウで表示され、スクロールして内容を確認できます。

### 問題の解決
- `Unable to load tkdnd library` エラーが発生した場合、`tkinterDnD2` のライブラリが正しく読み込まれていない可能性があります。この場合は、`tkdnd.dll` を手動で実行ファイルのディレクトリにコピーしてください。

### ライセンス
MITライセンス

---

### Application Name: Image Viewer & Metadata Extractor Tool

### Overview
This application allows you to drag and drop PNG images into the window, displaying the image and extracting the PNG metadata in a flat format. It provides an easy-to-read display of the detailed metadata of the image.

### Features
- Drag-and-drop support for images.
- Displays the PNG image.
- Extracts and displays the metadata of PNG images in a flat format.
- Nested JSON data is displayed clearly without indentation.
- A scrollbar is added to the text area for easy handling of large amounts of metadata.

### Requirements
- Python 3.x
- tkinter
- tkinterDnD2
- Pillow
- PyInstaller (for creating an executable file)

### Installation

1. Install the required dependencies:

   ```bash
   pip install pillow tkinterdnd2
   ```

2. Run the script:

   ```bash
   python PngMetaExtractor.py
   ```

3. To create an executable file, use the following command:

   ```bash
   pyinstaller --onefile --windowed --collect-data tkinterdnd2 PngMetaExtractor.py
   ```

4. Once the executable is created, run the `.exe` file from the `dist` folder.

### Usage
1. Launch the application.
2. Drag and drop a PNG image into the window.
3. The image will be displayed, and the metadata will be automatically extracted.
4. The metadata is shown in a separate window, and you can scroll through the details.

### Troubleshooting
- If you encounter the `Unable to load tkdnd library` error, it indicates that the `tkinterDnD2` library is not being loaded correctly. In this case, manually copy the `tkdnd.dll` file to the directory containing the executable.

### License
MIT License
