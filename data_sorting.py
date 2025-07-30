import xml.etree.ElementTree as ET
import re
import os

import firebase_admin
from firebase_admin import credentials, db

# Set the path to your folder
folder_path = 'E:\Code\FYP\scraped_data_2025_07_14'  # Replace this with the actual path

# Compile a regex pattern to match filenames containing "person" (case-insensitive)
pattern = re.compile(r'person', re.IGNORECASE)

# List all files in the folder
files = os.listdir(folder_path)

# Filter files that match the regex pattern
matching_files = [f for f in files if pattern.search(f)]

text_file = "E:\Code\FYP\members_details.txt"
with open(text_file, "w", encoding="utf-8") as file:
    pass  # clean file

# Output the result
def Data_Sorting_player(filename):
    
    name = ''
    teamfiles = ''
    
    try:
        tree = ET.parse(f"E:\Code\FYP\scraped_data_2025_07_14\{filename}")
    except ET.ParseError as e:
        try:
            tree = ET.parse(f"E:\Code\FYP\scraped_data_2025_07_14{filename}")
        except ET.ParseError as e:
            print(f"Error parsing {filename}: {e}")
            return
        print(f"Error parsing {filename}: {e}")
        # Skip files that cannot be parsed
        
    root = tree.getroot()



    content = root.find('content').text




    try:
        # basic information
        web_url = root.find('url').text
        print("web_url:", web_url)
    except Exception as e:
        print(f"An error occurred while processing {f}: {e}")
        
    
    team = ''
    taiwan_team_eng_names = ['TSG Hawks', 'U-Lions', 'Guardians', 'Brothers', 'Monkeys', 'DRAGONS']
    lines = content.split('\n') 
    for i in range(0, len(lines)):
        line = lines[i]
        if line in taiwan_team_eng_names:
            team = line
            print("team", team)


    content_length = len(content.split('\n'))


    for i in range(0,content_length-1):
        #基本資料 basic information
        if(content.split('\n')[i] == '個人成績表' and name == ''):
            name = content.split('\n')[i-1]
            print("name", "\t",content.split('\n')[i-1])
            number = content.split('\n')[i+3]
            print("number", "\t",content.split('\n')[i+3])
        if(content.split('\n')[i] == '位置'):
            position = content.split('\n')[i+1]
            print("position", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '投打習慣'):
            batting_hand = content.split('\n')[i+1]
            print("batting_hand", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '身高/體重'):
            height = content.split('\n')[i+1]
            print("height", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '生日'):
            birthday = content.split('\n')[i+1]
            print("birthday", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '初出場'):
            first_game = content.split('\n')[i+1]
            print("first_game", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '學歷'):
            education = content.split('\n')[i+1]
            if(education == '國籍/出生地'):
                education = None
            print("education", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '國籍/出生地'):
            birthplace = content.split('\n')[i+1]
            print("birthplace", "\t", "\t",content.split('\n')[i+1])
        if(content.split('\n')[i] == '原名'):
            birthname = content.split('\n')[i+1]
            if(birthname == '選秀順位'):
                birthname = None
            print("birthname", "\t",birthname)
        if(content.split('\n')[i] == '選秀順位'):
            draft_position = content.split('\n')[i+1]
            print("draft_position", "\t", draft_position)


    for i in range(0,content_length-1):
        if(content.split('\n')[i] == '投球成績' or content.split('\n')[i] == '打擊成績'):
            pitch_record_N = i
        if(content.split('\n')[i] == '守備成績'):
            defensive_performance_N = i
        if(content.split('\n')[i] == '對戰成績'):
            batting_result_N = i

    years = []

    pitch_record = []
    current_row = []



    import re

    def filter_by_year(content, start, end):
        lines = content.split('\n')  # Avoid splitting every iteration
        current_row = []
        array = []
        for i in range(start + 1, end):
            line = lines[i]
            if re.search(r'\b20[0-9]{2}\b', line) or line == 'TOTAL':  # If line contains a year
                if current_row:  # If current row has data, store it
                    array.append(current_row)
                current_row = [line]  # Start a new row 
            else:
                current_row.append(line.strip())  # Add line to current row

        # Don't forget to add the last collected row
        if current_row:
            array.append(current_row)
        
        return array

    def filter_by_teams(content, start, end):
        lines = content.split('\n')  # Avoid splitting every iteration
        current_row = []
        array = []
        for i in range(start + 1, end):
            line = lines[i]
            if line == '球隊':
                start = i
            if line == 'TOP':
                end = i
        
        teams = ['樂天桃猿', '中信兄弟', '富邦悍將', '統一7-ELEVEn獅', '味全龍', '衛冕軍', '台鋼雄鷹']
        for i in range(start, end):
            line = lines[i]
            if line in teams:  
                array.append(current_row)
                current_row = [line]  # Start a new row 
                match line:
                    case '樂天桃猿':
                        teamfiles = 'Monkeys'
                    case '中信兄弟':
                        teamfiles = 'Brothers'
                    case '富邦悍將':
                        teamfiles = 'Guardians'   
                    case '統一7-ELEVEn獅':
                        teamfiles = 'U-Lions'
                    case '味全龍':
                        teamfiles = 'DRAGONS'
                    case '衛冕軍':
                        teamfiles = 'Protectors'
                    case '台鋼雄鷹':
                        teamfiles = 'TSG Hawks'
            else:
                current_row.append(line.strip())  # Add line to current row

        # Don't forget to add the last collected row
        if current_row:
            array.append(current_row)
            
        return array

    pitch_record = filter_by_year(content, pitch_record_N, defensive_performance_N)
    defensive_performance = filter_by_year(content, defensive_performance_N, batting_result_N)
    batting_result = filter_by_teams(content, batting_result_N, content_length)







    # print("pitch_record:")
    # for row in pitch_record:
    #     print(row)
        
    # print("defensive_performance:")
    # for row in defensive_performance:
    #     print(row)

    # print("batting_result:")
    # for row in batting_result:
    #     print(row)



    try:
        with open(text_file, "a", encoding="utf-8") as file:
            file.write(f"web_url: \n {web_url}\n")
            file.write(f"name: \n {name}\n")
            file.write(f"number: \n {number}\n")    
            file.write(f"team: \n {team}\n")
            file.write(f"position: \n {position}\n")
            file.write(f"batting_hand: \n {batting_hand}\n")
            file.write(f"height: \n {height}\n")
            file.write(f"birthday: \n {birthday}\n")
            file.write(f"first_game: \n {first_game}\n")
            file.write(f"education: \n {education}\n")
            file.write(f"birthplace: \n {birthplace}\n")
            file.write(f"birthname: \n {birthname}\n")
            file.write(f"draft_position: \n {draft_position}\n")

            for row in pitch_record:
                file.write("\t".join(map(str, row)) + "\n")
            for row in defensive_performance:
                file.write("\t".join(map(str, row)) + "\n")
            for row in batting_result:
                file.write("\t".join(map(str, row)) + "\n")

            file.write("\n"*5)


        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the exception as needed


if __name__ == "__main__":
    # Iterate through the matching files and process them
    total_amount = 0
    for f in matching_files:
        try:
            Data_Sorting_player(f)
            total_amount += 1
        except Exception as e:
            print(f"An error occurred while processing {f}: {e}")
            
            continue
    print(f"Total files processed: {total_amount}")
    
        # Load and parse the XML file
        
        


