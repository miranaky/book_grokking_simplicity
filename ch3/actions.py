from db import fetch_coupons_from_db,fetch_subscribers_from_db
from calcs import emails_for_subscribers, select_coupons_by_rank,EmailSystem
from models import Rank


def send_issue():
    """
    이메일을 보내는 엑션
    """
    # 쿠폰 목록을 가져온다.
    coupons = fetch_coupons_from_db()
    # 쿠폰을 등급별로 분류한다.
    good_coupons = select_coupons_by_rank(coupons, Rank.GOOD)
    best_coupons = select_coupons_by_rank(coupons, Rank.BEST)
    
    # 구독자 목록이 너무 많을 경우 pagination 해서 가져온다.
    page=0
    subs = fetch_subscribers_from_db(page=page)
    while len(subs)>0:
        # 이메일 목록을 준비한다.
        emails = emails_for_subscribers(subs, good_coupons, best_coupons)
        # 이메일을 보낸다.
        for email in emails:
            EmailSystem.send(email)
        # 다음 페이지를 가져온다.
        page+=1
        subs = fetch_subscribers_from_db(page=page)

