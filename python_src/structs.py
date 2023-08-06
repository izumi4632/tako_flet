from random import randint, sample


class RandNum:
    """
    start と end (両方含む) の間のランダムな整数を生成するクラス。

    Attributes:
    start (int): ランダム整数の下限。
    end (int): ランダム整数の上限。

    Returns:
    int: start と end (両方含む) の間のランダムな整数。
    """

    def __init__(self, start, end) -> int:
        self.res = randint(start, end)


class RandNumArray:
    """
    start と end (両方含む) の間のランダムな整数の配列を生成するクラス。

    Attributes:
    start (int): ランダム整数の下限。
    end (int): ランダム整数の上限。
    length (int): 配列の長さ。

    Returns:
    list: start と end (両方含む) の間のランダムな整数の配列。
    """

    def __init__(self, start, end, length) -> list:
        self.res = [RandNum(start, end).res for _ in range(length)]


class PermOfRandRange:
    """
    start と end (両方含む) の間の整数のランダムな順列を生成するクラス。

    Attributes:
    start (int): 整数の下限。
    end (int): 整数の上限。

    Returns:
    list: start と end (両方含む) の間の整数のランダムな順列。
    """

    def __init__(self, start, end) -> list:
        self.res = sample(list(range(start, end + 1)), end + 1 - start)


class UniRandNumArray:
    """
    start と end (endは含まない) の間のユニークなランダムな整数の配列を生成するクラス。

    Attributes:
    start (int): ランダム整数の下限。
    end (int): ランダム整数の上限。
    length (int): 配列の長さ。

    Returns:
    list: start と end (endは含まない) の間のユニークなランダムな整数の配列。
    """

    def __init__(self, start, end, length) -> list:
        self.res = sample(list(range(start, end)), length)
