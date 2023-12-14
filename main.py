from diaries.DiarySample import DiarySample
from diaries.IshikawaDiary import IshikawaSample
from diaries.x22037Diary import x22037Diary
from diaries.ShukunoDiary import ShukunoDiary
from diaries.MoriDiary import MoriDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    IshikawaSample(),
    x22037Diary(),
    ShukunoDiary(),
    MoriDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
