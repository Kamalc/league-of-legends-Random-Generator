from Search_Google import Search_Save
from Scraping import scarping_img_html
def preprocces_():

    with open("Top_List.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            mylist.append(stripped_line)
            # print(stripped_line)

    idx = 2
    sz = len(mylist)

    while idx < sz:
        final_list.append(mylist[idx].lower())
        print(mylist[idx].lower())
        #Search_Save('RiotX_ChampionList_'+mylist[idx].lower(), 'Ignore_Area/Images')
        idx += 8


final_list =[]
mylist = []
def main():
    scarping_img_html('https://na.leagueoflegends.com/en-us/champions/','jpg','Download')

    #preprocces_()

    pass

if __name__ == "__main__":
    main()
