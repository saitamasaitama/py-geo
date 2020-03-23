from django.test import TestCase
from typing import NamedTuple
import struct


def fill_bits(size:int):
    b=0
    for i in range(size):
        b=b<<1
        b=b|1
    return b


def take_bit(V:int,begin:int,size:int ):
    #まず64ビット分マスク
    MASK=0xFFFFFFFFFFFFFFFF
    V=V&MASK
    
    #beginから先をビットシフト
    #開始までずらす
    V=V>>begin
    #マスクを取得
    OPEN_MASK=fill_bits(size)
    return V&OPEN_MASK

def GeoTime(NamedTuple):
    minute:int
    second:int
    millisec:int

def GeoBit(NamedTuple):
    latitude:int
    lat_time:GeoTime
    longitude:int
    long_time:GeoTime

class GEO:
    @staticmethod
    def From(V:int)->GeoBit:
        return GeoBit(
                latitude=10,
                longitude=10,
                lat_time=GeoTime(
                    minute=1,
                    second=2,
                    millisec=3
                ),
                long_time=GeoTime(
                    minute=1,
                    second=2,
                    millisec=3
            )
        )

# Create your tests here.
print("OK")

print(f"{take_bit(0x1234FFFFFFFFFFFFFFFF,10,7 ):020x}")
print(f"{GEO.From(0x1234FFFFFFFFFFFFFFFF)}")


