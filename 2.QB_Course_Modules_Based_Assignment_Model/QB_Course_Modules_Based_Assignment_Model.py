from fuzzywuzzy import fuzz #for natural language processing
import pandas as pd#important

with open('C:/Users/Archit/Desktop/ArcInternship/Dataset/ModuleInput.json',encoding='utf-8') as jsonfile:#here the json file should be dynamic(BACKEND AND AIML)
    data = json.load(jsonfile,)


def getmcq(a,b,c,id1):
    list_of_dataframes=[]
    list_of_dataframes1=[]
    df = pd.read_csv("C:/Users/Archit/Desktop/ArcInternship/Dataset/"+ "PYM" +".csv",encoding='latin1',error_bad_lines=False)
    df1=df[df['difficulty'].str.contains(difficulty,na=False)]
    df2=df1[df1['subcourse'].str.contains(b,na=False)]
    df3=df2.sample(n =a, replace = True)
    list_of_dataframes.append(df3)#all the questions till the loop ends will be appended in the list_of_dataframes
    master_frame=pd.concat(list_of_dataframes,axis=0,ignore_index=True)#all skill questions are received and put in one master frame
    master_frame1=master_frame[['QID']]#master frame1 will fetch the qids of the questions given in master_frame
    list_of_dataframes1.append(master_frame1)#important
    master_df=pd.concat(list_of_dataframes1,axis=0,ignore_index=True)#here all the dataframes are joined in a master_df#important
    master_df.reset_index(inplace=True)#important
    master_df.to_json(r'C:/Users/Archit/Desktop/ArcInternship/Dataset/'+id1+'cmb.json')#the qids are stored in a locally made json path with the name of the json file given by the id(parameter)
        #^important(Backend and AIML Team)

#---------------------------------------------------------Technical Scenario----------------------------------------------------#
id1=data['user_id']
coursename=data['course_name']
subsection=data['subsection']
difficulty=data['difficulty']
no_of_mcq=data['no_of_mcq']
skillcodes={'python':'PY','javascript':'JS','html':'HT','frontend':'UIFE'}
for key in skillcodes:
    if(coursename==key):
        get_course_code=skillcodes.get(coursename)
        #print(get_file_part1)


subsection=str(subsection)
subcourse_code=get_course_code+'-'+subsection
getmcq(no_of_mcq,subcourse_code,difficulty,id1)
