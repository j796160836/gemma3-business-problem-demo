# Tesseract OCR Demo

[English](#tesseract-ocr-demo) | [繁體中文](#tesseract-ocr-使用範例)

A demonstration project showcasing the capabilities of Tesseract OCR for optical character recognition in Python.

## Features

- Text extraction from images using Tesseract OCR
- Support for multiple image formats (PNG, JPG, JPEG, etc.)
- Python-based implementation with pytesseract
- Easy-to-use command-line interface
- Cross-platform support (Windows, macOS, Linux)

## Prerequisites

Before running this project, you need to install Tesseract OCR on your system:

### Windows
Download and install Tesseract from the [official GitHub repository](https://github.com/UB-Mannheim/tesseract/wiki).

### macOS
Install using Homebrew:
```bash
brew install tesseract
```

### Linux
Install using apt:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## Installing Traditional Chinese Language Data

To use Tesseract with Traditional Chinese, you need to download the language data file:

1. **Download the Traditional Chinese model:**
   Visit [https://tesseract-ocr.github.io/tessdoc/Data-Files](https://tesseract-ocr.github.io/tessdoc/Data-Files) and download `chi_tra.traineddata`

2. **List installed languages:**
   ```bash
   tesseract --list-langs
   ```

3. **Find Tesseract installation location:**
   ```bash
   brew list tesseract
   ```

   For example, you might see:
   ```
   /opt/homebrew/Cellar/tesseract/5.5.1_1/
   ```

4. **Place the model file:**
   Copy `chi_tra.traineddata` to:
   ```
   /opt/homebrew/Cellar/tesseract/<version_number>/share/tessdata
   ```

## Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd tesseract-ocr-demo
```

2. **Create a Python virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip3 install -r requirements.txt
```

## Usage

Run the project

```bash
python app.py
```

## Project Structure

```
tesseract-ocr-demo/
├── README.md
├── requirements.txt
└── app.py
```

## Troubleshooting

- **Tesseract not found error**: Make sure Tesseract is installed and added to your system PATH
- **Poor OCR accuracy**: Try preprocessing the image (adjust brightness, contrast, or resolution)
- **Language support**: Install additional language packs if needed using `brew install tesseract-lang` (macOS) or equivalent

## License

MIT License

---

# Tesseract OCR 使用範例

這是一個展示如何在 Python 中使用 Tesseract OCR 進行光學字元辨識的示範專案。

## 功能特色

- 使用 Tesseract OCR 從圖片中提取文字
- 支援多種圖片格式（PNG、JPG、JPEG 等）
- 基於 Python 與 pytesseract 實作
- 簡易的命令列介面
- 跨平台支援（Windows、macOS、Linux）

## 系統需求

在執行此專案之前，您需要先在系統中安裝 Tesseract OCR：

### Windows
從 [官方 GitHub 儲存庫](https://github.com/UB-Mannheim/tesseract/wiki)下載並安裝 Tesseract。

### macOS
使用 Homebrew 安裝：
```bash
brew install tesseract
```

### Linux
使用 apt 安裝：
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## 安裝繁體中文詞庫

要在 Tesseract 中使用繁體中文辨識,需要下載語言資料檔案:

1. **下載繁體中文模型:**
   前往 [https://tesseract-ocr.github.io/tessdoc/Data-Files](https://tesseract-ocr.github.io/tessdoc/Data-Files) 下載 `chi_tra.traineddata`

2. **列出已安裝的語言:**
   ```bash
   tesseract --list-langs
   ```

3. **找到 Tesseract 安裝位置:**
   ```bash
   brew list tesseract
   ```

   例如,您可能會看到:
   ```
   /opt/homebrew/Cellar/tesseract/5.5.1_1/
   ```

4. **放置模型檔案:**
   將 `chi_tra.traineddata` 複製到:
   ```
   /opt/homebrew/Cellar/tesseract/<version_number>/share/tessdata
   ```

## 安裝步驟

1. **複製儲存庫：**
```bash
git clone <repository-url>
cd tesseract-ocr-demo
```

2. **建立 Python 虛擬環境：**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

3. **安裝相依套件：**
```bash
pip3 install -r requirements.txt
```

## 使用方式

執行專案

```bash
python app.py
```

## 專案結構

```
tesseract-ocr-demo/
├── README.md
├── requirements.txt
└── app.py
```

## 疑難排解

- **找不到 Tesseract 錯誤**：請確保 Tesseract 已安裝並加入系統 PATH
- **OCR 辨識準確度不佳**：嘗試預處理圖片（調整亮度、對比度或解析度）
- **語言支援**：如需其他語言支援，請使用 `brew install tesseract-lang`（macOS）或其他對應指令安裝語言包

## 授權條款

MIT License
