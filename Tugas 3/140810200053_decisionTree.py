import pandas as pd
import numpy as np
import math

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

    return entropy(S)-sigmaT

def processDecision(data) :
    dictionary=dict.fromkeys(data,0)

    for d in dictionary.keys() :
        dictionary.update({d: data.count(d)})

    return dictionary.values()

def processAttribute(data,dataDec) :
    attribute=[]
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

def main() :
    file1=open("./ML-Dataset/golf.txt")

    attributeNames=file1.readline().strip("\n").split(",")
    dataset1=getData(file1)

    decision=processDecision(dataset1.decision)

    outlook=processAttribute(dataset1.outlook,dataset1.decision)

    # print(outlook)

    # Testing gain algorithm
    # test=gain([6,4],[[1,4],[5,0]])
    test=gain(decision,outlook)

    print(test)
    return 0

main()