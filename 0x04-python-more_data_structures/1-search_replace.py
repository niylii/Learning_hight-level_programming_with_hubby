#!/usr/bin/pythons3
def search_replace(my_list, search, replace):
    mlist = my_list.copy()
    for i in range(len(mlist)):
        if search == mlist[i]:
            mlist[i] = replace
    return mlist
