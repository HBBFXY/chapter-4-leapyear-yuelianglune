def is_leap_year(year):
    """判断是否为闰年的函数"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def main():
    print("闰年判断程序")
    print("============")
    
    while True:
        try:
            # 获取用户输入
            user_input = input("请输入一个年份（输入'quit'退出程序）: ")
            
            # 检查是否退出程序
            if user_input.lower() == 'quit':
                print("感谢使用，再见！")
                break
                
            # 尝试将输入转换为整数
            year = int(user_input)
            
            # 检查年份是否为正数
            if year <= 0:
                print("错误：请输入一个有效的正数年份。\n")
                continue
                
            # 判断是否为闰年并显示结果
            if is_leap_year(year):
                print(f"{year}年是闰年。\n")
            else:
                print(f"{year}年不是闰年。\n")
                
        except ValueError:
            # 处理非数字输入
            print("错误：请输入有效的数字年份。\n")

if __name__ == "__main__":
    main()
