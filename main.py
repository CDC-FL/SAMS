import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import analyze
import pymysql
import exinput


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('SAMS')
        self.root.iconbitmap("image\\GenericBox.ico")
        self.root.geometry('800x600')
        tk.Label(root, text='学生成绩管理系统', font=("华文行楷", 60),
                 fg='#D8DC6A', bg="#6689A1").pack()
        main(self.root)


class main():
    def __init__(self, master):
        self.usr = tk.StringVar()
        self.pwd = tk.StringVar()
        self.master = master
        self.master.config(bg='#3A405A')
        # 基准界面main
        self.main = tk.Frame(self.master, bg='#3A405A')
        self.main.pack()
        usr_label = tk.Label(self.main, text='用户名：', bg='#3A405A',
                             fg='white', font=('', 30), height='3')
        usr_entry = tk.Entry(self.main, textvariable=self.usr)
        self.usr.get()
        pwd_label = tk.Label(self.main, text=' 密码：', bg='#3A405A',
                             fg='white', font=('', 30), height='3')
        pwd_entry = tk.Entry(self.main, show="*", textvariable=self.pwd)
        self.pwd.get()
        login_button = tk.Button(self.main, text='登录', command=self.login)
        exit_button = tk.Button(self.main, text='退出', command=self.exit)
        usr_label.grid(row=0, column=0)
        usr_entry.grid(row=0, column=1)

        pwd_label.grid(row=1, column=0)
        pwd_entry.grid(row=1, column=1)

        tk.Label(self.main, bg='#3A405A', height='2').grid(row=2)
        login_button.grid(row=3, column=0)
        exit_button.grid(row=3, column=1)
        tk.Label(self.main, bg='#3A405A', height='2').grid(row=4, columnspan=2)
        tk.Button(self.main, text="我还没有注册，点击注册",
                  command=self.register).grid(row=5, columnspan=2)

    def register(self):
        self.main.destroy()
        sign_up(self.master)

    def login(self):
        # 登录界面login
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='123456',
                               db='SAMS',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute("select * from login where usr='"
                    + self.usr.get() + "' and pwd='" + self.pwd.get() + "'")
        # print(self.usr.get())
        # print(self.pwd.get())
        if cur.fetchone() is not None:
            self.main.destroy()
            menu(self.master)
            cur.close()
            conn.close()
        else:
            messagebox.showerror(
                title='连接错误!', message='请检查用户名与密码是否输入正确')  # 错误提醒
            # self.main.destroy()
            # menu(self.master)

    def exit(self):
        self.master.destroy()


class menu():
    # 菜单界面menu
    def __init__(self, master):
        self.master = master
        self.master.config(bg='#AEC5EB')
        self.menu = tk.Frame(self.master, bg='#AEC5EB')
        self.menu.pack()
        input_button = tk.Button(
            self.menu, text='录入记录', font=("", 30), command=self.input)
        watch_button = tk.Button(
            self.menu, text='查看记录', font=("", 30), command=self.watch)
        alter_button = tk.Button(
            self.menu, text='修改记录', font=("", 30), command=self.alter)
        back_button = tk.Button(self.menu, text='使用其他用户登录', command=self.back)
        exit_button = tk.Button(self.menu, text='退出SAMS', command=self.exit)
        tk.Label(self.menu, bg='#AEC5EB', height='2').grid(row=0)
        input_button.grid(row=1, column=1)
        tk.Label(self.menu, bg='#AEC5EB', height='2').grid(row=2)
        watch_button.grid(row=3, column=1)
        tk.Label(self.menu, bg='#AEC5EB', height='2').grid(row=4)
        alter_button.grid(row=5, column=1)
        tk.Label(self.menu, bg='#AEC5EB', height='2').grid(row=6)
        back_button.grid(row=7, column=0)
        exit_button.grid(row=7, column=2)

    def watch(self):
        self.menu.destroy()
        watch(self.master)

    def alter(self):
        self.menu.destroy()
        alter(self.master)

    def back(self):
        self.menu.destroy()
        main(self.master)

    def exit(self):
        self.master.destroy()

    def input(self):
        self.menu.destroy()
        input(self.master)
        # print(ee.store_to('SAMS', 'stu', 'Template_File.xls'))
        # ee.store_to('SAMS', 'stu', 'Template_File.xls')
        # messagebox.showinfo(title='录入成功', message=ee.store_to('SAMS', 'stu', 'Template_File.xls'))


