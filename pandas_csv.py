import csv
with open("test.csv", "r+", newline="", encoding="utf-8") as csvfile:
    textar = ["كيفية" ,"التعامل" ,"مع" "الكتابة","بالعربي"]
    textartow = ["كيفية التعامل مع الكتابة بالعربي"]
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    csvwriter = csv.writer(csvfile, delimiter='\n', quotechar=',')
    textar.reverse()
    textartow.reverse()
    csvwriter.writerow([textar]*5)
    csvwriter.writerow(["________________"])
    csvwriter.writerow([textartow]*5)


