import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("使用方法: python translate_and_convert.py <輸入的Markdown文件路徑> [輸出文件名(不含副檔名)]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "output"

    # 執行 markdown_translator.py
    subprocess.run(["python", "markdown_translator.py", input_file, "-o", output_name])

    # 執行 markdown_to_pdf.py
    translated_md = f"./exports/{output_name}.md"
    subprocess.run(["python", "markdown_to_pdf.py", translated_md])

    print(f"翻譯和轉換完成。PDF 文件已生成: exports/{output_name}.pdf")

if __name__ == "__main__":
    main()