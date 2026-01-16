# 定义一个函数，根据传入的分数，计算对应的分数等级并返回
def score_grade(score):
    """
    这是一个根据传入的分数，计算对应的分数等级并返回
    :param score: 分数
    :return: 分数所在等级
    """
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score < 60:
        return 'D'


print(score_grade(90))
print(score_grade(80))
print(score_grade(65))
print(score_grade(55))
