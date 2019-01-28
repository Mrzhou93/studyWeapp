# encoding=utf-8
"""
完成与数据库的一些简单交互
"""
import pymongo

ip_address = ''             # 服务器的IP地址
port = '27017'              # 端口号，MongoDB的默认监听端口为27017
user = ''                   # 用户名
pwd = ''                    # 密码
db = ''                     # 对应的数据库
coll = ''                   # 对应的数据集合


def upload_user(openId, avatarUrl):
    """
    向数据库中进行数据的
    :param openId: 用户的openid
    :param avatarUrl: 头像的地址
    :return: 数据库的操作结果
    """
    mongo = pymongo.MongoClient('mongodb://' + user + ':' + pwd + '@' + ip_address + ':' + port + '/' + db)

    mydb = mongo[db]
    collection = mydb[coll]

    try:
        flag = collection.find({'openId': openId}).count()  # 在数据库中查看是否存在含有openId所对应的文档
        if flag != 0:
            return 0  # 0代表数据已经存在
        else:
            collection.save({'openId': openId, 'avatarUrl': avatarUrl})
            return 1  # 1代表数据上传完毕
    except:
        return 2  # 出现错误


def getInfo():
    mongo = pymongo.MongoClient('mongodb://' + user + ':' + pwd + '@' + ip_address + ':' + port + '/' + db)

    mydb = mongo[db]
    collection = mydb[coll]
    try:
        userinfo = []
        for i in collection.find({}, {'_id': 0, 'openid': 0}):
            userinfo.append(i)
        return userinfo
    except:
        return 0