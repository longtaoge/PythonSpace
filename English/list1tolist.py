import re

def remove_brackets_content(text):
    # 使用正则表达式去掉所有括号及其内容
    return re.sub(r'\([^()]*\)', '', text)

def extract_first_column_words(txt_path, output_file):
    # 打开TXT文件
    with open(txt_path, 'r') as file:
        lines = file.readlines()
        
        # 提取每一行的第一列单词
        first_column_words = []
        for line in lines:
            # 去掉括号中的内容
            cleaned_line = remove_brackets_content(line.strip())
            # 按空格或制表符分割行，取第一列
            columns = cleaned_line.split()
            if columns:  # 确保行不为空
                first_column_words.append(columns[0])
        
        # 将第一列单词写入到指定的输出文件中
        with open(output_file, 'w') as out_file:
            for word in first_column_words:
                out_file.write(word + '\n')

    print(f"第一列单词已提取并保存到 {output_file}")

# 指定TXT文件路径和输出文件路径
txt_path = 'english/2265.txt'  # 替换为你的TXT文件路径
output_file = 'english/2265_1.txt'  # 替换为你想保存单词列表的文件路径

# 调用函数提取第一列单词并保存到文件
extract_first_column_words(txt_path, output_file)