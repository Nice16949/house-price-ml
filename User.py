# ========== 1. 用户实体类（对应用户管理模块） ==========
class User(object):
    def __init__(self, stu_id, password, name, gender, age, height):
        self.stu_id = stu_id        # 学号（唯一标识）
        self.password = password    # 登录密码
        self.name = name            # 姓名
        self.gender = gender        # 性别
        self.age = age              # 年龄
        self.height = height        # 身高（单位：m）

    def __str__(self):
        return f'学号:{self.stu_id}, 姓名:{self.name}, 性别:{self.gender}, 年龄:{self.age}, 身高:{self.height}m'


# ========== 2. 健康记录实体类（对应健康数据管理模块） ==========
class HealthRecord(object):
    def __init__(self, stu_id, date, weight, sleep_hour, water, calorie):
        self.stu_id = stu_id        # 所属用户学号
        self.date = date            # 记录日期
        self.weight = weight        # 体重（kg）
        self.sleep_hour = sleep_hour # 睡眠时长（小时）
        self.water = water          # 饮水量（ml）
        self.calorie = calorie      # 当日摄入热量（千卡）

    def __str__(self):
        return f'日期:{self.date}, 体重:{self.weight}kg, 睡眠:{self.sleep_hour}h, 饮水:{self.water}ml, 摄入热量:{self.calorie}千卡'


# ========== 3. 运动记录实体类（对应运动数据管理模块） ==========
class SportRecord(object):
    # 运动类型热量系数（千卡/小时），用于自动计算消耗
    SPORT_CAL = {
        "跑步": 450, "跳绳": 600, "篮球": 500,
        "羽毛球": 400, "健身": 350, "散步": 200
    }

    def __init__(self, stu_id, date, sport_type, duration):
        self.stu_id = stu_id
        self.date = date
        self.sport_type = sport_type    # 运动类型
        self.duration = duration        # 运动时长（分钟）
        # 自动计算消耗热量
        self.calorie = round(float(self.SPORT_CAL[sport_type]) * (float(duration) / 60), 1)

    def __str__(self):
        return f'日期:{self.date}, 运动:{self.sport_type}, 时长:{self.duration}分钟, 消耗热量:{self.calorie}千卡'