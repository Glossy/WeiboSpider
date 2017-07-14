from wblogin.login import *
"""q = {'see' : 1}
r = requests.get("https://www.baidu.com",params = q )
print(r.url)"""

su = get_encodename('542937552@qq.com')
session = requests.Session()
pre_url = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su="
pre_url = pre_url + su + "&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_="
prelogin_url = pre_url + str(int(time.time() * 1000))
# print(prelogin_url)
pre_data_res = session.get(prelogin_url, headers=headers)
server_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))

rs, yundama_obj, cid, session = login_no_pincode('542937552@qq.com', '1234567a', session, server_data)

#print(cid)
# print(rs)

rs_cont = session.get(rs, headers=headers)
login_info = rs_cont.text
#print(login_info)

u_pattern = r'"uniqueid":"(.*)",'
m = re.search(u_pattern, login_info)

# print(login_info)
# print(m)
# print(m.group())
#print(m.group())

home_url = "http://weibo.com/u/" + m.group(1) + "/home?wvr=5&lf=reg"
con = session.get(home_url,headers = headers)
#print(con.text)
if m and m.group(1):
    # 访问微博官方账号看是否正常
    check_url = "http://weibo.com/p/1006062671109275/home?from=page_100606&mod=TAB#place"
 #   'http://weibo.com/2671109275/about'

    resp = session.get(check_url, headers=headers)
    print(resp.text)



# print(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))
# sever_data = eval(pre_data_res.content.decode("utf-8").replace("sinaSSOController.preloginCallBack", ''))
#
# print(pre_data_res)
# print(sever_data)
#
# s = get_pincode_url(sever_data['pcid'])
# print(s)