import json
def main():
    income_list = []
    issurance_list = []
    with open("./../data/income.txt") as income_file:
        income_list = [line.strip().replace("（","-").replace("(","-").replace("）","").replace(")","").replace("~","-").replace("～","-").replace(" ","") for line in income_file]
    
    with open("./../data/bj-format.json") as bj_file:
        bj_list = json.load(bj_file)
        for bj in bj_list:
            for name in bj["DRUGNAME"].split("\n"):
                name = name.replace("（","-").replace("(","-").replace("）","").replace(")","").replace("~","-").replace("～","-").replace(" ","")
                issurance_list.append(name)
                if bj.get("DRUGDOSAGE","") is None:
                    continue
                issurance_list.append(bj["DRUGNAME"]+bj.get("DRUGDOSAGE",""))
            if len(bj["DRUGNAME"].split("\\")) > 1:
                issurance_list.append(bj["DRUGNAME"].split("\\")[0])


    for income in income_list:
        exist = False
        max_seq = ""
        max = 0
        for issurance in issurance_list:
            if issurance in income:
                exist = True
                max_seq = income + "|" + issurance
                max =  len(issurance) if len(issurance) > max else max
        if not exist:
            print(income)
        else:
            print(max_seq)
    # print(len(issurance_list))      
if __name__ == '__main__':
    main()