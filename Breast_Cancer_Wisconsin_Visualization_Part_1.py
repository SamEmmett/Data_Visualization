import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt


def readCSV(): #Reads the CSV file and returns it for use.
    
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", header = None)
    data.columns = ['Sample Code Number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class'     ]
    return data

def printQuantitatve(dataset): 
    for col in dataset.columns:
        if col != 'Sample Code Number' and col != 'Class': #Prints everything except the first and last columns based on column name
            if is_numeric_dtype(dataset[col]):
                print('%s:' % (col))
                print('\t Mean = %.2f' % dataset[col].mean())
                print('\t Standard deviation = %.2f' % dataset[col].std())
                print('\t Minimum = %.2f' % dataset[col].min())
                print('\t Maximum = %.2f' % dataset[col].max())

        
def printFreq(dataset):
    # for col in dataset.columns:
        print('Sample Code Number')
        print(dataset['Sample Code Number'].value_counts()) #prints the freqency of the 
        print()
        print('Class')
        print(dataset['Class'].value_counts())
        

def printDescription(dataset): # prints description of data
    print(dataset.describe(include='all'))

def boxPlot(dataset): #displays a boxPlot of Clump Thickness Column
    plt.boxplot(dataset['Clump Thickness'])
    plt.show()


def scatterPlot(dataset): #creates a scatterplot of cell size and cell shape columns
   
    plt.scatter(dataset['Uniformity of Cell Size'], dataset['Uniformity of Cell Shape'], color='red') #sets params for Math plots
    plt.title('Size and Shape') #Plot title
    plt.xlabel('Cell Size') #x-axis label
    plt.ylabel('Cell Shape') #y-axis label
    plt.show()

def corr(data):
    print(data)
    print(data['Clump Thickness'].corr(data['Class']))


def run():
    data = readCSV()
    print(data)
    print()
    printQuantitatve(data)
    print()
    printFreq(data)
    print()
    printDescription(data)
    boxPlot(data)
    scatterPlot(data)
    corr(data)
    
if __name__ == '__main__':
   run()
  
 
  
