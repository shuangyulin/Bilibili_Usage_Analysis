#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    '''
    yonghuxingming=VARCHAR
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    touxiang=Text
    xingbie=VARCHAR
    shoujihaoma=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class usedata(BaseModel):
    __doc__ = u'''usedata'''
    __tablename__ = 'usedata'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户ID' )
    age=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    gender=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    durationofuse=models.FloatField   (  null=True, unique=False, verbose_name='使用时长(小时)' )
    usagefrequency=models.IntegerField  (  null=True, unique=False, verbose_name='使用频率(次/天)' )
    numberoflogins=models.IntegerField  (  null=True, unique=False, verbose_name='登录次数' )
    browsetype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='浏览内容类型' )
    contentpreference=models.CharField ( max_length=255, null=True, unique=False, verbose_name='内容类别偏好' )
    numberoflikes=models.IntegerField  (  null=True, unique=False, verbose_name='点赞数' )
    numberofcomments=models.IntegerField  (  null=True, unique=False, verbose_name='评论数' )
    numberofshares=models.IntegerField  (  null=True, unique=False, verbose_name='分享次数' )
    numberofvideos=models.IntegerField  (  null=True, unique=False, verbose_name='观看视频数量' )
    numberofarticles=models.IntegerField  (  null=True, unique=False, verbose_name='阅读文章数量' )
    devicetype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='设备类型' )
    systemversion=models.CharField ( max_length=255, null=True, unique=False, verbose_name='操作系统版本' )
    network=models.CharField ( max_length=255, null=True, unique=False, verbose_name='网络类型' )
    signalstrength=models.CharField ( max_length=255, null=True, unique=False, verbose_name='信号强度' )
    '''
    userid=VARCHAR
    age=Integer
    gender=VARCHAR
    durationofuse=Float
    usagefrequency=Integer
    numberoflogins=Integer
    browsetype=VARCHAR
    contentpreference=VARCHAR
    numberoflikes=Integer
    numberofcomments=Integer
    numberofshares=Integer
    numberofvideos=Integer
    numberofarticles=Integer
    devicetype=VARCHAR
    systemversion=VARCHAR
    network=VARCHAR
    signalstrength=VARCHAR
    '''
    class Meta:
        db_table = 'usedata'
        verbose_name = verbose_name_plural = '使用数据'
class usedataforecast(BaseModel):
    __doc__ = u'''usedataforecast'''
    __tablename__ = 'usedataforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    browsetype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='浏览内容类型' )
    numberoflogins=models.IntegerField  (  null=True, unique=False, verbose_name='登录次数' )
    numberoflikes=models.IntegerField  (  null=True, unique=False, verbose_name='点赞数' )
    numberofcomments=models.IntegerField  (  null=True, unique=False, verbose_name='评论数' )
    age=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    '''
    browsetype=VARCHAR
    numberoflogins=Integer
    numberoflikes=Integer
    numberofcomments=Integer
    age=Integer
    '''
    class Meta:
        db_table = 'usedataforecast'
        verbose_name = verbose_name_plural = '使用数据预测'
