import random
import sys
from collections import deque

def FIFO(size,pages):
    memory = []
    pages = pages.split()
    replacement_index = 0
    page_hits = 0
    for page in pages:
        if len(memory) < int(sys.argv[2]):
            if page in memory:
                page_hits+=1
                continue
            else:
                memory.append(page)
        else:
            if page in memory:
                page_hits+=1
                continue
            else:
                memory[replacement_index] = page
                replacement_index+=1
                if replacement_index > int(sys.argv[2])-1:
                    replacement_index = 0
    print(page_hits)
    return len(pages)-page_hits

def LRU(size,pages):
    memory = deque([])
    pages = pages.split()
    page_hist = 0
    replacement_index = 0
    for page in pages:
        if len(memory) < int(sys.argv[2]):
            if page in memory:
                page_hist+=1
                memory.remove(page)
                memory.append(page)
            else:
                memory.append(page)

        else:
            if page in memory:
                page_hist+=1
                memory.remove(page)
                memory.append(page)
            else:
                memory.popleft()
                memory.append(page)
    return len(pages)-page_hist

#def OPT(size,page):


def main():
    pages = ""
    for i in range(0,int(sys.argv[1])):
        pages+= str(random.randint(0,9)) +  " "
    #print(pages)
    #print()
    if int(sys.argv[1]) == 8:
        pages = "8 5 6 2 5 3 5 4"

    if int(sys.argv[1]) == 16:
        pages = "8 5 6 2 5 3 5 4 2 3 5 3 2 6 2 5"

    if int(sys.argv[1]) == 24:
        pages = "8 5 6 2 5 3 5 4 2 3 5 3 2 6 2 5 6 8 5 6 2 3 4 2"

    if int(sys.argv[1]) == 32:
        pages = "8 5 6 2 5 3 5 4 2 3 5 3 2 6 2 5 6 8 5 6 2 3 4 2 1 3 7 5 4 3 1 5"
    size = int(sys.argv[1])
    print("FIFO", FIFO(size,pages), "page faults.")
    print("LRU", LRU(size,pages), "page faults.")
    #print("OPT", OPT(size,pages), "page faults.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
