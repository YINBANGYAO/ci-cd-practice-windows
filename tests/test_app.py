from app.app import dedupe, dedupe_with_key, add

def test_dedupe():
    """测试去重功能"""
    assert dedupe([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert dedupe(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert dedupe([]) == []
def test_dedupe_with_key():
    """测试带key函数的去重"""
    data = [{'x': 1}, {'x': 2}, {'x': 1}]
    result = list(dedupe_with_key(data, key=lambda d: d['x']))
    assert len(result) == 2
    assert result[0]['x'] == 1
    assert result[1]['x'] == 2
def test_add():
    """测试加法功能"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0