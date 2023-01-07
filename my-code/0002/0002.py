import random
import mysql.connector


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
    user = input('input the user of mysql:')
    psw = input('input the password of mysql: ')
    database = input('input the database of mysql: ')
    conn = mysql.connector.connect(user=user,
                                   password=psw,
                                   database=database)
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists codes(id int auto_increment primary key,code varchar(20) not null)'
    )

    codes = generateCode(200, 10)
    for code in codes:
        cursor.execute('insert into codes(code) values(%s)', [code])

    conn.commit()
    conn.close()
