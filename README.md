# 《you so beauty》

Created: May 17, 2023 12:29 AM

## How can achieve?

### 首先创建最重要的torch(CUDA)基础环境

1. anaconda 创建pytorch环境(python --version查询python版本)
    
    ```jsx
    conda create -n pytorch python=3.9.1
    ```
    
2. 切换为新建的环境
    
    ```jsx
    conda activate pytorch
    ```
    
3. pytorch配置本PC英伟达的cuda（具体参考以下博客）
    
    [win10 Anaconda 配置CUDA、CUDNN、pytorch详细安装教程_显卡与miniconda的关系_老秦子弟的博客-CSDN博客](https://blog.csdn.net/m0_52571323/article/details/110222966)
    
4. 在anaconda中继续执行以下命令，即安装torch(cuda)
    
    ```jsx
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
    ```
    
    等待10分钟左右的安装
    

### 安装各种相关的依赖包（pytorch环境下）

1. pyqt5、PyQt5-tools
    
    ![Untitled](%E3%80%8Ayou%20so%20beauty%E3%80%8B%20e1b3a27c9d8a41399f1de253b48902ed/Untitled.png)
    
    ```jsx
    (pip install PyQt5=5.9.2)
    pip install PyQt5-tools -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com
    ```
    
2. pymysql
    
    ```jsx
    pip install pymysql
    ```
    
3. matplotlib
    
    ```jsx
    pip install matplotlib
    ```
    
4. ****解决 ImportError: DLL load failed while importing win32api: 找不到指定的程序。****
    
    ```jsx
    pip install pypiwin32
    conda install pywin32
    ```
    
5. cv2
    
    ```jsx
    pip install opencv-python
    ```
    
6. mediapipe
    
    ```jsx
    pip install mediapipe 
    ```
    
7. ****dlib安装失败解决办法****
    
    ```jsx
    conda install -c conda-forge dlib
    ```
    
8. imutils
    
    ```jsx
    pip install imutils
    ```
    

### 连接数据库及建库建表

```jsx
create database facesorce_app;

use facesorce_app;

create table client_info
(
    acount    char(18) not null,
    password  char(12) not null,
    telephone char(11) null,
    email     char(20) null
);

create table mark_data
(
    id   int         not null,
    mark varchar(10) not null
);

create table images
(
    id   int auto_increment
        primary key,
    data mediumblob null
);

create table notice_data
(
    author varchar(20)  not null,
    notice varchar(100) not null
);

create table admin
(
    acount char(18) not null primary key,
    password char(12) not null
);

insert into client_info(acount, password, telephone, email) VALUES ('abc','123456','12345678910','10086@qq.com');
insert into admin(acount, password) values('admin','123456');
insert into mark_data(id, mark) values(1,'0');  //解释一下，这里的id=1是不变的，后面的mark作为一个标识记号
//根据发布信息的条数，当每次发布信息的时候，notice的条数都会+1（当连续发布时，只会），然后把这个notice的条数插入到mark字段中

```

修改~/Face/PyMysql.py和~/Face-server/server_PyMysql.py的配置

![Untitled](%E3%80%8Ayou%20so%20beauty%E3%80%8B%20e1b3a27c9d8a41399f1de253b48902ed/Untitled%201.png)

### 运行程序

~/Face/main.py

![Untitled](%E3%80%8Ayou%20so%20beauty%E3%80%8B%20e1b3a27c9d8a41399f1de253b48902ed/Untitled%202.png)

~/Face-server/UsoBeauty_Server.py

![Untitled](%E3%80%8Ayou%20so%20beauty%E3%80%8B%20e1b3a27c9d8a41399f1de253b48902ed/Untitled%203.png)

<aside>
💡 仅供学习使用，相关的图片、标识，如有侵权，请与作者联系。

</aside>