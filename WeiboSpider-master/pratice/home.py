import time

ajax_url = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain={}&pagebar={}&is_ori=1&id={}{}&page={}' \
           '&pre_page={}&__rnd={}'
print(ajax_url)

cur_time = int(time.time()*1000)
domain = 100505
uid = 2837176797
cur_page = 1
ajax_url_0 = ajax_url.format(domain, 0, domain, uid, cur_page, cur_page, cur_time)

print(ajax_url_0)