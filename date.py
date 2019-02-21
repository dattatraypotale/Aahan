from PyQt5.QtCore import QDate, QDateTime, Qt

now = QDate.currentDate()
print(now.toPyDate())
print(now)