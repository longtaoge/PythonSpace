import pandas as pd
from datetime import datetime

def filter_csv_data(input_file, output_file, condition, encoding='utf-8'):
    """
    从 CSV 文件中筛选数据并保存结果
    
    参数:
    input_file (str): 输入 CSV 文件路径
    output_file (str): 输出 CSV 文件路径
    condition (callable): 接收 DataFrame 返回布尔序列的筛选函数
    encoding (str): 文件编码格式 (默认 utf-8)
    """
    try:
        # 读取 CSV 文件
        df = pd.read_csv(input_file, encoding=encoding)
        
        # 原始数据统计
        original_count = len(df)
        print(f"已加载 {original_count} 条原始记录")
        
        # 应用筛选条件
        filtered_df = df[condition(df)]
        
        # 筛选结果统计
        filtered_count = len(filtered_df)
        print(f"找到 {filtered_count} 条匹配记录 (留存率 {filtered_count/original_count:.1%})")
        
        # 保存结果
        filtered_df.to_csv(output_file, index=False, encoding=encoding)
        print(f"结果已保存至: {output_file}")
        
        return True
    
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 不存在")
    except KeyError as e:
        print(f"列名错误：{e} 列不存在")
    except Exception as e:
        print(f"运行时错误：{str(e)}")
    return False

# 示例使用
if __name__ == "__main__":

  
    # 文件配置
    input_csv = "QT/file/test.csv"      # 输入文件路径
    output_csv = "QT/file/test_filter.csv"   # 输出文件路径
    file_encoding = "utf-8"     # 根据实际情况调整编码 (如 gbk, latin1 等)
    
    # 自定义筛选条件函数
    def custom_condition(df):
        """示例筛选条件："""
        return (
            (df['胜率(%)'] >= 75) &                      # 数值比较
            (df['年化收益率(%)'] >10     )         # 多值筛选
             )
    
    # 执行筛选
    success = filter_csv_data(
        input_file=input_csv,
        output_file=output_csv,
        condition=custom_condition,
        encoding=file_encoding
    )
    
    if success:
        print("筛选操作成功完成")
    else:
        print("筛选过程中出现错误")

 

   




   
 
    
    