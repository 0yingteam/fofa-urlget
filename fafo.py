# -*- coding: utf-8 -*-
#coding by wyc
import fofa

if __name__ == "__main__":
    print '''   
__  _  ______________|__|
\ \/ \/ /  ___|_  __ \  |
 \     /\___ \ |  | \/  |
  \/\_//____  >|__|  |__|
            \/         
            '''

    email, key = ('邮箱',"密钥")
    client = fofa.Client(email, key)
    query_str = raw_input("请输入查询语法：")

    f_ip_port = open("ip.txt","w")
    f_host=open("host.txt","w")
    frist_page = input("请输入开始页面：")
    last_page = input("请输入结束页面：")

    for page in range(frist_page,last_page):                                          #从第1页查到第50页
        data = client.get_data(query_str,page=page,fields="ip,host,port")  #查询第page页数据的ip和城市
        for ip,host,port in data["results"]:
            f_ip_port.write(ip+":"+port+"\n")
            f_host.write(host+"\n")

    f_host.close()
    f_ip_port.close()

print "game over"