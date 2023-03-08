
from models import Coupon,Subscriber,Rank

def fetch_coupons_from_db()->list[Coupon]:
    return [
        Coupon("MAYDISCOUNT",Rank.GOOD),
        Coupon("PROMOTION45",Rank.BEST),
        Coupon("GETADEAL",Rank.BEST),
        Coupon('ILIKEDISCOUNT',Rank.GOOD),
        ]

def fetch_subscribers_from_db(page:int)->list[Subscriber]:
    if page>=1:
        return []
    return [
        Subscriber("john@coldmail.com",2),
        Subscriber("sam@pmail.com",16),
        Subscriber("linda1989@oal.com",1),
        Subscriber("jan1940@ahoy.com",0),
        Subscriber("mrbig@pmail.co",25),
        Subscriber("lol@lol.lol",0),
    ]