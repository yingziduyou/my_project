num = 1
print(num)


def score(score_list):
    """
    计算成绩的最高分，最低分，平均分
    :param score_list: 成绩列表
    :return: 最高分，最低分，平均分
    """
    num=100
    print(f"局部变量num={num}")
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list))
    return max_score, min_score, avg_score


print(score([1, 2, 3, 4, 5]))
print(f"全局变量num={num}")

def new_num(newnum):
    """
    修改全局变量num
    :return:
    """
    global num
    num= newnum
print(num)
new_num(100)
print(num)