class input():
    # 录入界面
    def __init__(self, master):
        self.ID = tk.StringVar()
        self.name = tk.StringVar()
        self.classnum = tk.StringVar()
        self.gender = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.master = master
        self.master.config(bg='#2CDA9D')
        self.input = tk.Frame(self.master, bg='#2CDA9D')
        self.input.pack()
        self.Button_ = tk.Frame(self.master, bg='#2CDA9D')
        self.Button_.pack()
        tk.Label(self.input, bg='#2CDA9D', height='2').grid(row=0)

        tk.Label(self.input, text='学号:', bg='#2CDA9D').grid(row=1, column=0)
        tk.Entry(self.input, textvariable=self.ID).grid(row=1, column=1)
        self.ID.get()

        tk.Label(self.input, text='姓名:', bg='#2CDA9D').grid(row=2, column=0)
        tk.Entry(self.input, textvariable=self.name).grid(row=2, column=1)
        self.name.get()

        tk.Label(self.input, text='班级:', bg='#2CDA9D').grid(row=3, column=0)
        tk.Entry(self.input, textvariable=self.classnum).grid(row=3, column=1)
        self.classnum.get()

        tk.Label(self.input, text='性别:', bg='#2CDA9D').grid(row=4, column=0)
        tk.Entry(self.input, textvariable=self.gender).grid(row=4, column=1)
        self.gender.get()

        tk.Label(self.input, text='语文成绩:', bg='#2CDA9D').grid(row=5, column=0)
        tk.Entry(self.input, textvariable=self.chinese).grid(row=5, column=1)
        self.chinese.get()

        tk.Label(self.input, text='数学成绩:', bg='#2CDA9D').grid(row=6, column=0)
        tk.Entry(self.input, textvariable=self.math).grid(row=6, column=1)
        self.math.get()

        tk.Label(self.input, text='英语成绩:', bg='#2CDA9D').grid(row=7, column=0)
        tk.Entry(self.input, textvariable=self.english).grid(row=7, column=1)
        self.english.get()

        tk.Label(self.input, bg='#2CDA9D', height='2').grid(row=8)

        tk.Button(self.input, text='录入', command=self.input_data).grid(
            row=9, columnspan=2)
        tk.Label(self.input, bg='#2CDA9D', height='1').grid(row=10)
        tk.Button(self.input, text='返回主菜单',
                  command=self.back).grid(row=11, columnspan=2)
        tk.Label(self.input, bg='#2CDA9D', height='1').grid(row=12)
        tk.Button(self.input, text='excel导入',
                  command=self.excel_input).grid(row=13, columnspan=2)
        tk.Label(self.input, bg='#2CDA9D', height='1').grid(row=14)
        tk.Button(self.input, text='查看分析',
                  command=self.watch_analyze).grid(row=15, columnspan=2)

    def watch_analyze(self):
        messagebox.showinfo(
            title='分析结果', message=analyze.analyze('SAMS', 'stu'))

    def excel_input(self):
        messagebox.showinfo(title='录入成功', message=exinput.store_to(
            'SAMS', 'stu', 'Template_File.xls'))

    def back(self):
        self.input.destroy()
        menu(self.master)

    def input_data(self):
        list = []
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='SAMS', port=3306)
        # 创建游标对象
        cur = con.cursor()
        # 编写插入数据的sql
        sql = 'INSERT INTO stu(id,name,classnum,gender,chinese,math,english)VALUES(%s,%s,%s,%s,%s,%s,%s)'
        value = (
            self.ID.get(), self.name.get(), self.classnum.get(
            ), self.gender.get(), self.chinese.get(), self.math.get(),
            self.english.get())
        list.append(value)
        if list == [('', '', '', '', '', '', '')]:
            messagebox.showerror(title='错误!', message='请检查是否录入记录！')
        else:
            cur.executemany(sql, list)
            con.commit()
            cur.close()
            con.close()
            self.input.destroy()
            input(self.master)


