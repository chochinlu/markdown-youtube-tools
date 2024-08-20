# Markdown 轉 PDF 工具

這個工具可以將 Markdown 檔案轉換為 PDF 格式。

## 安裝依賴

在使用此工具之前，請確保已安裝所需的 Python 套件：

```bash
pip install markdown reportlab xhtml2pdf
```

## 使用方法

基本用法：

```bash
python markdown_to_pdf.py 輸入檔案路徑 [-o 輸出檔案路徑]
```

例如：

```bash
python markdown_to_pdf.py 文件.md -o 輸出.pdf
```

如果不指定輸出檔案路徑，程序會自動將 PDF 檔案保存在 `exports` 資料夾中，檔名與輸入檔案相同（副檔名改為 .pdf）。

## 查詢檔案完整路徑

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

## 注意事項

- 確保輸入檔案是有效的 Markdown 格式（.md 或 .markdown 副檔名）。
- 如果指定的輸出目錄不存在，程序會自動創建。
- 轉換過程中如遇到錯誤，程序會顯示相應的錯誤訊息。