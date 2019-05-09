# URL配置文档
## 首页 Index.urls
1. 首页

    srcserver.xyz/

    对应视图函数：Index.index

2. 登录后首页

    srcserver.xyz/logined/

    对应视图函数：Index.loginedIndex

## 关于页面 About.urls

1. 瑜伽简介

    srcserver.xyz/about/yoga/

    对应视图函数：About.yoga

2. 教师团队介绍

    srcserver.xyz/about/teacherteam/
    
    对应视图函数：About.teacherteam

3. 上课环境介绍

    srcserver.xyz/about/location/

    对应视图函数：About.location

4. 课程介绍

    srcserver.xyz/about/course/

    对应视图函数：About.course

## 登录&注销功能 UserLogin.urls

1. 用户登录

    srcserver.xyz/login/

    对应视图函数：UserLogin.login

2. 用户登出

    srcserver.xyz/login/logout

    对应视图函数：UserLogin.logout

## 注册功能 CustomerRegister.urls

1. 客户注册

    srcserver.xyz/register/

    对应视图函数：CustomerRegister.register

## 个人信息功能 PersonalInformation.urls

## 密码管理功能 ChangePassword.urls

1. 忘记密码

    srcserver.xyz/password/forget/

    对应视图函数：ChangePassword.forgetPassword

2. 忘记密码时用户名登录

    srcserver.xyz/password/forget/login/

    对应视图函数：ChangePassword.forgetPasswordLogin

3. 修改密码

    srcserver.xyz/password/change/

    对应视图函数：ChangePassword.changePassword

## 课程管理功能 Course.urls

## 订单功能 Purchase.urls

## 上课记录功能 CourseUsed.urls
