import random
import sys

def FIFO(size,pages):
    memory = []
    pages = pages.split()
    replacement_index = 0;
    page_faults = 0;
    for page in pages:
        if len(memory) < int(sys.argv[2]):
            if page in memory:
                continue
            else:
                memory.append(page)
        else:
            if page in memory:
                continue
            else:
                memory[replacement_index] = page
                replacement_index+=1
                page_faults+=1
                if replacement_index > size:
                    replacement_index = 0
        print(memory)
    return page_faults;

def main():
    pages = ""
    for i in range(0,int(sys.argv[1])):
        pages+= str(random.randint(0,9)) +  " "
    print(pages)
    print()
    size = int(sys.argv[1])
    print("FIFO", FIFO(size,pages), "page faults.")
    #print("LRU", LRU(size,pages), "page faults.")
    #print("OPT", OPT(size,pages), "page faults.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
