import numpy as np


def read_dat(path, shape, dtype):
    """读取无文件头的二进制 DAT 文件，返回 NumPy 数组。

    shape 按数组轴顺序指定，二维数据为 (行数, 列数)，按行排列。
    dtype 指定数值类型和字节序，例如 ">u2" 为大端序无符号 16 位整数。
    """
    return np.fromfile(path, dtype=dtype).reshape(shape)
