import exinput


def analyze(db_name, table_name):
    global analyze_result
    db = exinput.mysql_link(db_name)
    cursor = db.cursor()
    total = cursor.execute("select * from " + table_name)
    chinese = cursor.execute("select * from "+table_name+" where chinese>=60")
    math = cursor.execute("select * from "+table_name+" where math>=60")
    english = cursor.execute("select * from "+table_name+" where english>=60")
    print(str(total)+" "+str(chinese)+" "+str(math)+" "+str(english))
    analyze_result = "总计有" + str(total) + "人, 其中语文及格人数为"+str(chinese)+"人, 数学及格人数为"+str(math)+"人, 英语及格人数为"+str(english)+"人!"
    cursor.close()  # 关闭连接
    db.close()
    return analyze_result
