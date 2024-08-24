# Markdown 工具集

這個工具集包含三個主要功能：將 Markdown 轉換為 PDF、將 Markdown 翻譯成中英文對照版本，以及處理 YouTube 字幕。

## 安裝依賴

在使用這些工具之前，請確保已安裝所需的 Python 套件和字體：

1. 安裝 Python 套件：
   ```bash
   pip install markdown openai python-dotenv weasyprint youtube_transcript_api
   ```

2. 在 Ubuntu 上安裝 Noto Sans CJK 字體：
   ```bash
   sudo apt update
   sudo apt install fonts-noto-cjk
   ```

   安裝完成後，您可能需要重新啟動應用程式或登出再登入，以確保新安裝的字體生效。

## 1. Markdown 轉 PDF 工具

這個工具可以將 Markdown 檔案轉換為 PDF 格式，並正確支援中文顯示。

### 使用方法

基本用法：

```bash
python markdown_to_pdf.py 輸入檔案路徑 [-o 輸出檔案名稱]
```

例如：

```bash
python markdown_to_pdf.py 文件.md -o 輸出
```

注意事項：

- 輸入檔案路徑應該是完整的路徑或相對於當前目錄的路徑。
- 使用 `-o` 選項時，只需提供檔案名稱，不需要包含路徑或 `.pdf` 副檔名。
- 所有生成的 PDF 檔案都會自動保存在 `exports` 資料夾中。
- 如果不指定輸出檔案名稱，程序會使用輸入檔案的名稱（改為 .pdf 副檔名）。

例如，以下命令會在 `exports` 資料夾中生成 `輸出.pdf`：

```bash
python markdown_to_pdf.py /path/to/文件.md -o 輸出
```

如果不指定輸出名稱：

```bash
python markdown_to_pdf.py /path/to/文件.md
```

這會在 `exports` 資料夾中生成 `文件.pdf`。

### 查詢檔案完整路徑

在 Linux 系統中，有多種方法可以查詢檔案的完整路徑：

1. 使用 `readlink` 命令：

```bash
readlink -f readme.md
```

這個命令會顯示 `readme.md` 檔案的完整路徑。例如，如果 `readme.md` 位於 `/home/user/documents/` 目錄中，輸出會類似於：

```
/home/user/documents/readme.md
```

`readlink -f` 命令特別有用，因為它可以解析符號鏈接，顯示實際檔案的路徑，而不是鏈接的路徑。

2. 使用 `realpath` 命令：

```bash
realpath readme.md
```

3. 使用 `pwd` 和檔案名稱組合：

```bash
echo "$(pwd)/readme.md"
```

4. 使用 `find` 命令：

```bash
find "$(pwd)" -name "readme.md"
```

5. 如果您使用的是 Bash shell，可以使用 `$BASH_SOURCE` 變數（對於腳本文件）：

```bash
echo "${BASH_SOURCE[0]}"
```

這些命令都會顯示 `readme.md` 的完整路徑。

## 2. Markdown 翻譯工具

這個工具可以將英文 Markdown 文件翻譯成中英文對照的版本，並可選擇性地將結果轉換為 PDF。

### 使用前準備

1. 創建一個名為 `.env` 的文件在專案根目錄。
2. 在 `.env` 文件中添加您的 OpenAI API Key：

   ```
   OPENAI_API_KEY=您的OpenAI_API_Key
   ```

   請將 `您的OpenAI_API_Key` 替換為您實際的 OpenAI API Key。

### 使用方法

基本用法：

```bash
python markdown_translator.py 輸入檔案路徑 [-o 輸出檔案名稱] [--pdf]
```

例如：

```bash
python markdown_translator.py 文件.md -o 輸出 --pdf
```

這個命令會將 `文件.md` 翻譯成中英文對照的版本，並將結果保存為 `輸出.md` 和 `輸出.pdf`。

如果不指定輸出檔案名稱，程序會使用輸入檔案的名稱（加上 `_translated` 前綴）：

```bash
python markdown_translator.py 文件.md --pdf
```

這會生成 `文件_translated.md` 和 `文件_translated.pdf`。

### 注意事項

- 輸入檔案路徑應該是完整的路徑或相對於當前目錄的路徑。
- 使用 `-o` 選項時，只需提供檔案名稱，不需要包含路徑或 `.md` 副檔名。
- 使用 `--pdf` 選項時，程序會生成 PDF 文件，並將其保存在與輸出 Markdown 文件相同的路徑中。
- 所有生成的檔案都會自動保存在 `exports` 資料夾中。
- 確保您已在 `.env` 文件中正確設置了 OpenAI API Key。

## 3. YouTube 字幕處理工具

這個工具可以下載指定 YouTube 影片的字幕，將其轉換為 Markdown 格式，然後翻譯成中英文對照版本，最後生成 PDF 文件。

### 使用方法

基本用法：

```bash
python youtube_subtitle_processor.py <YouTube影片ID> [輸出檔案名稱]
```

例如：

```bash
python youtube_subtitle_processor.py dQw4w9WgXcQ 我的影片字幕
```

注意事項：

- YouTube 影片 ID 是影片網址中 `v=` 後面的部分。
- 如果無法下載字幕，程序會顯示錯誤訊息並退出。

## 疑難排解

如果在生成 PDF 時遇到中文顯示問題，請確保：

1. 已正確安裝 Noto Sans CJK 字體。
2. 重新啟動了終端機或系統以確保字體安裝生效。
3. Markdown 文件使用 UTF-8 編碼保存。

如果問題仍然存在，可以嘗試使用不同的中文字體，或檢查生成的 HTML 內容以進行進一步的調試。