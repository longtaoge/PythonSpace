import PyPDF2
import re
from spellchecker import SpellChecker

def extract_and_filter_words(pdf_path, output_file):
    # 初始化拼写检查器
    spell = SpellChecker()

    # 打开PDF文件
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        
        # 读取每一页的内容
        for page in reader.pages:
            text += page.extract_text()
        
        # 使用正则表达式提取单词（仅字母组成的单词）
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        # 过滤掉拼写错误的单词、数字和单字母单词
        valid_words = []
        for word in words:
            # 检查单词是否拼写正确、不是单字母单词且不是数字
            if len(word) > 1 and word.lower() in spell:
                valid_words.append(word.lower())  # 统一转换为小写
        
        # 将有效单词写入到指定的输出文件中
        with open(output_file, 'w') as out_file:
            for word in valid_words:
                out_file.write(word + '\n')

    print(f"有效单词已提取并保存到 {output_file}")

 
# 指定PDF文件路径和输出文件路径
pdf_path = 'english/example.pdf'  # 替换为你的PDF文件路径
output_file = 'english/filtered_word_list.txt'  # 替换为你想保存单词列表的文件路径

# 调用函数提取单词并保存到文件
extract_and_filter_words(pdf_path, output_file)



 