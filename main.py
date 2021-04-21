from Search_Google import Search_Save
from Scraping import scarping_img_html
import json

def preprocces_(txt):

    with open(txt, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            mylist.append(stripped_line)
            print(stripped_line)

    idx = 2
    sz = len(mylist)

    while idx < sz:
        final_list.append(mylist[idx].lower())
        print(mylist[idx].lower())
        #Search_Save('RiotX_ChampionList_'+mylist[idx].lower(), 'Ignore_Area/Images')
        idx += 8
    with open('JsonDB/data.json', 'w') as f:
        json.dump(final_list, f)

final_list =[]
mylist = []
def main():
    #scarping_img_html('https://na.leagueoflegends.com/en-us/champions/','jpg','Download')

    preprocces_("Roles_DB/top.txt")

    pass


if __name__ == "__main__":
    main()
