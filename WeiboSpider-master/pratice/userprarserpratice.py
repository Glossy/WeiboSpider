from db.models import User
from logger.log import storage
from page_get.basic import get_page
from page_parse.basic import is_404
from db.user import save_user, get_user_by_uid
from db.seed_ids import set_seed_crawled
from page_parse.user import enterprise, person, public

page = get_page("http://weibo.com/163music?refer_flag=1005055013_&is_all=1",False,False)
print(page)
