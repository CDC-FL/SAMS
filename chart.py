import matplotlib.pyplot as plt
import pymysql

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 连接数据库
db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='SAMS')

# 开启一个游标cursor
cursor = db.cursor()

# 获取phone数据表里的所有数据
sql = 'select * from stu'

# 执行sql中的语句
cursor.execute(sql)

# 将获取到的sql数据全部显示出来
result = cursor.fetchall()

# 定义需要用上的空数据数组，然后通过遍历数据库的数据将数据附上去
name = []
chinese = []
math = []
english = []
# 遍历表里的数据
for x in result:
    name.append(x[1])
    chinese.append(int(x[4]))
    math.append(int(x[5]))
    english.append(int(x[6]))

# 创建一个figure（一个窗口）来显示条形图
plt.figure()
plt.bar(name, chinese)
plt.xlabel('姓名')
plt.ylabel('语文成绩')
for x, y in enumerate(chinese):
    plt.text(x, y, '%s' % y)

plt.figure()
plt.bar(name, math)
plt.xlabel('姓名')
plt.ylabel('数学成绩')
for x, y in enumerate(math):
    plt.text(x, y, '%s' % y)

plt.figure()
plt.bar(name, english)
plt.xlabel('姓名')
plt.ylabel('英语成绩')
for x, y in enumerate(english):
    plt.text(x, y, '%s' % y)

# 创建一个figure（一个窗口）来显示折线图
plt.figure()
plt.plot(name, chinese)
plt.xlabel('姓名')
plt.ylabel('语文成绩')
for x, y in enumerate(chinese):
    plt.text(x, y, '%s' % y)

plt.figure()
plt.plot(name, math)
plt.xlabel('姓名')
plt.ylabel('数学成绩')
for x, y in enumerate(math):
    plt.text(x, y, '%s' % y)

plt.figure()
plt.plot(name, english)
plt.xlabel('姓名')
plt.ylabel('英语成绩')
for x, y in enumerate(english):
    plt.text(x, y, '%s' % y)

# 显示图表
plt.show()

# 关闭游标和数据库
cursor.close()
db.close()
