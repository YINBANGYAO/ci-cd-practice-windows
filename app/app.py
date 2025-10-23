def dedupe(items):
    """去重函数 - 保留顺序"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
def dedupe_with_key(items, key=None):
    """支持key函数的去重"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 更新main函数测试新功能
if __name__ == "__main__":
    # ... 原有测试代码 ...
    
    # 测试带key函数的去重
    sample_dicts = [{'x': 1}, {'x': 2}, {'x': 1}]
    result = list(dedupe_with_key(sample_dicts, key=lambda d: d['x']))
    print(f"字典去重: {result}")
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