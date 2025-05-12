from datetime import datetime

a = datetime.now()
date_format = '%d.%m.%Y %H:%M:%S'
print(datetime.strftime(a, date_format))