class alter():
    def __init__(self, master):
        self.ID = tk.StringVar()
        self.name = tk.StringVar()
        self.classnum = tk.StringVar()
        self.gender = tk.StringVar()
        self.chinese = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.master = master
        self.master.config(bg='#2CDA9D')
        self.input = tk.Frame(self.master, bg='#2CDA9D')
        self.input.pack()
        self.Button_ = tk.Frame(self.master, bg='#2CDA9D')
        self.Button_.pack()
        tk.Label(self.input, bg='#2CDA9D', height='2').grid(row=0)

        tk.Label(self.input, text='学号:', bg='#2CDA9D').grid(row=1, column=0)
        tk.Entry(self.input, textvariable=self.ID).grid(row=1, column=1)
        self.ID.get()

        tk.Label(self.input, text='姓名:', bg='#2CDA9D').grid(row=2, column=0)
        tk.Entry(self.input, textvariable=self.name).grid(row=2, column=1)
        self.name.get()

        tk.Label(self.input, text='班级:', bg='#2CDA9D').grid(row=3, column=0)
        tk.Entry(self.input, textvariable=self.classnum).grid(row=3, column=1)
        self.classnum.get()

        tk.Label(self.input, text='性别:', bg='#2CDA9D').grid(row=4, column=0)
        tk.Entry(self.input, textvariable=self.gender).grid(row=4, column=1)
        self.gender.get()

        tk.Label(self.input, text='语文成绩:', bg='#2CDA9D').grid(row=5, column=0)
        tk.Entry(self.input, textvariable=self.chinese).grid(row=5, column=1)
        self.chinese.get()

        tk.Label(self.input, text='数学成绩:', bg='#2CDA9D').grid(row=6, column=0)
        tk.Entry(self.input, textvariable=self.math).grid(row=6, column=1)
        self.math.get()

        tk.Label(self.input, text='英语成绩:', bg='#2CDA9D').grid(row=7, column=0)
        tk.Entry(self.input, textvariable=self.english).grid(row=7, column=1)
        self.english.get()

        tk.Label(self.input, bg='#2CDA9D', height='2').grid(row=8)

        tk.Button(self.input, text='修改', command=self.alter_data).grid(
            row=9, column=0)
        tk.Button(self.input, text='返回主菜单',
                  command=self.back).grid(row=9, column=1)

    def alter_data(self):
        list = []
        con = pymysql.connect(host='localhost', user='root',
                              password='123456', database='SAMS', port=3306)
        # 创建游标对象
        cur = con.cursor()
        # 编写插入数据的sql
        # sql = 'INSERT INTO stu(id,name,classnum,gender,chinese,math,english)VALUES(%s,%s,%s,%s,%s,%s,%s)'
        sql = "update stu set id=%s,name=%s,classnum=%s,gender=%s,chinese=%s,math=%s,english=%s where id=%s"
        value = (
            self.ID.get(), self.name.get(), self.classnum.get(
            ), self.gender.get(), self.chinese.get(), self.math.get(),
            self.english.get(), self.ID.get())
        list.append(value)
        if self.name.get() == '0' and self.classnum.get() == '0' and self.gender.get() == '0' and self.chinese.get() == '0' and self.math.get() == '0' and self.english.get() == '0':
            cur.execute("delete from stu where id='"+self.ID.get()+"'")
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo(title='删除成功!', message='已删除记录！')
            self.input.destroy()
            alter(self.master)

        elif list == [('', '', '', '', '', '', '', '')]:
            messagebox.showerror(title='错误!', message='请检查是否录入记录！')
        else:
            cur.executemany(sql, list)
            con.commit()
            cur.close()
            con.close()
            self.input.destroy()
            alter(self.master)

    def back(self):
        self.input.destroy()
        menu(self.master)


