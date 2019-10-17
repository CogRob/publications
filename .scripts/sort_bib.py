#!/usr/bin/env python3

import argparse
import string

SEPARATOR="@"
SORT_KEY="author" #As of yet, not sorting on this key
DEBUG=True

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("bibfile", help="Include the bibfile you want sorted")
    return parser.parse_args()

def get_val(key,str):
    """
    Get the value of the element associated with the
    bibtex key.  Right now the key doesn't do anything.
    
    TODO:  Get this to work for an arbitrary key.
    """
    # Pull out the slug for each tex item:  assume in alphabetical order
    return str[str.find('{')+1:str.find(',')]
    

def insert_alpha(index,sorted_list,elem,prev_lt):
    """
    Takes bibtex string elem and returns sorted_list
    with elem placed in it in its aphabetical location.
    
    prev_lt predicate to determine
    
    TODO: You could make this a binary search.  Right now it's
    linear.
    """
    if get_val(SORT_KEY,elem)<get_val(SORT_KEY,sorted_list[index]):
        if index==0:
            # if DEBUG: 
                # print("LT/BC: ",index,", "+get_val(SORT_KEY,elem)+", "+get_val(SORT_KEY,sorted_list[index])) 
            return sorted_list.insert(index,elem)
        else:
            index-=1
            # if DEBUG: 
                # print("LT/UC: ",index,", "+get_val(SORT_KEY,elem)+", "+get_val(SORT_KEY,sorted_list[index])) 
            return insert_alpha(index,sorted_list,elem,True)
    else:
        if index==len(sorted_list)-1 or prev_lt:
            # if DEBUG: 
                # print("GT/BC: ",index,", "+get_val(SORT_KEY,elem)+", "+get_val(SORT_KEY,sorted_list[index]))
            return sorted_list.insert(index+1,elem)
        else:
            index+=1
            # if DEBUG: 
                # print("GT/UC: ",index,", "+get_val(SORT_KEY,elem)+", "+get_val(SORT_KEY,sorted_list[index])) 
            return insert_alpha(index,sorted_list,elem,False)

def main():
    args=parse_args()
    f=open(args.bibfile,'r')
    infile=f.read()
    # items=string.split(infile,SEPARATOR)
    items=infile.split(SEPARATOR)
    
    # print(string.find(items[1],"author"))
    # print(items[1].find("author"))
    
    sorted=list()
    sorted.append(items[1])   # Zero-ith element is the empty string
    for i in range(len(items))[2:]:
        insert_alpha(0,sorted,items[i],False)
        # if DEBUG: print("***************************************************************")
    
    sorted= [SEPARATOR+sorted[i] for i in range(len(sorted))]
    
    sortfile=args.bibfile+"-sorted2"
    fnew=open(sortfile,'w')
    # fnew.write(string.join(sorted,'\n'))
    fnew.write(''.join(sorted))
    f.close()
    fnew.close()

if __name__ == "__main__":
    main()
