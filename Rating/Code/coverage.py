import csv
import os
from hit_builder import *
from xml_builder import *
from data import *
from random import shuffle
from Node import Node
from MQueue import mQueue


def ask(data):
    sandbox_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
    # prod_url = 'https://mturk-requester.us-east-1.amazonaws.com'
    new_xml = Xml(data, 5, 'https://cov-img.s3.amazonaws.com/feret-full/')
    new_xml.xml_builder()
    new_hit = Hit(sandbox_url, 'hit.xml', 'Image data coverage', 'Answer to a yes-no question about a set of images', '0.05',
                  3)
    hit_id = new_hit.create()
    result = new_hit.result(hit_id)
    return result


def coverage(dataset, n, k):
    count = 0
    qs = 0
    Q = mQueue()
    for i in range(0, len(dataset), n):
        root = Node(data=dataset[i:i + n])
        Q.put(root)
    # print(dataset)
    while not (Q.empty()):
        node = Q.get()
        print(node.get_data())
        parent = node.get_parent()
        ans = ask(node.get_data())
        qs += 1
        if parent is None:
            if ans:
                count += 1
            else:
                continue
        else:
            if not ans:
                if node == parent.get_left():
                    node = Q.get_element(parent.get_right())
                else:
                    continue
            if parent.is_checked():
                count += 1
            else:
                parent.set_checked(True)
        if count == k:
            return True, qs
        set = node.get_data()
        if len(set) > 1:
            lchild = Node(data=set[:len(set)//2], parent=node)
            rchild = Node(data=set[len(set)//2:], parent=node)
            node.add_child(lchild)
            node.add_child(rchild)
            Q.put(lchild)
            Q.put(rchild)
    return False, qs


# main

dataset = Data('data_full.csv').dataset_init()
shuffle(dataset)
N = len(dataset)  # dataset size
# print(N)
n = 50  # subset size
k = 50  # coverage threshold
result, questions = coverage(dataset, n, k)
print(result, questions)
f = open('log.txt', 'a')
f.write('result: ' + str(result) + '\t' + 'questions: ' + str(questions) + '\n')
f.close()
