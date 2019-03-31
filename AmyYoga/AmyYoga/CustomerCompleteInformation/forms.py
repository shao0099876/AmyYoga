from django import forms
from django.forms import fields
SexChoices=(
    (0,'女'),
    (1,'男')
) #性别下拉列表

AgeChoices=(
    (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),
    (11,'11'),(12,'12'),(13,'13'),(14,'14'),(15,'15'),(16,'16'),(17,'17'),(18,'18'),(19,'19'),(20,'20'),
    (21,'21'),(22,'22'),(23,'23'),(24,'24'),(25,'25'),(26,'26'),(27,'27'),(28,'28'),(29,'29'),(30,'30'),
    (31,'31'),(32,'32'),(33,'33'),(34,'34'),(35,'35'),(36,'36'),(37,'37'),(38,'38'),(39,'39'),(40,'40'),
    (41,'41'),(42,'42'),(43,'43'),(44,'44'),(45,'45'),(46,'46'),(47,'47'),(48,'48'),(49,'49'),(50,'50'),
    (51,'51'),(52,'52'),(53,'53'),(54,'54'),(55,'55'),(56,'56'),(57,'57'),(58,'58'),(59,'59'),(60,'60'),
    (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'),
    (71, '71'), (72, '72'), (73, '73'), (74, '74'), (75, '75'), (76, '76'), (77, '77'), (78, '78'), (79, '79'), (80, '80'),
    (81, '81'), (82, '82'), (83, '83'), (84, '84'), (85, '85'), (86, '86'), (87, '87'), (88, '88'), (89, '89'), (90, '90'),
    (91, '91'), (92, '92'), (93, '93'), (94, '94'), (95, '95'), (96, '96'), (97, '97'), (98, '98'), (99, '99'), (100, '100'),
    (101, '101'), (102, '102'), (103, '103'), (104, '104'), (105, '105'), (106, '106'), (107, '107'), (108, '108'), (109, '109'), (110, '110')
)#年龄下拉列表
class CompleteForm(forms.Form):  #完善个人信息时提交的表单
    name = forms.CharField(label='姓名', widget=forms.TextInput) #姓名
    sex = fields.ChoiceField(label='性别',choices=SexChoices,widget=forms.Select)  # 性别

    age = fields.ChoiceField(label='年龄',choices=AgeChoices,widget=forms.Select)  # 年龄

    birthday = forms.CharField(label='生日', widget=forms.TextInput)  # 生日
    phoneNumber = forms.IntegerField(label='联系方式', widget=forms.TextInput) #联系方式
    profession = forms.CharField(label='职业', widget=forms.TextInput)  # 职业
    height = forms.IntegerField(label='身高', widget=forms.TextInput)  #身高
    weight = forms.IntegerField(label='体重', widget=forms.TextInput) #体重
    bust = forms.IntegerField(label='胸围', widget=forms.TextInput) #胸围
    waistline = forms.IntegerField(label='腰围', widget=forms.TextInput) #腰围
    hipline = forms.IntegerField(label='臀围', widget=forms.TextInput) #臀围
    shoulderwidth = forms.IntegerField(label='肩宽', widget=forms.TextInput) #肩宽