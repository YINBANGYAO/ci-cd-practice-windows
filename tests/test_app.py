from app.app import dedupe, add

def test_dedupe():
    """测试去重功能"""
    assert dedupe([1, 2, 3, 2, 1]) == [1, 2, 3]
    assert dedupe(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']
    assert dedupe([]) == []

def test_add():
    """测试加法功能"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0