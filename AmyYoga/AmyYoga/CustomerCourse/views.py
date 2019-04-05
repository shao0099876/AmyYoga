from django.shortcuts import render
from Database.models import BuyCourse as buyCourseDB #购买课程记录
from Database.models import BuyedCourse as buyedCourseDB #已消费课程记录
from Tools import SessionManager,FormsManager

# Create your views here.

def get_data1(sql):#从数据库中获取数据
    conn = buyCourseDB.connect(conf.test_dbhost, conf.test_user, conf.test_passd, conf.test_dbname, port=8000,
                               charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()  # 搜取所有结果
    cur.close()
    conn.close()
    return results

def get_data2(sql):#从数据库中获取数据
    conn = buyedCourseDB.connect(conf.test_dbhost, conf.test_user, conf.test_passd, conf.test_dbname, port=8000,
                               charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()  # 搜取所有结果
    cur.close()
    conn.close()
    return results

def customercourse(request):  # 向页面输出订单
     sql1 = "SELECT coursename,number,money" \
              "FROM `buyCourseDB` GROUP BY username" \
              "WHERE username=SessionManager.getUsername(request)"
     m_data1 = get_data1(sql1)

     sql2 = "SELECT coursename,number,money" \
            "FROM `buyedCourseDB` GROUP BY username" \
            "WHERE username=SessionManager.getUsername(request)"
     m_data2 = get_data1(sql2)
     return render(request, 'customercourseUI.html', locals(), {'order1': m_data1},{'order2':m_data2})  # 渲染页面 按照课程名排序
