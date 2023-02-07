import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def readCSV(): #Reads the CSV file and returns it for use.
    
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', header = None)
    data.columns = ['Sample Code Number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class'     ]
    return data

def practice1(dataset): #practice 1


    print("PRACTICE 1")
    print("Before the drop")
    print("Attributes and Instances: " + str(dataset.shape)) #Prints attributes and instances
    print() #spacing

    print("After the drop")
    dataset = dataset.drop(columns="Sample Code Number") #drops the SCN column from the dataframe
    print("Attributes and Instances: " + str(dataset.shape)) #Prints attributes and instances
    print() #spacing

    

    return dataset
    
def practice2(dataset): #Practice 2
        print("PRACTICE 2")
        print("Before Replacement:")
        print(dataset[290:300]) #I Chose this range since there are a good number of missing values
        print()

        for col in dataset[1:-1]: #iterates accross all columns
            dataset.loc[dataset[col] == "?", col] = np.NaN #Replaces '?' with NaN values buy using mask function 

        print("After Replacement:")
        print(dataset[290:300]) #I Chose this range since there are a good number of missing values
        print()

def practice3(dataset): #Practice 3
    print("PRACTICE 3")

    data = dataset.copy() #this way we won't need to read the doc again and it will remain un altered for the next part

    print("Before Replacement:")
    print(str(data.shape))

    for col in data[1:-1]: #iterates across all columns
        
        data[col] = pd.to_numeric(data[col])
        data[col] = data[col].fillna(data[col].mean()) #Replaces 'NaN' values with the mean of the column values buy using mask function
        
    print("After Replacement:")
    print(str(data.shape)) #output will not be different since the row and column count did not change
    print()

def practice4(dataset): #Practice 4
    print("PRACTICE 4")

    print("Before dropna():")
    print(str(data.shape))
   
    new = dataset.dropna() #Replaces 'NaN' values with the mean of the column values buy using mask function

    print("After dropna():")
    print(str(new.shape)) #output will not be different since the row and column count did not change
    print()

def practice5(dataset): #Practice 5
    print("Practice 5")
    print("see graph")
    for col in dataset[1:-1]: #iterates across all columns
        dataset[col] = pd.to_numeric(dataset[col]) #makes each column numeric

    column = ['Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    plt.boxplot(dataset[column])
    plt.show()
    print()

def practice6(dataset): #Practice 6
    print("Practice 6")
    print("Before Drop")
    print(dataset.shape)
    for col in dataset:
        mean = np.mean(dataset[col])
        std = std = np.std(dataset[col])

        for i in dataset[col].index.values:
            val = dataset._get_value(i, col)
            z = (val-mean)/std

            if z > 0:
                new = dataset.drop(dataset.index[i])
    print("After Drop")
    print(new.shape) 
    print()    

def practice78(dataset): #Practice 7 and 8   
    print("Practice 7")
    print(dataset.duplicated()) #Practice 7
    print()
    print("Practice 8")
    print(dataset.shape) #practice 8
    new = dataset.drop_duplicates()
    print(new.shape)
    print()
def practice9(dataset): #practice 9

    print()
    print("PRACTICE 9")
    replaced = dataset.sample(frac =.01, replace= True, random_state= 1)
    print(replaced)
    print()
    not_replaced = replaced = dataset.sample(frac =.01, replace= False, random_state= 1)
    print(not_replaced)




if __name__ == '__main__':

    data = readCSV() #I seperated this from practice1 because it will allow for the data variable to be reused without needing to scan the document each time
    data = practice1(data) #Practice 1
    practice2(data) #Practice 2 NOTE: I did not actually return this because the inplace attribute alters the dataframe
    practice3(data) #Practice 3 NOTE: output of practice 3 did not change because row and column count is still the same
    practice4(data) #Practice 4
    practice5(data) #Practice 5
    practice6(data) #Practice 6
    practice78(data) #Practice 7 and 8
    practice9(data) #Practice 9
    
