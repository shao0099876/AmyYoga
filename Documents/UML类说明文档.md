# UML类说明文档
## Customer类
Customer类是数据库表 
### 父类
- models.Model

    声明为一个模型类，以转换为数据库表

- Interface.CustomerInterface

    Customer类的接口

### 属性
- authoritySignal

    BooleanField字段，True表示管理员，False表示客户，默认值为客户

- username

    CharField字段，Customer表主键，最大长度20，含义为用户名

- password

    CharField字段，最大长度20，含义为密码

- personalInformation

    PersonalInformation的一个对象，属私有成员，含义为用户个人信息

    
### 方法
- checkAuthority(self,password)

    身份验证函数，参数self为调用的Customer对象，password为传入待验证的密码。作用是比较传入password与Customer对象自己的password的关系。返回值True含义是两个password相同，False是不相同

- isAdministrator(self)

    用户权限等级获取函数，参数self为调用的Customer对象。作用是返回该用户的权限等级。返回值True含义是用户为管理员权限，False是普通客户权限
- PersonalInformationInterface的抽象方法
    对PersonalInformationInterface的访问只能通过Customer进行，因此需要在Customer类中实现这些方法。方法作用为作为中间人访问PersonalInformation传递参数和返回值。
    具体内容可参见PersonalInformation类方法部分

## PersonalInformation类
### 父类
- Interface.PersonalInformationInterface
    PersonalInformation类的接口
### 属性
- phonenumber
    电话号码
- name
    姓名
- age
    年龄
- birthday
    生日
- profession
    职业
- sex
    性别
- height
    身高
- weight
    体重
- bust
    胸围
- waistline
    腰围
- hipline
    臀围
- shoulderwidth
    肩宽
### 方法
- set+属性名(self,p)

    此类方法作用是设置属性的值为参数p，无返回值。
    
- get+属性名(self)

    此类方法作用是获取属性的值并作为返回值。