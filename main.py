from diaries.DiarySample import DiarySample
from diaries.OkuboDiary import OkuboDiary
from diaries.IshikawaDiary import IshikawaSample
from diaries.x22037Diary import x22037Diary
from diaries.ShukunoDiary import ShukunoDiary
from diaries.MoriDiary import MoriDiary
from diaries.ShoDiary import ShoDiary
from diaries.AyanoDiary import AyanoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    IshikawaSample(),
    x22037Diary(),
    ShukunoDiary(),
    MoriDiary(),
    OkuboDiary(),
    ShoDiary(),
    AyanoDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
