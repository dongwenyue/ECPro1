# -*- coding: utf-8 -*-

def get_color_size_index(index: int, color_len, size_len):
    color_index, size_index = 0, 0
    if index != 0:
        color_index = int(index / size_len)

        # size_index = int(index - color_index * color_len)
    return color_index, size_index
def test_get_color_size_index():
    assert [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] == [
        get_color_size_index(index, 3, 3) for index in range(9)]

    print([get_color_size_index(index, 2, 4) for index in range(8)])
    # print([get_color_size_index(index, 4, 2) for index in range(8)])


def test(color_num, size_num):
    num = 0
    data = {}
    for i in range(int(color_num)):
        for k in range(int(size_num)):
            num += 1
            data[num] = [i,k]
    return data