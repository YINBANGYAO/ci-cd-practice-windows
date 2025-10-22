def dedupe(items):
    """去重函数 - 保留顺序"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def add(a, b):
    """加法函数 - 新增功能"""
    return a + b

if __name__ == "__main__":
    # 测试去重功能
    sample_list = [1, 2, 3, 2, 1, 4, 5, 4]
    result = dedupe(sample_list)
    print(f"原始列表: {sample_list}")
    print(f"去重后: {result}")
    
    # 测试加法功能
    print(f"加法测试: 2 + 3 = {add(2, 3)}")