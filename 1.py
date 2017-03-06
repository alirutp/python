import mysql.connector
import os
import codecs
#设置数据库用户名和密码
user='root';#用户名
pwd='111111';#密码
host='localhost';#ip地址
db='wpad';#所要操作数据库名字
charset='UTF-8'
cnx = mysql.connector.connect(user=user,password=pwd, host=host, database=db)
#设置游标
cursor = cnx.cursor(dictionary=True)
#插入数据
#print(insert('gelixi_help_type',{'type_name':'\'sddfdsfs\'','type_sort':'283'}))
def insert(table_name,insert_dict):
  param='';
  value='';
  if(isinstance(insert_dict,dict)):
    for key in insert_dict.keys():
      param=param+key+","
      value=value+insert_dict[key]+','
    param=param[:-1]
    value=value[:-1]
  sql="insert into %s (%s) values(%s)"%(table_name,param,value)
  cursor.execute(sql)
  id=cursor.lastrowid
  cnx.commit()
  return id