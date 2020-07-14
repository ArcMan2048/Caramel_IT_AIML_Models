import pandas as pd
import numpy as np
import json #library needed
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:/Users/Archit/Desktop/ArcInternship/Dataset/Master.csv",encoding='latin1')
with open('C:/Users/Archit/Desktop/ArcInternship/Dataset/CRinput.json',encoding='utf-8') as jsonfile:#here the json file should be dynamic(BACKEND AND AIML)
    data = json.load(jsonfile,)#json files data is stored in data
##print(df.head())
##df.drop(['Unnamed: 7','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6'], axis=1, inplace=True)
##df.shape
index=[]
for i in range(511):
    index.append(i)
df["index"]=index

##print(df.head())
features1 = ['Tags']
def combine_features1(row):
    return row['Tags']
for feature in features1:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string
df["combined_features1"] = df.apply(combine_features1,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

#features2 = ['user_feedback']
#def combine_features2(row):
#    return row['Ratings']
#for feature in features2:
#    df[feature] = df[feature].fillna('') #filling all NaNs with blank string
#df["combined_features2"] = df.apply(combine_features2,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

#features3 = ['user_score']
#def combine_features3(row):
#    return row['Ratings']
#for feature in features3:
#    df[feature] = df[feature].fillna('') #filling all NaNs with blank string
#df["combined_features3"] = df.apply(combine_features3,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column

##print(df.iloc[0].combined_features)

cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features1"]) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)

def get_Course_Name_from_index(index):
    return df[df.index == index]["Course Name"].values[0]
def get_index_from_Course_Name(Course_Name):
    return df[df["Course Name"] == Course_Name]["index"].values[0]

#MAIN IMPORTANT PART OF THE CODE(INPUT)
#course_user_likes = "Learn and Understand NodeJS"
course_user_likes = data['course_name']
Course_index = get_index_from_Course_Name(course_user_likes)
influenced_courses = list(enumerate(cosine_sim[Course_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
sorted_influenced_courses = sorted(influenced_courses,key=lambda x:x[1],reverse=True)[1:]


RClist=[]
i=0
print("\nUsers who bought "+course_user_likes+" also bought:\n")
for element in sorted_influenced_courses:
    temp=get_Course_Name_from_index(element[0])
    RClist.append(temp)
    print(temp)
    i=i+1
    if i>5:
        break
print("\n")
dffinal=pd.DataFrame(RClist,columns=['Influenced Course'])
#print(dffinal)
dffinal.to_json(r'C:/Users/Archit/Desktop/ArcInternship/Dataset/'+'CRoutput.json')
