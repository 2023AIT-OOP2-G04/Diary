from diaries.DiarySample import DiarySample
from diaries.IshikawaDiary import IshikawaSample
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           IshikawaSample(),
           ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()