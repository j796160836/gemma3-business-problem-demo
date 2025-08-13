# EasyOCR Demo

[English](#easyocr-demo) | [繁體中文](#easyocr-使用範例)

A demonstration project showcasing EasyOCR's capabilities for optical character recognition (OCR) in multiple languages.

## Features

- Extract text from images using EasyOCR
- Support for multiple languages including English and Traditional Chinese
- Simple and easy-to-use interface
- Lightweight virtual environment setup

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Installation

1. **Create a Python virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

Run the project

```bash
python app.py
```

## Project Structure

```
easy-ocr-demo/
├── README.md
├── requirements.txt
└── app.py
```

## Supported Languages

EasyOCR supports over 80 languages. Common options include:
- `en` - English
- `ch_tra` - Traditional Chinese
- `ch_sim` - Simplified Chinese
- `ja` - Japanese
- `ko` - Korean

## Troubleshooting

If you encounter installation issues:
- Ensure you have the latest version of pip: `pip install --upgrade pip`
- On some systems, you may need to install additional dependencies for image processing

## License

MIT License

This is a demonstration project. Please refer to [EasyOCR's official repository](https://github.com/JaidedAI/EasyOCR) for more detail information.

---

# EasyOCR 使用範例

一個展示 EasyOCR 光學字元辨識（OCR）功能的範例專案，支援多種語言文字辨識。

## 功能特色

- 使用 EasyOCR 從圖片中提取文字
- 支援多種語言，包含英文和繁體中文
- 簡單易用的介面
- 輕量級虛擬環境設定

## 系統需求

- Python 3.7 或更高版本
- pip 套件管理器

## 安裝步驟

1. **建立 Python 虛擬環境：**
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

2. **安裝依賴：**
```bash
pip install -r requirements.txt
```

## 使用方式

執行專案

```bash
python app.py
```

## 專案結構

```
easy-ocr-demo/
├── README.md
├── requirements.txt
└── app.py
```

## 支援語言

EasyOCR 支援超過 80 種語言。常見選項包括：
- `en` - 英文
- `ch_tra` - 繁體中文
- `ch_sim` - 簡體中文
- `ja` - 日文
- `ko` - 韓文

## 疑難排解

如果遇到安裝問題：
- 確保您使用最新版本的 pip：`pip install --upgrade pip`
- 某些系統可能需要安裝額外的影像處理相關套件

## 授權

MIT License

這是一個 Demo 專案。更多相關資訊請參考 [EasyOCR 官方儲存庫](https://github.com/JaidedAI/EasyOCR)。
