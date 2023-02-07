from math import dist
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import pdist, squareform

def jaccard_arr(list1, list2):  #function for the jaccard similarity of the array
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection

    sim = float(intersection) / union
   
    print("The Jaccard Similarity is: " + str(sim))
    return 

def jaccard_sent(data): #function for the jaccard similarity of the sentences
    sentA = set(data[0].lower().split())
    sentB = set(data[1].lower().split())
    sentC = set(data[2].lower().split())

   
    intersection = set.intersection(sentA, sentB, sentC)
    union = set.union(sentA, sentB, sentC)

    sim = float(len(intersection)) / len(union)

    print("The Jaccard similarity of the 3 sentences is: " + str(sim))
    print()

def corr (data1, data2): #Correlation Method
    print("Correlation of arrayA and arrayB")
    print(data1['arrayA'].corr(data1['arrayB'])) #Correlation of Array
    print()
    print("Correlation of Sentence A with B and C") #Correlation of Sentence A with B and C
    print(data2.corrwith(data2.iloc[0], axis=1))
    print()
    print("Correlation of Sentence B with A and C") #Correlation of Sentence B with A and C
    print(data2.corrwith(data2.iloc[1], axis=1))
    print()
    print("Correlation of Sentence C with B and C") #Correlation of Sentence C with B and C
    print(data2.corrwith(data2.iloc[2], axis=1))
    print()

def cos(data1, data2): #Method for Cosine-Similarity of both Array and Sentences
    print("Cosine Similarity of Array A and B")
    similarity1 = cosine_similarity(data1)
    print(similarity1)
    print()

    similarity2 = cosine_similarity(data2)
    print("Cosine Similarity of Sentences")
    print(similarity2)
    print()

def euc_Arr(list1, list2): #Method for Euclidian distance of the Arrays
    print("Array Euclidian Distance")
    print("The euclidian distance from Array A to Array B is: " + str(dist(list1, list2)))

def euc_Sent(data): #Method for Euclidian distance of the sentences
    print("The Euclidean distance of the 3 sentences is:")

    distance = pdist(data.values, metric = 'euclidean')
    dist_matrix = squareform(distance)

    print(dist_matrix)
    
if __name__ == '__main__':
    arrayA = [0,1,0,1,0,1,0,0,0,1]
    arrayB = [0,1,0,0,0,1,1,0,0,0]
    data1 = pd.DataFrame({'arrayA': arrayA, 'arrayB': arrayB})


    sentenceA = "Data mining is the process of extracting and discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems."
    sentenceB = "Data mining is the process of analyzing data, extracting patterns, discovering trends, and gaining insights using machine learning, database, statistics, and mathematics."
    sentenceC = "Coal mining is the process of extracting coal from the ground, involving discovering, exploration, and production"

    corpus = [sentenceA, sentenceB, sentenceC]
    vectorizer = TfidfVectorizer()
    trsfm = vectorizer.fit_transform(corpus)
    data2 = pd.DataFrame(trsfm.toarray(), columns=vectorizer.get_feature_names_out(), index = ['sentenceA', 'sentenceB', 'sentenceC'] )

    cos(data1, data2)
    corr(data1, data2)

    print("Jaccard Similarity of Array A and B")
    jaccard_arr(arrayA, arrayB)
    print()

    print("Jaccard Similarity of the Sentences")
    jaccard_sent(corpus)

    euc_Arr(arrayA, arrayB)
    euc_Sent(data2)
