"""
    @Time ： 2023/12/13 09:42
    @Auth ： wmq
    @Company ：XXX wmq@2019.com.cn
    @Function ：学生类
"""


class Student(object):
    # 学员信息：姓名 性别 手机号
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    # 添加__str__魔法方法，方便查看学员对象信息
    def __str__(self):
        return f'学员的基本信息如下：姓名是：{self.name}，性别是：{self.gender}，电话是：{self.tel}'


if __name__ == '__main__':
    st = Student('小明', '男', '13777777777')
    print(st)
