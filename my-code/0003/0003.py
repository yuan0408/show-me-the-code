import redis
import random


def generateCode(generateNum: int, codeLen: int) -> list:
    """生成指定数量和指定长度的激活码

    Args:
        generateNum (int): 生成激活码的数量
        codeLen (int): 每个激活码的长度

    Returns:
        list: 生成的激活码列表
    """
    elements = [str(i) for i in range(10)]
    elements.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
    elements.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    return [
        ''.join([
            elements[random.randint(0,
                                    len(elements) - 1)] for i in range(codeLen)
        ]) for j in range(generateNum)
    ]


if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    codes = generateCode(200, 10)
    for i, code in enumerate(codes):
        r.hset('show_me_the_code_0003', i, code)
