from diaries.AbstractDiary import AbstractDiary

class OkuboDiary(AbstractDiary):
  def get_date(self):
   return "2023-12-14"
  def get_summary(self):
   return """グループワークが始まった。迷惑がかからないよう頑張る。"""
  def get_author(self):
    return "Okubo"