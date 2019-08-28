import pickle
class guanliyuan:

    def register(self,name,pwd):
        self.name = name
        self.pwd = pwd
        struct_data = {'name': self.name, 'pwd': self.pwd}
        self.data = pickle.dumps(struct_data)
        return self.data

    def login(self):
        user.name = input('请输入你的名字:').strip()
        user.pwd = input('请输入你的密码:').strip()
        data = pickle.loads(self.data)
        print(data, type(data))
        if  user.name == data['name'] and user.pwd == data['pwd']:
            return True, '登录成功'
        return False, '登录失败'

user = guanliyuan()
user1 = user.register('sean', '123')
print(user1)

user2 = user.login()
print(user2)




