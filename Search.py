# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:37:20 2020

@author: Rishabh
"""
import Searcher as s
import ColorDescriptor as c
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--index",required=True,
    help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
 	help = "Path to the query image")
ap.add_argument("-r", "--result_path", required = True,
 	help = "Path to the result path")
args = vars(ap.parse_args())
cd= c.ColorDescriptor((8, 12, 3))
query = cv2.imread(args["query"])
cv2.imshow("querys",query)
cv2.waitKey(0)
features = cd.describe(query)

searcher = s.Searcher(args["index"])
results =searcher.search(features)

cv2.imshow("Query",query)
print(args["result_path"])
for(score,resultID) in results:
    print(resultID)
    result = cv2.imread(resultID)
    cv2.imshow("Result",result)
    cv2.waitKey(0)






