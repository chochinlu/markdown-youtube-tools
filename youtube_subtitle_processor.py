import sys
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def download_youtube_subtitle(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        return formatted_transcript
    except Exception as e:
        print(f"無法抓取字幕：{str(e)}")
        return None

def main():
    if len(sys.argv) < 2:
        print("使用方法: python youtube_subtitle_processor.py <YouTube影片ID> [輸出文件名(不含副檔名)]")
        sys.exit(1)

    video_id = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else "output"

    # 下載 YouTube 字幕
    subtitle = download_youtube_subtitle(video_id)
    if subtitle is None:
        sys.exit(1)

    # 將字幕保存為 Markdown 文件
    input_file = f"./exports/{output_name}_subtitle.md"
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(subtitle)

    print(f"字幕已保存為 Markdown 文件：{input_file}")

    # 執行 markdown_translator.py
    subprocess.run(["python", "markdown_translator.py", input_file, "-o", output_name])

    # 執行 markdown_to_pdf.py
    translated_md = f"./exports/{output_name}.md"
    subprocess.run(["python", "markdown_to_pdf.py", translated_md])

    print(f"翻譯和轉換完成。PDF 文件已生成: exports/{output_name}.pdf")

if __name__ == "__main__":
    main()