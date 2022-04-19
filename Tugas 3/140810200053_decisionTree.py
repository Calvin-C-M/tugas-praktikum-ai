'''
JUDUL PROGRAM   : Decision Tree
NAMA            : Calvin Calfi Montolalu
NPM             : 140810200053
KELAS           : A
'''

import pandas as pd
import numpy as np
import math
from treelib import Tree

class Data :
    def __init__(self,outlook,temp,humid,wind,decision) :
        self.outlook=outlook
        self.temp=temp
        self.humid=humid
        self.wind=wind
        self.decision=decision

def getData(file) :
    dataset=Data([],[],[],[],[])
    for text in file :
        line=text.split(",")
        dataset.outlook.append(line[0])
        dataset.temp.append(line[1])
        dataset.humid.append(line[2])
        dataset.wind.append(line[3])
        dataset.decision.append(line[4].strip("\n"))
    return dataset

def total(S) :
    count=0
    for dec in S :
        count += dec
    return count

# S = 1 dim array
def entropy(S) :
    totalS=total(S)
    p=0
    for dec in S :
        if dec == 0:
            p=0
            break
        p += (-dec/totalS) * math.log2(dec/totalS)
    return p

# S = 1 dim array
# attribute = 2 dim array
def gain(S,attribute) :
    sigmaT=0

    for attr in attribute :
        sigmaT += (total(attr)/total(S)) * entropy(attr)

    return entropy(S)-sigmaT if len(attribute) > 0 else 0

def processDecision(data) :
    dictionary=dict.fromkeys(data,0)

    for d in dictionary.keys() :
        dictionary.update({d: data.count(d)})

    return dictionary.values()

def processAttribute(data,dataDec) :
    attribute=[]
    if len(data) > 0 :
        dictionary=dict.fromkeys(data,{})

        for d in dictionary.keys() :
            decDictionary=dict.fromkeys(dataDec,0)

            for i in range(0,len(data)) :
                if d == data[i] :
                    prevVal=decDictionary.get(dataDec[i])
                    decDictionary.update({dataDec[i]: prevVal+1})

            dictionary.update({d: decDictionary})

        for d in dictionary.values() :
            attribute.append(d.values())

    return attribute

def divide(data) :
    indexes=dict.fromkeys(data,[])

    for i in indexes.keys() :
        indexList=[]
        for index in range(0,len(data)-1) :
            if i == data[index] :
                indexList.append(index)
        indexes.update({i: indexList})

    return indexes

def isEndNode(index, dataDec) :
    count=0
    firstIndex=index[0]
    for i in index :
        if dataDec[i] == dataDec[firstIndex] :
            count += 1

    return True if count == len(index) else False

def allAttrEmpty(data) :
    temp=data.copy()
    temp.pop("Decision")
    for d in temp.values() :
        print(d)
        if len(d) > 0 :
            return False
    return True

def decisionTree(data) :
    subjectData={
        "Outlook":data.outlook,
        "Temp":data.temp,
        "Humid":data.humid,
        "Wind":data.wind,
        "Decision":data.decision
    }

    tree=Tree()

    sd=subjectData.copy()
    prevParent=""

    # ===== START LOOP =====
    while allAttrEmpty(sd) == False :
        outlook=processAttribute(sd["Outlook"],sd["Decision"])
        temp=processAttribute(sd["Temp"],sd["Decision"])
        humid=processAttribute(sd["Humid"],sd["Decision"])
        wind=processAttribute(sd["Wind"],sd["Decision"])
        decision=processDecision(sd["Decision"])

        gains={
            "Outlook": gain(decision,outlook),
            "Temp": gain(decision,temp),
            "Humid": gain(decision,humid),
            "Wind": gain(decision,wind)
        }

        maxGainIndex=np.argmax(list(gains.values()))

        if maxGainIndex == 0 : # If outlook gain is higher
            tree.create_node("Outlook","outlook")
            div=divide(data.outlook)
            prevParent="outlook"
            for d in div.values() :
                if isEndNode(d, data.decision) :
                    tree.create_node(data.decision[d[0]], data.decision[d[0]]+"_outlook", parent=prevParent)

            sd["Outlook"]=[]

        elif maxGainIndex == 1 : # If temp gain is higher
            tree.create_node("Temp","temp",parent=prevParent)
            div=divide(data.temp)
            prevParent="temp"

            for d in div.values() :
                if isEndNode(d, data.decision) :
                    tree.create_node(data.decision[d[0]], data.decision[d[0]]+"_temp", parent=prevParent)

            sd["Temp"]=[]

        elif maxGainIndex == 2 : # If humid gain is higher
            tree.create_node("Humid","humid",parent=prevParent)
            div=divide(data.humid)
            prevParent="humid"

            for d in div.values() :
                if isEndNode(d, data.decision) :
                    tree.create_node(data.decision[d[0]], data.decision[d[0]]+"_humid", parent=prevParent)
            sd["Humid"]=[]

        elif maxGainIndex == 3 : # If wind gain is higehr
            tree.create_node("Wind","wind",parent=prevParent)
            div=divide(data.wind)
            prevParent="wind"

            for d in div.values() :
                if isEndNode(d, data.decision) :
                    tree.create_node(data.decision[d[0]], data.decision[d[0]]+"_wind", parent=prevParent)

            sd["Wind"]=[]

    # ===== END LOOP =====

    # Visualisasi Data 
    print("\nData Frame")
    dataFrame=pd.DataFrame(subjectData)
    print(dataFrame)

    # Visualisasi Tree
    print("\nVisualisasi Tree")
    tree.show()

def main() :
    file1=open("./ML-Dataset/golf.txt")

    attributeNames=file1.readline().strip("\n").split(",")
    dataset1=getData(file1)

    decisionTree(dataset1)
    return 0

main()