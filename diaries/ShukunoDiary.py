from diaries.AbstractDiary import AbstractDiary
class ShukunoDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return "朝早く起きたので眠かった"
    def get_author(self):
        return "Shukuno"