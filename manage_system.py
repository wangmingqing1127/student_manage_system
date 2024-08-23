"""
    @Time ： 2023/12/13 09:42
    @Auth ： wmq
    @Company ：XXX wmq@2019.com.cn
    @Function ：管理系统类
"""
# __dict__
# 实例.__dict__：返回实例属性和值组成的字典
from student import Student


class StudentManager:

    def __init__(self):
        # 存储学员数据---列表
        self.student_list = []

    # 程序入口函数
    def run(self):
        # 1.加载文件里面的函数
        self.load_student()
        while True:
            # 2.显示功能菜单
            self.show_menu()
            # 3.用户输入目标功能序号
            num = int(input('请您输入需要的功能序号：'))
            # 4.根据用户输入的序号执行不同的功能
            if num == 1:
                # 添加学员
                self.add_student()
            elif num == 2:
                # 删除学员
                self.del_student()
            elif num == 3:
                # 修改学员
                self.modify_student()
            elif num == 4:
                # 查询学员
                self.search_student()
            elif num == 5:
                # 显示所有学员
                self.show_student()
            elif num == 6:
                # 保存学员
                self.save_student()
            elif num == 7:
                # 退出系统
                break

    # 1.加载文件里面的函数
    def load_student(self):
        # 尝试r打开文件，异常则 w 打开
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据
            data = f.read()
            # 数据转换：字符串--[{}]字典--对象[学员对象]
            dict_data = eval(data)
            self.student_list = [Student(name=i['name'], gender=i['gender'], tel=i['tel']) for i in dict_data]
        finally:
            f.close()

    # 显示功能菜单---静态方法
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1：添加学员')
        print('2：删除学员')
        print('3：修改学员')
        print('4：查询学员')
        print('5：显示所有学员')
        print('6：保存学员')
        print('7：退出系统')

    # 添加学员
    def add_student(self):
        # 1.用户输入姓名 性别 手机号
        name = input('请输入你的名字：')
        gender = input('请输入你的性别：')
        tel = input('请输入你的电话号码：')
        # 2.创建学员对象
        st = Student(name=name, gender=gender, tel=tel)
        # 3.将对象添加到学院里表中
        self.student_list.append(st)

    # 删除学员
    def del_student(self):
        # 1.用户输入目标学员姓名
        name = input('请输入要删除的学员姓名：')
        # 2.遍历学员列表，如果用户输入的学员存在则删除学员对象，否则提示不存在
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                break
        else:
            print('用户不存在')

    # 修改学员
    def modify_student(self):
        # 1.用户输入目标学员姓名
        name = input('请输入需要修改的学员姓名：')
        # 2.遍历学员列表，学员姓名存在则修改姓名 性别 手机号，否则提示学员信息不存在
        for i in self.student_list:
            if i.name == name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                print(f'学员的基本信息如下：姓名是：{i.name}，性别是：{i.gender}，电话是：{i.tel}')
                break
        else:
            print('学员不存在')

    # 查询学员
    def search_student(self):
        # 1.用户输入需要查询的学员姓名
        name = input('请输入需要查询的学员姓名：')
        # 2.遍历学员列表，学员姓名存在则显示姓名 性别 手机号，否则提示学员信息不存在
        for i in self.student_list:
            if name == i.name:
                print(f'学员的基本信息如下：姓名是：{i.name}，性别是：{i.gender}，电话是：{i.tel}')
                break
        else:
            print('学员不存在')

    # 显示所有学员
    def show_student(self):
        # 遍历学员列表 打印学员信息
        for i in self.student_list:
            print(f'学员的基本信息：姓名是：{i.name}，性别是：{i.gender}，电话是：{i.tel}')

    # 保存学员
    def save_student(self):
        # 1.打开文件
        f = open('student.data', 'w')
        # 2.文件写入：
        # 2.1 文件写入的数据不能是学员对象的内存地址，把数据转换成列表字典数据[学员对象]转换[字典]
        data = [i.__dict__ for i in self.student_list]
        # 2.2 文件数据要求为字符串类型，需要数据转换
        f.write(str(data))
        # 3.文件关闭
        f.close()
