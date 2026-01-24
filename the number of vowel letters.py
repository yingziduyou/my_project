def vowel_letters(letters):
    """
    用来判断一个字母字符串有几个元音字母
    :param letters: 需要判断的字符串
    :return: 元音字母的数量
    """
    num = 0
    for i in letters:
        if i in "aeiouAEIOU":
            num += 1
    return print(num)


vowel_letters("fuisheiu")
