# Ollama PII Detection Demo

[English](#ollama-pii-detection-demo) | [繁體中文](#ollama-pii-偵測示範專案)

A demonstration project showcasing PII (Personally Identifiable Information) detection using Ollama's local language models. This tool helps identify and protect sensitive personal information in text.

## Features

- **Privacy-First**: Runs completely locally using Ollama - no data sent to external servers
- **AI-Powered**: Leverages local language models for intelligent PII detection
- **Multiple PII Types**: Detects names, emails, phone numbers, addresses, and more
- **Easy to Use**: Simple setup and straightforward API

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running locally
- A compatible Ollama model (e.g., gemma3, etc.)

## Installation

### 1. Create a Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Ensure Ollama is Running

Make sure Ollama is installed and running on your system. You can start it with:

```bash
ollama serve
```

Pull a model if you haven't already:

```bash
ollama pull gemma3:27b
```

## Usage

Run the example 1:

```bash
python app.py
```

Run the example 2:

```bash
python app2.py
```

## Supported PII Types

- Names (first, last, full names)
- Email addresses
- Phone numbers
- Physical addresses
- Social Security Numbers
- Credit card numbers
- Date of birth
- ID numbers

## Project Structure

```
ollama-pii-demo/
├── README.md
├── requirements.txt
├── app.py
└── app2.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

---

# Ollama PII 偵測示範專案

這是一個展示如何使用 Ollama 本地語言模型進行 PII（個人身分識別資訊）偵測的示範專案。此工具幫助識別和保護文本中的敏感個人資訊。

## 功能特色

- **隱私優先**：完全在本地運行，使用 Ollama - 不會將資料傳送到外部伺服器
- **AI 驅動**：利用本地語言模型進行智慧型 PII 偵測
- **多種 PII 類型**：偵測姓名、電子郵件、電話號碼、地址等
- **易於使用**：簡單的設定和直觀的 API

## 系統需求

- Python 3.8 或更高版本
- 已安裝並運行的 [Ollama](https://ollama.ai/)
- 相容的 Ollama 模型（例如：gemma3 等）

## 安裝步驟

### 1. 建立 Python 虛擬環境

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

### 2. 安裝依賴套件

```bash
pip3 install -r requirements.txt
```

### 3. 確保 Ollama 正在運行

確保您的系統已安裝並運行 Ollama。您可以使用以下命令啟動：

```bash
ollama serve
```

如果尚未下載模型，請先下載：

```bash
ollama pull gemma3:27b
```

## 使用方法

執行範例一

```bash
python app.py
```

執行範例二

```bash
python app2.py
```

## 支援的 PII 類型

- 姓名（名字、姓氏、全名）
- 電子郵件地址
- 電話號碼
- 實體地址
- 身分證字號
- 信用卡號碼
- 出生日期
- 各類證件號碼

## 專案結構

```
ollama-pii-demo/
├── README.md
├── requirements.txt
├── app.py
└── app2.py
```

## 貢獻

歡迎貢獻！請隨時提交 Pull Request。

## 授權

MIT License

## 注意事項

- 本工具僅供示範和教育用途
- 在處理真實的敏感資料時，請確保遵守相關的資料保護法規
- 建議在生產環境中加入額外的安全措施

## 技術支援

如有問題或建議，請在 GitHub Issues 中提出。
