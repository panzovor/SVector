__author__ = 'E440'
import dir

def load_data():
    all_sen_path = dir.resources+"stanfordSentimentTreebank\\datasetSentences.txt"
    split_sen_path = dir.resources+"stanfordSentimentTreebank\\datasetSplit.txt"
    label_sen_path = dir.resources+"stanfordSentimentTreebank\\sentiment_labels.txt"
    dictionary_sen_path = dir.resources+"stanfordSentimentTreebank\\dictionary.txt"
    all_sen = read(all_sen_path)
    split_sen = read(split_sen_path)
    label_sen = read(label_sen_path)
    dictionary_sen = read(dictionary_sen_path)
    return all_sen,split_sen,label_sen,dictionary_sen

def seperate_data(two = False):
    all_sen,split_sen,label_sen,dict_sen = load_data()
    split_dict= build_dict(split_sen)
    label_dict= build_dict(label_sen)
    dict_dict= build_dict(dict_sen)
    train,validation,test=[],[],[]
    # print(len(label_dict))
    count = 0
    for sen in all_sen:
        sentence = sen[1].replace("-LRB-","(")
        sentence = sentence.replace("-RRB-",")")
        try:
            count+=1
            label = label_dict[dict_dict[sentence]]
            value = float(label)
            if value<0.2: label =1
            elif value<0.4: label = 2
            elif value<0.6: label =3
            elif value<0.8: label = 4
            else: label =  5
            if two:
                if label == 1 or label ==2:
                    label =0
                elif label == 4 or label  == 5:
                    label =1
                else:
                    continue
            if split_dict[sen[0]] == "1":
                train.append([sen[1],label])
            elif  split_dict[sen[0]] == "2":
                validation.append([sen[1],label])
            else:
                test.append([sen[1],label])
        except:
            print(count,len(all_sen),sentence)
            input()
    return train,validation,test

def build_dict(data,key_index =0):
    result ={}
    for tmp in data:
        if tmp[key_index] not in result.keys():
            result[tmp[key_index]] =tmp[1]
    return result


def read(path):
    data = []
    with open(path,mode="r") as file:
        lines = file.readlines()
        first_line = lines[0]
        if "|" in first_line:
            seperator = "|"
        elif "\t" in first_line:
            seperator = "\t"
        elif "," in first_line:
            seperator = ","
        length = len(first_line.split(seperator))
        for i in range(1,len(lines)):
            line = lines[i].strip()
            if seperator in line:
                tmp = line.split(seperator)
                if length  == len(tmp):
                    data.append(tmp)
    return data

if __name__ == "__main__":
    load_data()