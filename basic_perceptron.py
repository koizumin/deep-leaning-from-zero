"""
2.3 パーセプトロンの実装
"""

import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    weighted_biased = np.sum(x * w) + b
    return 1 if weighted_biased > 0 else 0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4

    weighted_biased = np.sum(x * w) + b
    return 1 if weighted_biased > 0 else 0


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    weighted_biased = np.sum(x * w) + b
    return 1 if weighted_biased > 0 else 0


def XOR(x1, x2):
    """
    パーセプトロンは線形に出力を決定するので単層では実装できない
    しかし、複数の層を組み合わせることで実装できる
    """

    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


def assert_equal(actual, expected):
    result = 'success' if actual == expected else 'failed'
    print(f"{result}: {actual} = {expected}")


if __name__ == '__main__':
    print("AND")
    assert_equal(AND(0, 0), 0)
    assert_equal(AND(1, 0), 0)
    assert_equal(AND(0, 1), 0)
    assert_equal(AND(1, 1), 1)

    print("OR")
    assert_equal(OR(0, 0), 0)
    assert_equal(OR(1, 0), 1)
    assert_equal(OR(0, 1), 1)
    assert_equal(OR(1, 1), 1)

    print("NAND")
    assert_equal(NAND(0, 0), 1)
    assert_equal(NAND(1, 0), 1)
    assert_equal(NAND(0, 1), 1)
    assert_equal(NAND(1, 1), 0)

    print("XOR")
    assert_equal(XOR(0, 0), 0)
    assert_equal(XOR(1, 0), 1)
    assert_equal(XOR(0, 1), 1)
    assert_equal(XOR(1, 1), 0)
