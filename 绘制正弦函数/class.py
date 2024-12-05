"""
Animal类，动物的基本类型

属性包括
- name, 动物的名字
- age, 动物的年龄

方法
- make_sound()，打印出动物的叫声
- move()，打印出动物的移动方式
"""

class Animal:
    """Animal类，动物的基本类型

    属性包括
    - name, 动物的名字
    - age, 动物的年龄

    方法
    - make_sound()，打印出动物的叫声
    - move()，打印出动物的移动方式
    """

    def __init__(self, name, age):
        """初始化动物的名字和年龄"""
        self.name = name
        self.age = age

    def make_sound(self):
        """打印出动物的叫声"""
        print(f"{self.name} 发出声音。")

    def move(self):
        """打印出动物的移动方式"""
        print(f"{self.name} 正在移动。")

# 示例用法
if __name__ == "__main__":
    dog = Animal("小狗", 3)
    dog.make_sound()  # 输出: 小狗 发出声音。
    dog.move()        # 输出: 小狗 正在移动。
