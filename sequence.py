def test_distinct(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False
print(test_distinct([1,5,7,0]))
print(test_distinct([2,7,5,5,7,0]))
