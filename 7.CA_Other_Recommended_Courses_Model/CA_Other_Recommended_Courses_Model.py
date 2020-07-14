import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("C:/Users/Archit/Desktop/ArcInternship/Dataset/Master.csv",encoding='latin1')#backend and AIML here dataset should be dynamic
with open('C:/Users/Archit/Desktop/ArcInternship/Dataset/input_orc.json',encoding='utf-8') as jsonfile:#here the json file should be dynamic(BACKEND AND AIML)
    data = json.load(jsonfile,)#json files data is stored in data

index=[]
for i in range(511):#AIML here I guess 89 courses for caramel IT change range accordingly
    index.append(i)
df["index"]=index
features = ['Tags']
def combine_features(row):
    return row['Tags']
for feature in features:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string
df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
df.iloc[0].combined_features
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)
def get_Course_Name_from_index(index):
    return df[df.index == index]["Course Name"].values[0]
def get_index_from_Course_Name(Course_Name):
    return df[df["Course Name"] == Course_Name]["index"].values[0]

#course_user_likes = "Natural Language Processing with Deep Learning in Python"#AIML this should be commented out when course_user_likes comes from json
#AIML AND BACKEND course_user_likes should fetch data from json
#Course_index = get_index_from_Course_Name(course_user_likes)
Course_index=int(data['courseId'])
print(Course_index)
similar_courses = list(enumerate(cosine_sim[Course_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
sorted_similar_courses = sorted(similar_courses,key=lambda x:x[1],reverse=True)[1:]
i=0
list1=[]
id1=data['user_id']
#print("Top 5 similar courses to "+course_user_likes+" are:\n")#AIML Comment out
for element in sorted_similar_courses:
    list1.append(element[0])
    #list1.append((get_Course_Name_from_index(element[0])))
    i=i+1
    if i>5:
        break
#print(list1)
json_object = json.dumps(list1)
with open(id1+"orc.json", "w") as outfile:
            outfile.write(json_object)
