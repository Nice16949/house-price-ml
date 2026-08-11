class HealthManager(object):
    # 初始化
    def __init__(self):
        self.user_list = []         # 用户列表（对应用户管理模块）
        self.health_list = []       # 健康记录列表（对应健康数据模块）
        self.sport_list = []        # 运动记录列表（对应运动数据模块）
        self.current_user = None    # 当前登录用户
        self.sport_target = 150     # 默认每周运动目标（分钟）

    # ===================== 菜单部分（对应系统辅助模块） =====================
    # 登录注册菜单
    @staticmethod
    def show_login_menu():
        print('=' * 30)
        print('大学生健康管理系统 V1.0')
        print('1. 用户登录')
        print('2. 用户注册')
        print('3. 退出系统')
        print('=' * 30)

    # 系统主菜单（对应5大模块入口）
    @staticmethod
    def show_main_menu():
        print('=' * 30)
        print('1. 个人信息管理')
        print('2. 健康数据管理')
        print('3. 运动数据管理')
        print('4. 数据统计分析')
        print('5. 保存所有数据')
        print('6. 系统帮助')
        print('7. 退出登录')
        print('=' * 30)

    # 健康数据子菜单
    @staticmethod
    def show_health_menu():
        print('-' * 26)
        print('1. 添加健康记录')
        print('2. 删除健康记录')
        print('3. 修改健康记录')
        print('4. 查询健康记录')
        print('5. 显示全部记录')
        print('6. 返回主菜单')
        print('-' * 26)

    # 运动数据子菜单
    @staticmethod
    def show_sport_menu():
        print('-' * 26)
        print('1. 添加运动打卡')
        print('2. 删除运动记录')
        print('3. 修改运动记录')
        print('4. 查询运动记录')
        print('5. 显示全部记录')
        print('6. 设置运动目标')
        print('7. 返回主菜单')
        print('-' * 26)

    # ===================== 系统运行主逻辑 =====================
    def run(self):
        # 启动时加载所有历史数据
        self.load_users()
        self.load_health()
        self.load_sport()

        while True:
            self.show_login_menu()
            choice = input('请输入功能序号：')
            if choice == '1':
                self.user_login()
                # 登录成功后进入主菜单
                if self.current_user:
                    self.main_loop()
            elif choice == '2':
                self.user_register()
            elif choice == '3':
                print('谢谢使用！')
                break
            else:
                print('输入有误！')

    # 登录后主循环
    def main_loop(self):
        while True:
            print(f'\n当前登录用户：{self.current_user.name}（学号：{self.current_user.stu_id}）')
            self.show_main_menu()
            choice = input('请输入功能序号：')
            if choice == '1':
                self.user_info_manage()
            elif choice == '2':
                self.health_manage()
            elif choice == '3':
                self.sport_manage()
            elif choice == '4':
                self.data_analysis()
            elif choice == '5':
                self.save_all()
            elif choice == '6':
                self.show_help()
            elif choice == '7':
                self.current_user = None
                print('已退出登录')
                break
            else:
                print('输入有误！')

    # ===================== 1. 用户管理模块方法 =====================
    # 用户注册
    def user_register(self):
        stu_id = input('请输入学号：')
        # 校验学号是否已存在
        for user in self.user_list:
            if user.stu_id == stu_id:
                print('该学号已注册，请直接登录！')
                return
        password = input('请设置密码：')
        name = input('请输入姓名：')
        gender = input('请输入性别：')
        age = input('请输入年龄：')
        height = input('请输入身高（单位m）：')
        # 创建用户对象并加入列表
        new_user = User(stu_id, password, name, gender, age, height)
        self.user_list.append(new_user)
        print('注册成功！')

    # 用户登录
    def user_login(self):
        stu_id = input('请输入学号：')
        password = input('请输入密码：')
        for user in self.user_list:
            if user.stu_id == stu_id:
                if user.password == password:
                    self.current_user = user
                    print('登录成功！')
                    return
                else:
                    print('密码错误！')
                    return
        print('学号不存在，请先注册！')

    # 个人信息管理
    def user_info_manage(self):
        print('\n当前个人信息：')
        print(self.current_user)
        print('1. 修改基本信息')
        print('2. 修改密码')
        print('3. 返回')
        choice = input('请选择：')
        if choice == '1':
            self.current_user.name = input('请输入新姓名：')
            self.current_user.gender = input('请输入新性别：')
            self.current_user.age = input('请输入新年龄：')
            self.current_user.height = input('请输入新身高：')
            print('信息修改成功！')
        elif choice == '2':
            old_pwd = input('请输入原密码：')
            if old_pwd != self.current_user.password:
                print('原密码错误！')
                return
            new_pwd = input('请输入新密码：')
            self.current_user.password = new_pwd
            print('密码修改成功！')

    # ===================== 2. 健康数据管理模块方法 =====================
    def health_manage(self):
        while True:
            self.show_health_menu()
            choice = input('请输入功能序号：')
            if choice == '1':
                self.add_health()
            elif choice == '2':
                self.del_health()
            elif choice == '3':
                self.modify_health()
            elif choice == '4':
                self.search_health()
            elif choice == '5':
                self.show_all_health()
            elif choice == '6':
                break
            else:
                print('输入有误！')

    # 添加健康记录
    def add_health(self):
        date = input('请输入记录日期（如2026-06-18）：')
        weight = input('请输入体重（kg）：')
        sleep = input('请输入睡眠时长（小时）：')
        water = input('请输入饮水量（ml）：')
        calorie = input('请输入当日摄入热量（千卡）：')
        record = HealthRecord(self.current_user.stu_id, date, weight, sleep, water, calorie)
        self.health_list.append(record)
        print('添加成功！')
        print(record)

    # 删除健康记录
    def del_health(self):
        date = input('请输入要删除的记录日期：')
        for record in self.health_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                self.health_list.remove(record)
                print('删除成功！')
                break
        else:
            print('未找到该日期的记录！')

    # 修改健康记录
    def modify_health(self):
        date = input('请输入要修改的记录日期：')
        for record in self.health_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                record.weight = input('请输入新体重：')
                record.sleep_hour = input('请输入新睡眠时长：')
                record.water = input('请输入新饮水量：')
                record.calorie = input('请输入新摄入热量：')
                print('修改成功！')
                print(record)
                break
        else:
            print('未找到该日期的记录！')

    # 查询健康记录
    def search_health(self):
        date = input('请输入要查询的日期：')
        for record in self.health_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                print('查询结果：')
                print(record)
                break
        else:
            print('未找到该日期的记录！')

    # 显示全部健康记录
    def show_all_health(self):
        my_records = [r for r in self.health_list if r.stu_id == self.current_user.stu_id]
        if not my_records:
            print('暂无健康记录！')
            return
        print('日期\t\t体重(kg)\t睡眠(h)\t饮水(ml)\t摄入热量(千卡)')
        for r in my_records:
            print(f'{r.date}\t{r.weight}\t\t{r.sleep_hour}\t{r.water}\t\t{r.calorie}')

    # ===================== 3. 运动数据管理模块方法 =====================
    def sport_manage(self):
        while True:
            self.show_sport_menu()
            choice = input('请输入功能序号：')
            if choice == '1':
                self.add_sport()
            elif choice == '2':
                self.del_sport()
            elif choice == '3':
                self.modify_sport()
            elif choice == '4':
                self.search_sport()
            elif choice == '5':
                self.show_all_sport()
            elif choice == '6':
                self.set_sport_target()
            elif choice == '7':
                break
            else:
                print('输入有误！')

    # 添加运动打卡
    def add_sport(self):
        date = input('请输入打卡日期：')
        print('可选运动类型：跑步、跳绳、篮球、羽毛球、健身、散步')
        sport_type = input('请输入运动类型：')
        if sport_type not in SportRecord.SPORT_CAL:
            print('不支持该运动类型！')
            return
        duration = input('请输入运动时长（分钟）：')
        record = SportRecord(self.current_user.stu_id, date, sport_type, duration)
        self.sport_list.append(record)
        print(f'打卡成功！消耗{record.calorie}千卡')

    # 删除运动记录
    def del_sport(self):
        date = input('请输入要删除的记录日期：')
        for record in self.sport_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                self.sport_list.remove(record)
                print('删除成功！')
                break
        else:
            print('未找到该日期的记录！')

    # 修改运动记录
    def modify_sport(self):
        date = input('请输入要修改的记录日期：')
        for record in self.sport_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                record.sport_type = input('请输入新运动类型：')
                record.duration = input('请输入新运动时长：')
                # 重新计算热量
                record.calorie = round(float(SportRecord.SPORT_CAL[record.sport_type]) * (float(record.duration) / 60), 1)
                print('修改成功！')
                print(record)
                break
        else:
            print('未找到该日期的记录！')

    # 查询运动记录
    def search_sport(self):
        date = input('请输入要查询的日期：')
        for record in self.sport_list:
            if record.stu_id == self.current_user.stu_id and record.date == date:
                print('查询结果：')
                print(record)
                break
        else:
            print('未找到该日期的记录！')

    # 显示全部运动记录
    def show_all_sport(self):
        my_records = [r for r in self.sport_list if r.stu_id == self.current_user.stu_id]
        if not my_records:
            print('暂无运动记录！')
            return
        print('日期\t\t运动类型\t时长(分钟)\t消耗热量(千卡)')
        for r in my_records:
            print(f'{r.date}\t{r.sport_type}\t\t{r.duration}\t\t{r.calorie}')

    # 设置运动目标
    def set_sport_target(self):
        target = input('请设置每周运动时长目标（分钟）：')
        self.sport_target = int(target)
        print(f'目标设置成功！当前每周目标：{self.sport_target}分钟')

    # ===================== 4. 数据分析模块方法（控制台统计，无第三方库） =====================
    def data_analysis(self):
        my_health = [r for r in self.health_list if r.stu_id == self.current_user.stu_id]
        my_sport = [r for r in self.sport_list if r.stu_id == self.current_user.stu_id]

        print('\n===== 健康与运动统计分析 =====')
        # 1. BMI计算
        if my_health:
            latest_weight = float(my_health[-1].weight)
            height = float(self.current_user.height)
            bmi = round(latest_weight / (height ** 2), 2)
            print(f'最新体重：{latest_weight}kg，BMI指数：{bmi}')
            if bmi < 18.5:
                print('BMI状态：偏瘦，建议增加营养摄入')
            elif 18.5 <= bmi <= 23.9:
                print('BMI状态：正常，继续保持')
            elif 24 <= bmi <= 27.9:
                print('BMI状态：偏胖，建议增加有氧运动')
            else:
                print('BMI状态：肥胖，建议制定减脂计划')

        # 2. 运动统计
        if my_sport:
            total_min = sum([float(r.duration) for r in my_sport])
            total_cal = sum([float(r.calorie) for r in my_sport])
            days = len(set([r.date for r in my_sport]))
            print(f'\n累计运动：{total_min}分钟，累计消耗：{total_cal}千卡')
            print(f'累计打卡天数：{days}天')
            # 目标完成率
            week_min = total_min / max(1, days // 7 + 1)
            rate = round(week_min / self.sport_target * 100, 1)
            print(f'周均运动：{round(week_min,1)}分钟，目标完成率：{rate}%')
        else:
            print('\n暂无运动数据，建议开始运动打卡')
        # 3. 健康建议
        print('\n健康建议：')
        if not my_sport:
            print('- 每周至少运动3次，每次30分钟以上')
        if my_health and float(my_health[-1].sleep_hour) < 7:
            print('- 睡眠时长不足，建议每日保证7-8小时睡眠')
        print('- 每日饮水量建议达到1500-2000ml')
        print('==============================\n')

    # ===================== 5. 系统辅助模块方法（文件持久化+帮助） =====================
    # 保存所有数据
    def save_all(self):
        self.save_users()
        self.save_health()
        self.save_sport()
        print('所有数据已保存！')
    # 保存用户数据
    def save_users(self):
        f = open('users.txt', 'w', encoding='utf-8')
        for user in self.user_list:
            f.write(f'{user.stu_id},{user.password},{user.name},{user.gender},{user.age},{user.height}\n')
        f.close()
    # 保存健康数据
    def save_health(self):
        f = open('health_records.txt', 'w', encoding='utf-8')
        for r in self.health_list:
            f.write(f'{r.stu_id},{r.date},{r.weight},{r.sleep_hour},{r.water},{r.calorie}\n')
        f.close()
    # 保存运动数据
    def save_sport(self):
        f = open('sport_records.txt', 'w', encoding='utf-8')
        for r in self.sport_list:
            f.write(f'{r.stu_id},{r.date},{r.sport_type},{r.duration},{r.calorie}\n')
        f.close()
    # 加载用户数据
    def load_users(self):
        try:
            f = open('users.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            return
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            sid, pwd, name, gender, age, height = line.split(',')
            self.user_list.append(User(sid, pwd, name, gender, age, height))
        f.close()
    # 加载健康数据
    def load_health(self):
        try:
            f = open('health_records.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            return
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            sid, date, weight, sleep, water, cal = line.split(',')
            self.health_list.append(HealthRecord(sid, date, weight, sleep, water, cal))
        f.close()
    # 加载运动数据
    def load_sport(self):
        try:
            f = open('sport_records.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            return
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            sid, date, stype, dur, cal = line.split(',')
            # 重建对象（跳过自动计算，直接用保存的数值）
            record = SportRecord(sid, date, stype, dur)
            record.calorie = cal
            self.sport_list.append(record)
        f.close()
    # 系统帮助
    def show_help(self):
        print('\n===== 系统使用帮助 =====')
        print('1. 首次使用请先注册账号，学号为唯一标识')
        print('2. 健康数据可记录每日体重、睡眠、饮水、饮食热量')
        print('3. 运动打卡支持6种常见运动，自动计算消耗热量')
        print('4. 所有数据需手动保存，退出前请先执行保存操作')
        print('5. 统计分析可查看BMI、运动总量与目标完成情况')
        print('========================\n')