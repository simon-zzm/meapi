开发目的：
    学习http api开发知识。简化api开发流程。

接口开发步骤(修改好配置文件): 
1)example.py为例子文件。拼接一个sql取出值，并整理成json返回。
2)在route.py文件中导入例子from example import *。
3)在route.py文件中写好路由(r"/test", exampleHandler)。
开发完成。启动服务,推荐命令如下。
python me.py ttt
后面的ttt是随便加，最好是项目名，方便后台运行时的进程查找。
浏览器浏览即可http://x.x.x.x:xx/test。

其它部分的详细记录

开发规范：
    变量、函数、文件名等命名使用驼峰命名法。
    python开发遵循 PEP-8代码风格。

已经实现功能:
1)数据库读写分离
2)数据库多库
3)redis认证存储session
4)账户密码加盐存在mysql中,加密加盐
5)mysql中查出的二维表转json
6)支持将多次查询（select）数据组成一个json

涉及到的技术和第三方库、软件
tornado
redis
mysql

文件说明:
config.py            整个项目配置
createPass.py        初期生成密码使用
route.py             路由文件
me.py                主文件，http入口
modules.py           全局使用模块
mysqlToJson.py       mysql数据库选出的数据转json
requirements.txt     使用第三方库名版本记录
example.py           例子文件 

基础功能说明:
登陆格式
http://x.x.x.x:xxx/v1/login?user=simonzhang&passwd=1
注销格式
http://x.x.x.x:xxx/v1/logout

返回错误部分说明：
服务端错误为1xx到5xx 详见：http://www.simonzhang.net/?p=2972
所以本系统错误返回错误用9xx
950    转换json失败
960    认证失败或接口错误
995    用户名或密码出现错误
997    服务端错误（写入redis错误）
998    注销成功
999    登陆成功

数据库中的测试数据(密码部分做了修改，可以使用createPass.py生成)
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `passwd` varchar(70) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

INSERT INTO `user` VALUES ('1', 'simonzhang', 'pbkdf2:sha1:1000$X.............');
INSERT INTO `user` VALUES ('2', 'tom', 'pbkdf2:sha1:1000$ZTwYUsHN$38...............');
INSERT INTO `user` VALUES ('3', 'Dave', 'pbkdf2:sha1:1000$dLoolU5Z$7.................');

CREATE TABLE `userInfo` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userId` int(10) NOT NULL,
  `age` int(2) NOT NULL,
  `class` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4;

-- ----------------------------
-- Records of userInfo
-- ----------------------------
INSERT INTO `userInfo` VALUES ('1', '1', '23', '3');
INSERT INTO `userInfo` VALUES ('2', '3', '16', '2');

个人博客 www.simonzhang.net
邮箱 simon-zzm@163.com
