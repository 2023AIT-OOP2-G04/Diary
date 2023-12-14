from diaries.AbstractDiary import AbstractDiary


class ShoDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"

    def get_summary(self):
        return "みんな初めまして。"

    def get_author(self):
        return "Sho"
