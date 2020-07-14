import json
from fuzzywuzzy import fuzz #for natural language processing
import pandas as pd
question_list=[]
with open('C:/Users/Archit/Desktop/ArcInternship/Dataset/1.json',encoding='utf-8') as jsonfile:#here the json file should be dynamic(BACKEND AND AIML)
    data = json.load(jsonfile,)#json files data is stored in data

def getmcq(a,b,c,id1):
    global question_list
    list_of_dataframes=[]
    list_of_dataframes1=[]
    df = pd.read_csv("C:/Users/Archit/Desktop/ArcInternship/Dataset/"+"PYM"+".csv",encoding='latin1',error_bad_lines=False)
    df1=df[df['subcourse'].str.contains(b,na=False)]
    df2=df1[df1['difficulty'].str.contains(c,na=False)]
    df3=df2.sample(n =a, replace = True)
    list_of_dataframes.append(df3)#all the questions till the loop ends will be appended in the list_of_dataframes
    master_frame=pd.concat(list_of_dataframes,axis=0,ignore_index=True)#all skill questions are received and put in one master frame
    master_frame1=master_frame[['QID']]#master frame1 will fetch the qids of the questions given in master_frame
    for i in range(a):
        question_list1=master_frame1['QID'].values[i]
        #print(question_list1)
        question_list.append(question_list1)
    #list_of_dataframes1.append(master_frame1)#important
    #master_df=pd.concat(list_of_dataframes1,axis=0,ignore_index=True)#here all the dataframes are joined in a master_df#important
    #master_df.reset_index(inplace=True)#important
    #master_df.to_json(r'C:/Users/hp/Desktop/Internship/'+id1+'cmb.json')#the qids are stored in a locally made json path with the name of the json file given by the id(parameter)
        #^important(Backend and AIML Team)
#---------------------------------------------------------Technical Scenario----------------------------------------------------#
def getts(number,b,c,id1):
    global question_list
    list_of_dataframes=[]
    list_of_dataframes1=[]
    for i in range(number):
        df = pd.read_csv("C:/Users/Archit/Desktop/ArcInternship/Dataset/"+ "PYTS" +".csv",encoding='latin1',error_bad_lines=False)#file is retreived
        #We will get questions from here
        df1=df[df['subcourse'].str.contains(b,na=False)]
        df2=df1[df1['difficulty'].str.contains(c,na=False)]
        df3=df2.sample(n =number, replace = True)
        list_of_dataframes.append(df3)#all the questions till the loop ends will be appended in the list_of_dataframes
        master_frame=pd.concat(list_of_dataframes,axis=0,ignore_index=True)#all skill questions are received and put in one master frame
        master_frame1=master_frame[['QID']]#master frame1 will fetch the qids of the questions given in master_frame
    for i in range(number):
        question_list1=master_frame1['QID'].values[i]
        #print(question_list1)
        question_list.append(question_list1)
    json_object = json.dumps(question_list)
    with open(id1+"cca.json", "w") as outfile:
            print("success")
            outfile.write(json_object)
#id1=input("Enter the id")
id1=data['user_id']
#coursename=input("Enter the coursename")
get_course_code=data['courseid']
#difficulty=input("Enter the difficulty")
difficulty=data['difficulty']
#no_of_mcq=int(input("Enter the number of mcq's to be given"))
no_of_mcq=int(data["no_of_mcqquestions"])
#no_of_ts=int(input("Enter the number of technical scenarios"))
no_of_ts=int(data["no_of_tsquestions"])
qid={'mcq':'M','technical scenarios':'TS','modify code in the coding platform':'MC','coding tests':'CT'} #codes for qid for filename retreival
#skillcodes={'python':'PY','javascript':'JS','html':'HT','frontend':'UIFE'}
#for key in skillcodes:
 #   if(coursename==key):
  #      get_course_code=skillcodes.get(coursename)
   #     #print(get_file_part1)
get_course_code=data['courseid']
subcourse_code=get_course_code+'-'
getmcq(no_of_mcq,subcourse_code,difficulty,id1)
getts(no_of_ts,subcourse_code,difficulty,id1)
