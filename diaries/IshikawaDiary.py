from diaries.AbstractDiary import AbstractDiary
class IshikawaSample(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "グループに顔見知りが結構いた。"
    def get_author(self):
        return "Ishikawa"