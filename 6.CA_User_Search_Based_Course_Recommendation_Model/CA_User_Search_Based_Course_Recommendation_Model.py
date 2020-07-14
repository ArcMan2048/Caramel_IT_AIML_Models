import pandas as pd
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
from IPython.display import display
with open('C:/Users/Archit/Desktop/ArcInternship/Dataset/input_usb.json',encoding='utf-8') as jsonfile:#here the json file should be dynamic(BACKEND AND AIML)
    data = json.load(jsonfile,)#json files data is stored in data


df = pd. read_csv('C:/Users/Archit/Desktop/ArcInternship/Dataset/Master.csv',encoding='latin1')
df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1, inplace=True)
#df.head()


vote_counts = df[df['Users Reviewed'].notnull()]['Users Reviewed'].astype('int')
vote_averages = df[df['Ratings'].notnull()]['Ratings'].astype('int')
C = vote_averages.mean()
C

m = vote_counts.quantile(0.95)
m

qualified = df[(df['Users Reviewed'] >= m) & (df['Users Reviewed'].notnull()) & (df['Ratings'].notnull())][['Course ID','Course Name','Ratings','Users Reviewed','Hours','Lectures','Tags']]
qualified['Users Reviewed'] = qualified['Users Reviewed'].astype('int')
qualified['Ratings'] = qualified['Ratings'].astype('int')
qualified.shape

def weighted_rating(x):
    v = x['Users Reviewed']
    R = x['Ratings']
    return (v/(v+m) * R) + (m/(m+v) * C)

qualified['wr'] = qualified.apply(weighted_rating, axis=1)

qualified = qualified.sort_values('wr', ascending=False).head(250)

#d=input("Search for anything:")#User enters course
#id1=input("Enter the userid")
id1=data['user_id']#user id from the json file questions.json
d=data['search']#user id from the json file questions.json
course_list=[]#imp
course_list2=[]#imp

def get_ratio1(row):#first it will sort on the basis of course names
    #name = row['Tags']
    name2=row['Course Name']
    return fuzz.token_set_ratio(d, name2)
def get_ratio2(row):#sorting on the basis of tags
    #name1=
    name = row['Tags']
    #name2=row['Course Name']
    return fuzz.token_set_ratio(d, name)
df3=df[df.apply(get_ratio1, axis=1) >30].head(50)#check empty
#print(df3)
df4=df[df.apply(get_ratio2, axis=1) >30].head(50)#check if empty
if(df3.empty==False):
    res1=df[df.apply(get_ratio1, axis=1) >50]
    #print(res1)
    res2=res1.head(50)
    res2=res2[['Course ID']]
    length1=len(res2)
    for i in range(length1):
        course_list1=res2['Course ID'].values[i]
        course_list1=int(course_list1)
        course_list.append(course_list1)
elif(df4.empty==False):
    res2=df[df.apply(get_ratio2, axis=1) >50]
    res2=res1.head(100)
    res2=res2[['Course ID']]
    length1=len(res2)
    for i in range(length1):
        course_list1=res2['Course ID'].values[i]
        course_list1=int(course_list1)
        course_list.append(course_list1)
else:#AIML TEST THIS PIECE OF CODE BELOW
    #print("Sorry we could not find what you were looking for!!!")
    #print("Here is a list of our top rated courses instead")
    for i in range(250):#AIML CHANGE 250 ACCORDING TO NUMBER OF COURSES IN THE CARAMELIT WEBSITE
        course_list1=qualified['Course ID'].values[i]
        course_list1=int(course_list1)
        course_list.append(course_list1)
        #display(qualified.head(15))
    #get the top courses
    #print("Search again")#redirect it to search bar

#print(course_list)
json_object = json.dumps(course_list)
with open(id1+"usb.json", "w") as outfile:
            outfile.write(json_object)
