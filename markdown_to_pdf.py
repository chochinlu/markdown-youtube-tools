import argparse
import os
from markdown import markdown
from weasyprint import HTML, CSS

def is_markdown_file(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in ['.md', '.markdown']

def convert_markdown_to_pdf(input_file, output_file):
    if not is_markdown_file(input_file):
        print("錯誤：輸入檔案不是 Markdown 格式。")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    html_content = markdown(markdown_content)

    # 確保 exports 資料夾存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 定義 CSS 樣式，包括中文字體
    css = CSS(string='''
        @font-face {
            font-family: 'Noto Sans CJK TC';
            src: local('Noto Sans CJK TC'), local('Noto Sans CJK SC'), local('Noto Sans CJK JP'), local('Noto Sans CJK KR');
        }
        body {
            font-family: 'Noto Sans CJK TC', sans-serif;
        }
    ''')

    # 生成 PDF
    HTML(string=html_content).write_pdf(output_file, stylesheets=[css])

    print(f"PDF 已成功生成：{output_file}")

def main():
    parser = argparse.ArgumentParser(description='將 Markdown 檔案轉換為 PDF')
    parser.add_argument('input_file', help='輸入的 Markdown 檔案路徑')
    parser.add_argument('-o', '--output', help='輸出的 PDF 檔案路徑')
    args = parser.parse_args()

    input_file = args.input_file
    if args.output:
        output_filename = args.output if args.output.endswith('.pdf') else args.output + '.pdf'
    else:
        output_filename = os.path.splitext(os.path.basename(input_file))[0] + '.pdf'
    
    output_file = os.path.join('exports', output_filename)

    convert_markdown_to_pdf(input_file, output_file)

if __name__ == '__main__':
    main()