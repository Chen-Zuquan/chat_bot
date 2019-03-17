import re
from datetime import datetime

def checkValidTime(time):
    # 日期格式话模版
    format_pattern = "%Y-%m-%d"
    end_date = datetime.now()
    end_date = end_date.strftime(format_pattern)
    diff = datetime.strptime(end_date, format_pattern) - datetime.strptime(time, format_pattern)
    if diff.days > 0:
        return True
    else:
        return False

def getTime(message):
    pattern = re.compile(r'\b\d{4}-\d{1,2}-\d{1,2}\b')
    results = pattern.findall(message)
    if results:
        #print(results[0])
        if checkValidTime(results[0]):
            return results[0]
        else:
            return ""
    else:
        return ""

#getTime("i am 2188-2-42 what iii, 20818-2-42")
