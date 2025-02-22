def split_words_into_groups(txt_path, output_file, group_size=500):
    # 打开TXT文件
    with open(txt_path, 'r') as file:
        # 读取所有内容并按空格分割成单词列表
        words = file.read().split()
        
        # 将单词分成每组500个
        groups = [words[i:i + group_size] for i in range(0, len(words), group_size)]
        
        # 将每组单词用逗号分隔并写入输出文件
        with open(output_file, 'w') as out_file:
            for group in groups:
                out_file.write(','.join(group) + '\n')

    print(f"单词已分组并保存到 {output_file}")

# 指定TXT文件路径和输出文件路径
txt_path = 'IELTS/2265.txt'  # 替换为你的TXT文件路径
output_file = 'IELTS/grouped_words.txt'  # 替换为你想保存分组单词的文件路径

# 调用函数分组单词并保存到文件
split_words_into_groups(txt_path, output_file)