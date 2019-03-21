# UML接口说明文档
## PersonalInformation Interface
- setPhoneNumber(p)
    
    设置客户电话号码为p
- getPhoneNumber()

    获取用户电话号码，有返回值
- setName(p)

    设置用户姓名为p
- getName()

    获取用户姓名
- setAge(p)

    设置用户年龄为p
- getAge()

    获取用户年龄
- setBirthday(p)

    设置用户生日为p
- getBirthday()

    获取用户生日
- setProfession(p)

    设置用户职业为p
- getProfession()
    
    获取用户职业
- setSex(p)

    设置用户性别为p
- getSex()

    获取用户性别
- setHeight(p)

    设置用户身高为p
- getHeight()

    获取用户身高
- setWeight(p)

    设置用户体重为p
- getWeight()

    获取用户体重
- setBust(p)

    设置用户胸围为p
- getBust()

    获取用户胸围
- setWaistline(p)

    设置用户腰围为p
- getWaistline()

    获取用户腰围
- setHipline(p)

    设置用户臀围
- getHipline()

    获取用户臀围
- setShoulderwidth(p)

    设置用户肩宽
- getShoulderwidth()

    获取用户肩宽
## Customer Interface
- isAdministrator()
    
    获取用户身份，返回True为管理员，返回False为客户
- checkAuthority(password)

    身份验证函数，将未验证的密码作为参数输入，返回True为身份验证成功，False为身份验证失败
    