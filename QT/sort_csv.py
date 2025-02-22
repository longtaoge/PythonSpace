import pandas as pd

def sort_csv_data(input_file, output_file, 
                 sort_columns, ascending_orders,
                 encoding='utf-8'):
    """
    多列排序 CSV 文件
    
    参数:
    input_file (str): 输入文件路径
    output_file (str): 输出文件路径
    sort_columns (list): 排序字段列表，如 ['列名1', '列名2']
    ascending_orders (list): 排序方向列表，如 [True, False]
    encoding (str): 文件编码格式 (默认 utf-8)
    """
    try:
        # 读取 CSV 文件
        df = pd.read_csv(input_file, encoding=encoding)
        print(f"成功读取文件: {input_file} (共 {len(df)} 条记录)")
        
        # 验证参数有效性
        if len(sort_columns) != len(ascending_orders):
            raise ValueError("排序字段与排序方向数量不匹配")
            
        for col in sort_columns:
            if col not in df.columns:
                raise KeyError(f"列 '{col}' 不存在")
        
        # 执行多列排序
        sorted_df = df.sort_values(
            by=sort_columns,
            ascending=ascending_orders,
            na_position='last'  # 空值排在最后
        )
        
        # 保存排序结果
        sorted_df.to_csv(output_file, index=False, encoding=encoding)
        print(f"排序结果已保存至: {output_file}")
        
        # 打印排序后首尾数据
        print("\n排序后前 3 条记录:")
        print(sorted_df.head(3).to_string(index=False))
        print("\n排序后最后 3 条记录:")
        print(sorted_df.tail(3).to_string(index=False))
        
        return True
    
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 不存在")
    except pd.errors.EmptyDataError:
        print("错误：文件为空或格式不正确")
    except Exception as e:
        print(f"运行时错误：{str(e)}")
    return False

# 示例使用
if __name__ == "__main__":
    # 文件配置
    input_file = "QT/file/test_filter.csv"    # 输入文件路径
    output_file = "QT/file/test_sort.csv"  # 输出文件路径
    file_encoding = "utf-8"           # 中文常用编码
    
    # 排序参数配置
    sort_columns = ['评测公式', '胜率(%)','年化收益率(%)']  # 先按部门升序，再按销售额降序
    ascending_orders = [True, False,False]  # 每个字段的排序方向


 
    # 执行排序
    success = sort_csv_data(
        input_file=input_file,
        output_file=output_file,
        sort_columns=sort_columns,
        ascending_orders=ascending_orders,
        encoding=file_encoding
    )
    
    if success:
        print("\n排序完成！")
    else:
        print("\n排序过程中出现错误")