from models import Coupon,Subscriber, Rank,Message

def sub_coupon_rank(sub:Subscriber)->Rank:
    """
    구독자의 쿠폰 등급을 계산한다.
    """
    if sub.rec_count >=10:
        return Rank.BEST
    else:
        return Rank.GOOD
    
def select_coupons_by_rank(coupons:list[Coupon], rank:Rank)->list[Coupon]:
    """
    쿠폰 리스트에서 특정 등급의 쿠폰만 선택한다.
    """
    return [coupon for coupon in coupons if coupon.rank == rank]

def email_for_subscriber(sub:Subscriber,good_coupons:list[Coupon],best_coupons:list[Coupon])->Message:
    """
    구독자가 받을 이메일을 계산한다.
    """
    rank = sub_coupon_rank(sub)
    if rank == Rank.GOOD:
        return Message(
            from_="newsletter@coupondog.co",
            to_=sub.email,
            subject="Your Good weekly coupon inside",
            body=f"Here are your good coupons: {', '.join(c.code for c in good_coupons)}",
        )
    else:    # rank == Rank.BEST
        return Message(
            from_="newsletter@coupondog.co",
            to_=sub.email,
            subject="Your Best weekly coupon inside",
            body=f"Here are your best coupons: {', '.join(c.code for c in best_coupons)}",
        )
    
def emails_for_subscribers(subs:list[Subscriber],good_coupons:list[Coupon],best_coupons:list[Coupon])->list[Message]:
    """
    보낼 이메일 목록을 준비한다.
    """
    return [email_for_subscriber(sub,good_coupons,best_coupons) for sub in subs]

class EmailSystem:
    @staticmethod
    def send(email:Message):
        """
        이메일을 보낸다.
        """
        
        print(f"From: {email.from_}")
        print(f"To: {email.to_}...")
        print("-----"*10)
        print(f"Subject: {email.subject}")
        print(f"Body: {email.body}")
        print("\n\n")