class watch():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='#CFD4C5')
        self.watch = tk.Frame(self.master, bg='#CFD4C5')
        self.watch.pack()
        tk.Label(self.watch, bg='#CFD4C5', height='2').grid(row=0)
        # 表格数据
        tree = ttk.Treeview(self.watch, height=15)
        tree.grid(row=1)
        tk.Label(self.watch, bg='#CFD4C5', height='2').grid(row=2)
        tk.Button(self.watch, text='返回主菜单', command=self.back).grid(row=3)
        # 定义列(_注意如下的信息顺序一定要对齐_)
        tree["columns"] = ("学号", "姓名", "班级", "性别", "语文成绩", "数学成绩", "英语成绩")
        # 设置列
        tree.column("学号", width=70)
        tree.column("姓名", width=70)
        tree.column("班级", width=70)
        tree.column("性别", width=70)
        tree.column("语文成绩", width=70)
        tree.column("数学成绩", width=70)
        tree.column("英语成绩", width=70)
        # 设置表头
        tree.heading("学号", text="学号")
        tree.heading("姓名", text="姓名")
        tree.heading("班级", text="班级")
        tree.heading("性别", text="性别")
        tree.heading("语文成绩", text="语文成绩")
        tree.heading("数学成绩", text="数学成绩")
        tree.heading("英语成绩", text="英语成绩")

        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='123456',
                               db='SAMS',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        row_count = cur.execute("select * from stu")
        for line in cur.fetchall():
            tree.insert("", 0, text=line['id'], values=(
                line['id'], line['name'], line['classnum'], line['gender'], line['chinese'], line['math'],
                line['english']))
            # print(line)

    def back(self):
        self.watch.destroy()
        menu(self.master)


class sign_up():
    def __init__(self, master):
        self.name = tk.StringVar()
        self.password = tk.StringVar()
        self.re_password = tk.StringVar()
        self.master = master
        self.master.config(bg='#845A6D')
        self.sign_up = tk.Frame(self.master, bg='#845A6D')
        self.sign_up.pack()

        tk.Label(self.sign_up, text='请输入用户名：', bg='#845A6D', fg='white',
                 font=('', 20), height='3').grid(row=0, column=0)
        tk.Entry(self.sign_up, textvariable=self.name).grid(row=0, column=1)
        self.name.get()

        tk.Label(self.sign_up, text='请输入密码：', bg='#845A6D', fg='white',
                 font=('', 20), height='3').grid(row=1, column=0)
        tk.Entry(self.sign_up, textvariable=self.password, show='*').grid(
            row=1, column=1)
        self.password.get()

        tk.Label(self.sign_up, text='请再输入一遍密码：', bg='#845A6D',
                 fg='white', font=('', 20), height='3').grid(row=2, column=0)
        tk.Entry(self.sign_up, textvariable=self.re_password, show='*').grid(
            row=2, column=1)
        self.re_password.get()
        tk.Label(self.sign_up, bg='#845A6D',
                 height='2').grid(row=3, columnspan=2)
        tk.Button(self.sign_up, text='我已确认信息，执行注册',
                  command=self.register).grid(row=4, columnspan=2)
        tk.Label(self.sign_up, bg='#845A6D',
                 height='2').grid(row=5, columnspan=2)
        tk.Button(self.sign_up, text='返回登录界面',
                  command=self.back).grid(row=6, columnspan=2)

    def back(self):
        self.sign_up.destroy()
        main(self.master)

    def register(self):
        if self.password.get() != self.re_password.get():
            messagebox.showerror(
                title='注册失败!', message='请检查您两次输入的密码是否一致！')  # 错误提醒
        else:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                   db='SAMS', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            row_count = cursor.execute(
                "select * from login where usr ='"+self.name.get()+"'")
            #print(row_count)
            if row_count == 0:
                cursor.execute("insert into login(usr,pwd) values ('"
                               + self.name.get()+"','"+self.password.get()+"')")
                conn.commit()
                messagebox.showinfo(title='注册成功！', message='您已成为SAMS用户，祝您使用愉快')
                self.sign_up.destroy()
                menu(self.master)
            else:
                messagebox.showerror(
                    title='注册失败!', message='请更换当前用户名，该用户名已经存在！')  # 错误提醒


if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
