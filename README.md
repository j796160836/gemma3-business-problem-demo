# Solving Tough Enterprise Problems with Gemma 3 Open Models

[English](#solving-tough-enterprise-problems-with-gemma-3-open-models) | [繁體中文](#用-gemma-3-開放模型來解決企業難解的問題)

## Overview

A collection of demos showcasing LLM applications in enterprise scenarios:

1. **Privacy Protection** - Detecting and handling personally identifiable information (PII)
2. **Traditional OCR** - Optical Character Recognition for image text extraction
3. **LLM-Enhanced Vision (LLM-OCR)** - Advanced document understanding with vision-language models, using LLM to do OCR tasks.

## Demo Projects

### 1. Ollama PII Demo
Privacy-focused demo for detecting and handling personally identifiable information.

- **Location**: [ollama-pii-demo/](ollama-pii-demo/)
- **Technology**: Ollama
- **Features**:
  - PII detection and masking
  - Privacy-aware document processing

### 2. EasyOCR Demo
Simple OCR implementation using EasyOCR library with support for Traditional Chinese and English.

- **Location**: [easy-ocr-demo/](easy-ocr-demo/)
- **Technology**: EasyOCR
- **Features**:
  - Traditional Chinese and English recognition
  - Regex-based field extraction
  - Lightweight and easy to set up

### 3. Tesseract OCR Demo
Traditional OCR approach using Tesseract engine.

- **Location**: [tesseract-ocr-demo/](tesseract-ocr-demo/)
- **Technology**: Tesseract OCR
- **Features**:
  - Classic OCR engine
  - Traditional Chinese language pack (chi_tra)
  - Pattern-based information extraction

### 4. Ollama OCR Demo
LLM-powered OCR using Ollama with vision models.

- **Location**: [ollama-ocr-demo/](ollama-ocr-demo/)
- **Technology**: Ollama + Vision LLM
- **Features**:
  - AI-powered text recognition and understanding
  - Structured JSON output
  - Support for models like Qwen2.5-VL, Gemma3
  - Image preprocessing and optimization

### 5. EasyOCR + Ollama Demo
Hybrid approach combining EasyOCR with LLM post-processing.

- **Location**: [easy-ocr-ollama-demo/](easy-ocr-ollama-demo/)
- **Technology**: EasyOCR + Ollama
- **Features**:
  - Two-stage processing
  - Enhanced accuracy through LLM refinement

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- For Ollama demos: Ollama installed and download specific models

### Installation

Each demo has its own virtual environment and dependencies. Navigate to the specific demo directory and install requirements:

```bash
cd <demo-directory>
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running a Demo

```bash
python app.py
```

## Project Structure

```
ocr-demo/
├── README.md
├── ollama-pii-demo/
│   ├── README.md
│   ├── app.py
│   ├── app2.py
│   └── requirements.txt
├── easy-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   └── requirements.txt
├── tesseract-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   ├── output.json
│   └── requirements.txt
├── ollama-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   └── requirements.txt
└── easy-ocr-ollama-demo/
    ├── README.md
    ├── app.py
    ├── demo-pic/
    │   └── roc-mol.jpg
    └── requirements.txt
```

## Use Cases

- Government document digitization
- Automated form processing
- Document information extraction
- Compliance and record-keeping
- Data entry automation

## Technologies Used

- **EasyOCR**: Lightweight OCR engine with multilingual support
- **Tesseract**: Open-source OCR engine by Google
- **Ollama**: Local LLM deployment platform
- **Vision LLMs (LLM-OCR)**: Multimodal language models (Qwen2.5-VL, Gemma3)

## License

MIT License

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

---

# 用 Gemma 3 開放模型來解決企業難解的問題

示範使用 LLM 的相關應用：

1. **專注於個人資料保護** - 偵測與處理個人識別資訊（PII）
2. **使用傳統 OCR** - 光學字元辨識實作圖片文字擷取
3. **使用 LLM 增強的視覺功能** - 運用視覺語言模型進行進階文件理解

## 概述

本儲存庫包含多個示範專案，展示不同的 OCR 技術，用於從繁體中文政府文件中擷取結構化資訊。每個實作都專注於辨識關鍵欄位，如文號、日期、發文/收文單位資訊和文件標題。

## 示範專案

### 1. Ollama PII 示範
專注於隱私的示範，用於偵測和處理個人識別資訊。

- **位置**：[ollama-pii-demo/](ollama-pii-demo/)
- **技術**：Ollama
- **功能**：
  - PII 偵測和遮罩
  - 具隱私意識的文件處理

### 2. EasyOCR 示範
使用 EasyOCR 函式庫的簡單 OCR 實作，支援繁體中文和英文。

- **位置**：[easy-ocr-demo/](easy-ocr-demo/)
- **技術**：EasyOCR
- **功能**：
  - 繁體中文和英文辨識
  - 基於正則表達式的欄位擷取
  - 輕量且易於設定

### 3. Tesseract OCR 示範
使用 Tesseract 引擎的傳統 OCR 方法。

- **位置**：[tesseract-ocr-demo/](tesseract-ocr-demo/)
- **技術**：Tesseract OCR
- **功能**：
  - 經典 OCR 引擎
  - 繁體中文語言包（chi_tra）
  - 基於模式的資訊擷取

### 4. Ollama OCR 示範
使用 Ollama 與視覺模型的 LLM 驅動 OCR。

- **位置**：[ollama-ocr-demo/](ollama-ocr-demo/)
- **技術**：Ollama + 視覺 LLM
- **功能**：
  - AI 驅動的文字辨識與理解
  - 結構化 JSON 輸出
  - 支援 Qwen2.5-VL、Gemma3 等模型
  - 影像預處理和最佳化

### 5. EasyOCR + Ollama 示範
結合 EasyOCR 與 LLM 後處理的混合方法。

- **位置**：[easy-ocr-ollama-demo/](easy-ocr-ollama-demo/)
- **技術**：EasyOCR + Ollama
- **功能**：
  - 兩階段處理
  - 透過 LLM 精煉提升準確度

## 快速開始

### 先決條件

- Python 3.8 或更高版本
- Python venv 虛擬環境（建議）
- 對於 Ollama 示範：需有對應下載模型的 Ollama 伺服器

### 安裝

每個示範都有自己的虛擬環境和依賴項。導航到特定的示範目錄並安裝需求：

```bash
cd <示範目錄>
python -m venv .venv
source .venv/bin/activate  # Windows 使用：.venv\Scripts\activate
pip install -r requirements.txt
```

### 執行示範

```bash
python app.py
```

## 專案結構

```
ocr-demo/
├── README.md
├── ollama-pii-demo/
│   ├── README.md
│   ├── app.py
│   ├── app2.py
│   └── requirements.txt
├── easy-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   └── requirements.txt
├── tesseract-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   ├── output.json
│   └── requirements.txt
├── ollama-ocr-demo/
│   ├── README.md
│   ├── app.py
│   ├── demo-pic/
│   │   └── roc-mol.jpg
│   └── requirements.txt
└── easy-ocr-ollama-demo/
    ├── README.md
    ├── app.py
    ├── demo-pic/
    │   └── roc-mol.jpg
    └── requirements.txt
```

## 使用案例

- 政府文件數位化
- 自動化表單處理
- 文件資訊擷取
- 合規與記錄保存
- 資料輸入自動化

## 使用技術

- **EasyOCR**：輕量級多語言支援的 OCR 引擎
- **Tesseract**：Google 開源的 OCR 引擎
- **Ollama**：本地 LLM 部署平台
- **視覺 LLM**：多模態語言模型（Qwen2.5-VL、Gemma3）

## 授權

MIT License

## 貢獻

歡迎貢獻、問題和功能請求。如果您想貢獻，請隨時查看問題頁面。
