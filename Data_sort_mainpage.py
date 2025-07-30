import xml.etree.ElementTree as ET
import re
import os

text_file = "E:\Code\FYP\main_page.txt.txt"
with open(text_file, "w", encoding="utf-8") as file:
    pass  # clean file

taiwan_team_chinese_names = ['統一7-ELEVEn獅','中信兄弟','樂天桃猿','台鋼雄鷹','富邦悍將', '味全龍']


def Data_Sorting_mainpage():
        
    try:
        tree = ET.parse(f"E:\Code\FYP\scraped_data_2025_07_14\www_cpbl_com_tw_.xml")
    except ET.ParseError as e:
        try:
            tree = ET.parse(f"E:\Code\FYP\scraped_data_2025_07_14\www_cpbl_com_tw_.xml")
        except ET.ParseError as e:
            print(f"Error parsing www_cpbl_com_tw_.xml: {e}")
            return
        print(f"Error parsing www_cpbl_com_tw_.xml: {e}")
        # Skip files that cannot be parsed
        
    root = tree.getroot()



    content = root.find('content').text

    try:
        # basic information
        web_url = root.find('url').text
        print("web_url:", web_url)
    except Exception as e:
        print(f"An error occurred while processing: {e}")

    content_length = len(content.split('\n'))

    placing=[]
    team_name=[]
    no_of_cmp=[]
    w_l_d=[]
    w_prob=[]
    w_diff=[]
    sub_w_l=[]
    sh_placing=[]
    sh_team_name=[]
    sh_no_of_cmp=[]
    sh_w_l_d=[]
    sh_w_prob=[]
    sh_w_diff=[]
    sh_sub_w_l=[]
    
    
    def standing_search(content):
        lines = content.split('\n')
        current_row = []
        array = []
        for i in range(content_length):
            line = lines[i]
            if line == 'standing':
                standing_num = i
                # startloop 
            if line == 'pitching leaders':
                pitching_leaders_num = i
                break
        for i in range(standing_num, pitching_leaders_num-2):
            line = lines[i] 
            if re.fullmatch(r'^[0-9]', line) and lines[i+1] in taiwan_team_chinese_names:
                if current_row:
                    array.append(current_row)
                current_row = [line]
            else:
                current_row.append(line.strip())
        
        if current_row:
            array.append(current_row)

        return array


    standing_result = standing_search(content)
    for i in range(len(standing_result)):
        print(standing_result[i])
        def extract_leaders(section_name, end_marker):
            lines = content.split('\n')
            section_data = []
            capture = False
            current_entry = []

            for line in lines:
                if line.strip() == section_name:
                    capture = True
                    continue
                if line.strip() == end_marker:
                    if current_entry:
                        section_data.append(current_entry)
                    break
                if capture:
                    if re.match(r"^\d+\.", line):
                        if current_entry:
                            section_data.append(current_entry)
                        current_entry = [line.strip()]
                    else:
                        current_entry.append(line.strip())

            return section_data

        def print_leaderboard(title, data):
            print(f"\n--- {title} ---")
            for entry in data:
                print(" ".join(entry))

        # Extract and print pitching leaders
        pitching_categories = [
            ("防禦率", "勝投"),
            ("勝投", "救援成功"),
            ("救援成功", "中繼成功"),
            ("中繼成功", "奪三振"),
            ("奪三振", "打擊TOP5"),
        ]

        print("\n✅ 投手TOP5 Pitching Leaders")
        for start, end in pitching_categories:
            category_data = extract_leaders(start, end)
            print_leaderboard(start, category_data)

        # Extract and print batting leaders
        batting_categories = [
            ("打擊率", "安打"),
            ("安打", "全壘打"),
            ("全壘打", "打點"),
            ("打點", "盜壘"),
            ("盜壘", "達成紀錄"),
        ]

        print("\n✅ 打擊TOP5 Batting Leaders")
        for start, end in batting_categories:
            category_data = extract_leaders(start, end)
            print_leaderboard(start, category_data)







if __name__ == "__main__":
    try:
        Data_Sorting_mainpage()
    except Exception as e:
        print(f"An error occurred while processing main page: {e}")
