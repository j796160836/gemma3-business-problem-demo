# Ollama OCR Demo

[English](#ollama-ocr-demo) | [繁體中文](#ollama-ocr-使用範例)

A demonstration project for performing Optical Character Recognition (OCR) using Ollama's multimodal language models.

## Features

- Extract text from images using local AI models
- Powered by Ollama (runs completely offline)
- Privacy-focused: all processing happens locally
- Easy setup and usage
- Pure Python implementation

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed on your system
- A vision-capable model (e.g., `gemma3:27b`, `qwen2.5vl:7b`)

## Installation

### 1. Install Ollama

If you haven't already, install Ollama from [https://ollama.ai/](https://ollama.ai/)

### 2. Pull a Vision Model

```bash
ollama pull gemma3:27b
```

### 3. Set Up Python Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python3 -m venv venv
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python ocr_demo.py <path_to_image>
```

Example:
```bash
python ocr_demo.py sample_image.png
```

## Supported Image Formats

- PNG
- JPEG/JPG
- BMP
- WebP
- TIFF

## How It Works

This demo uses Ollama's vision-language models to analyze images and extract text content. The models can:

1. Recognize printed and handwritten text
2. Understand document layouts
3. Extract text in multiple languages
4. Provide context about the image content

## Troubleshooting

**Issue: "Model not found"**
- Make sure you've pulled a vision model: `ollama pull gemma3:27b`

**Issue: "Connection refused"**
- Ensure Ollama is running: `ollama serve`

**Issue: Low accuracy**
- Try different models (`gemma3:27b`, `qwen2.5vl:7b`)
- Ensure image quality is sufficient
- Check that text is clearly visible

## License

MIT License

---

## 繁體中文說明

# Ollama OCR 使用範例

這是一個使用 Ollama 多模態語言模型進行光學字元辨識（OCR）的示範專案。

## 功能特色

- 使用本地 AI 模型從圖片中提取文字
- 基於 Ollama（完全離線運行）
- 注重隱私：所有處理都在本地進行
- 簡單易用的設置
- 純 Python 實作

## 系統需求

- Python 3.8 或更高版本
- 系統已安裝 [Ollama](https://ollama.ai/)
- 支援視覺功能的模型（例如 `gemma3:27b`, `qwen2.5vl:7b`）

## 安裝步驟

### 1. 安裝 Ollama

如果尚未安裝，請從 [https://ollama.ai/](https://ollama.ai/) 下載安裝 Ollama

### 2. 下載視覺模型

```bash
ollama pull gemma3:27b
```

### 3. 建立 Python 虛擬環境

**macOS/Linux：**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows：**
```bash
python3 -m venv .venv
.venv\Scripts\activate
```

### 4. 安裝相依套件

```bash
pip3 install -r requirements.txt
```

## 使用方法

```bash
python ocr_demo.py <圖片路徑>
```

範例：
```bash
python ocr_demo.py sample_image.png
```

## 支援的圖片格式

- PNG
- JPEG/JPG
- BMP
- WebP
- TIFF

## 運作原理

此示範使用 Ollama 的視覺語言模型來分析圖片並提取文字內容。模型能夠：

1. 識別印刷體和手寫文字
2. 理解文件排版
3. 提取多種語言的文字
4. 提供圖片內容的上下文資訊

## 常見問題排除

**問題：「找不到模型」**
- 確認已下載視覺模型：`ollama pull gemma3:27b`

**問題：「連線被拒絕」**
- 確保 Ollama 正在運行：`ollama serve`

**問題：辨識準確度低**
- 嘗試不同的模型（`gemma3:27b`, `qwen2.5vl:7b`）
- 確保圖片品質足夠
- 檢查文字是否清晰可見

## 授權條款

MIT License
