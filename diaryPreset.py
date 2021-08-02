import datetime

# Get Today's Date
today = datetime.date.today()

# Get Today's Day of week
weekdays = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
now = datetime.datetime.now()
wd = int(now.strftime("%w"))

# Check if file exist
try:
    testPresent = open(f"D:/Thong So Xue/Diary/{str(today)}.txt", "r")
    testPresent.close()
# Create File Name with Today's Date & write default preset
except:
    diaryPresent = open(f"D:/Thong So Xue/Diary/{str(today)}.txt", "w")
    diaryPresent.write(f"Diary {today}（{weekdays[wd]}）\n\n")
    diaryPresent.close()

# variables for yesterday
pastFilled = True
yesterday = datetime.date.today() - datetime.timedelta(days=1)

# Check if yesterday's diary is filled and exist
try:
    diaryPast = open(f"D:/Thong So Xue/Diary/{str(yesterday)}.txt", "r")
    if len(diaryPast.read()) <= 23:
        pastFilled = False
    diaryPast.close()
except:
    print(f"Diary File not Found. D:/Thong So Xue/Diary/{str(yesterday)}.txt is missing.")

# Write default text if yesterday's diary is not written
if not pastFilled:
    writePast = open(f"D:/Thong So Xue/Diary/{str(yesterday)}.txt", "a")
    writePast.write("今天世界很和平。\n【混日子+1】")
    writePast.close()
