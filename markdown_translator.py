import argparse
import os
from openai import OpenAI
from markdown import markdown
from weasyprint import HTML, CSS
import dotenv

# 載入 .env 檔案中的環境變數
dotenv.load_dotenv()

client = OpenAI()

def translate_markdown(input_file, output_file, to_pdf=False):
    # 讀取 Markdown 文件
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用 OpenAI API 進行翻譯
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a translator. Translate the given English text to Traditional Chinese. Keep the original English text and add the Chinese translation after each line or paragraph."},
            {"role": "user", "content": content}
        ]
    )

    translated_content = response.choices[0].message.content

    # 寫入翻譯後的 Markdown 文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_content)

    print(f"翻譯後的 Markdown 文件已保存為：{output_file}")

    # 如果需要轉換為 PDF
    if to_pdf:
        pdf_file = os.path.splitext(output_file)[0] + '.pdf'
        html_content = markdown(translated_content)
        
        # 定義 CSS 樣式，包括中文字體
        css = CSS(string='''
            @font-face {
                font-family: 'NotoSansCJK';
                src: url('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc');
            }
            body {
                font-family: 'Noto Sans CJK TC', 'Noto Sans CJK SC', 'Noto Sans CJK JP', 'Noto Sans CJK KR', sans-serif;
            }
        ''')
        
        # 生成 PDF
        HTML(string=html_content).write_pdf(pdf_file, stylesheets=[css])
        
        print(f"PDF 文件已生成：{pdf_file}")

def main():
    parser = argparse.ArgumentParser(description='將 Markdown 文件翻譯成中英文對照版本')
    parser.add_argument('input_file', help='輸入的 Markdown 文件路徑')
    parser.add_argument('-o', '--output', help='輸出的 Markdown 文件名稱')
    parser.add_argument('--pdf', action='store_true', help='同時生成 PDF 文件')
    args = parser.parse_args()

    input_file = args.input_file
    if args.output:
        output_file = args.output if args.output.endswith('.md') else args.output + '.md'
    else:
        output_file = os.path.splitext(os.path.basename(input_file))[0] + '_translated.md'
    
    output_file = os.path.join('exports', output_file)

    # 確保 exports 資料夾存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    translate_markdown(input_file, output_file, args.pdf)

if __name__ == '__main__':
    main()