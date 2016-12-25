#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Interval(object):
    """docstring for Interval"""
    def __init__(self, start,end):
        #super(Interval, self).__init__()
        self.start = start
        self.end = end

        
def insert(intervals,newInterval):
    result = []
    insertPos = 0
    for interval in intervals:
        if interval.start > newInterval.end:
            result.append(interval)
        elif interval.end < newInterval.start:
            insertPos += 1
            result.append(interval)
        else:
            newInterval.start = min(interval.start,newInterval.start)
            newInterval.end = max(interval.end,newInterval.end)
    result.insert(insertPos,newInterval)
    print("len(result)",len(result),"result",result) 
    return result

if __name__ == "__main__":
    interList = [Interval(1,2),Interval(5,9)]
    s1 = (insert(interList,Interval(2,5)))
    for s in s1:
        print(s.start,s.end)

    s2 = (insert(interList,Interval(3,4)))
    for s in s2:
        print(s.start,s.end)
