import pandas as pd
import re

def clean_numeric_data(input_file, output_file, column_names):
    """
    处理 CSV 文件中多个指定列的数字数据
    
    参数:
    input_file (str): 输入 CSV 文件路径
    output_file (str): 输出 CSV 文件路径
    column_names (list): 要处理的列名列表
    """
    # 读取 CSV 文件
    df = pd.read_csv(input_file)
    
    def convert_to_number(value):
        # 如果已经是数字，直接返回
        if isinstance(value, (int, float)) and not pd.isna(value):
            return float(value)
        
        # 如果是空值，返回 0
        if pd.isna(value) or str(value).strip() == '':
            return 0.0
            
        # 转换为字符串并移除空白
        value = str(value).strip()
        
        try:
            # 处理会计格式 (例如: (123.45) 表示负数)
            if value.startswith('(') and value.endswith(')'):
                value = '-' + value[1:-1]
            
            # 移除常见的非数字字符（如千位分隔符、货币符号）
            value = re.sub(r'[^\d.-]', '', value)
            
            # 如果是空字符串或只包含符号，返回 0
            if value == '' or value == '-' or value == '.':
                return 0.0
                
            # 转换为浮点数
            return float(value)
        except (ValueError, TypeError):
            # 如果转换失败，返回 0
            return 0.0
    
    # 检查所有指定列是否存在
    missing_cols = [col for col in column_names if col not in df.columns]
    if missing_cols:
        raise KeyError(f"文件中不存在以下列：{', '.join(missing_cols)}")
    
    # 对每个指定列应用转换
    for column_name in column_names:
        df[column_name] = df[column_name].apply(convert_to_number)
    
    # 保存处理后的数据到新文件
    df.to_csv(output_file, index=False)
    print(f"处理完成，结果已保存到 {output_file}")

# 使用示例
if __name__ == "__main__":
    try:
        clean_numeric_data(
            input_file="/QT/file/Table.csv",
            output_file="/QT/file/Table_output.csv",
            column_names=["DX", "数5日内", "涨幅%"]  # 处理多个列
        )
    except FileNotFoundError:
        print("错误：找不到输入文件")
    except KeyError as e:
        print(f"错误：{str(e)}")
    except Exception as e:
        print(f"发生错误：{str(e)}")


     
 