shopping_cart = {}
while True:
    print("""
    ########### 购物车系统 ###########
    #           1.添加购物车         #
    #           2.修改购物车         #
    #           3.删除购物车         #
    #           4.查询购物车         #
    #           5.退出购物车         #
    """)
    user_choice = input("请输入你要使用的功能的数字")
    match user_choice:
        case "1":
            user_name = input("请输入商品名称")
            user_price = input("请输入商品价格")
            user_num = input("请输入商品数量")
            if user_name not in shopping_cart:
                shopping_cart[user_num] = {"price": user_price, "num": user_num}
                print("已将商品添加到购物车内")
            else:
                print("输入的商品已在购物车内")
        case "2":
            user_name = input("请输入商品名称")
            if user_name in shopping_cart:
                user_price = input("请输入商品价格")
                user_num = input("请输入商品数量")
                shopping_cart[user_name] = {"price": user_price, "num": user_num}
                print("已将商品修改")
            else:
                print("你要修改的商品不在购物车内")
        case "3":
            user_name = input("请输入商品名称")
            if user_name in shopping_cart:
                del shopping_cart[user_name]
                print("已将商品从购物车中删除")
            else:
                print("你要删除的商品不在购物车内")
        case "4":
            user_name = input("请输入商品名称")
            if user_name in shopping_cart:
                print(shopping_cart[user_name])
            else:
                print("你要查询的商品不在购物车里")
        case "5":
            print("再见")
            break
