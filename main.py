from diaries.DiarySample import DiarySample
from diaries.OkuboDiary import OkuboDiaryDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),OkuboDiaryDiary(), ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()