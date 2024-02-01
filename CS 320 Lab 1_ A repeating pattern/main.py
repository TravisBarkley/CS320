def repeat(list):
    if list is None:
        return None
    
    if len(list) < 3:
        return None
    
    max_len = len(list)
    for pat_len in range(max_len // 2, 0, -1):
        if max_len % pat_len == 0:
            pattern = list[0:pat_len] 
            is_valid_pat = all(list[i:i + pat_len] == pattern for i in range(0, max_len, pat_len))
            if is_valid_pat:
                return pattern
            
    return None


# odd length/pattern test 
def test_odd():
    assert repeat(['a', 'b', 'c']) is None
    assert repeat(['a', 'b', 'a', 'b', 'a']) is None
    assert repeat(['a', 'b', 'c', 'a', 'b', 'c']) == ['a', 'b', 'c']
    assert repeat(['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == ['a', 'b', 'c']
    assert repeat(['a', 'b', 'c', 'a', 'b', 'c', 'f']) is None


def test_odd_length_pattern():
    assert repeat(['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y']) is None
    assert repeat(['1', '2', '3', '4', '1', '2', '3', '4']) == ['1', '2', '3', '4']
    assert repeat(['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']) == ['A', 'B', 'C', 'D']
    assert repeat(['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green']) is None


def test_repeat_function():
    assert repeat(['a', 'b', 1, 'b', 'a', 'b', 1, 'b']) == ['a', 'b', 1, 'b']
    assert repeat(['a', 'b', 'a', 'b', 'a', 'b', 'c']) is None
    assert repeat([1]) is None
    assert repeat(None) is None


test_repeat_function()
test_odd_length_pattern()
test_odd()
