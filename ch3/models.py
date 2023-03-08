from dataclasses import dataclass
from enum import Enum

class Rank(Enum):
    """
    쿠폰 등급
    """
    GOOD='good'
    BEST='best'

@dataclass
class Subscriber:
    """
    구독자
    """
    email:str
    rec_count:int

@dataclass
class Coupon:
    """
    쿠폰
    """
    code:str
    rank:Rank


@dataclass
class Message:
    """
    이메일
    """
    from_:str
    to_:str
    subject:str
    body:str