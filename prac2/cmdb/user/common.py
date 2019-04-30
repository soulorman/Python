#enconding: utf-8
from .models import Hardware_Information

def getDictValues(oldDict, newDicts):
    for key,value in oldDict.items():
        if isinstance(value, dict):
            getDictValues(value, newDicts)
        elif isinstance(value, list):
            for data in value:
                if isinstance(data, dict):
                    getDictValues(data, newDicts)
        else:
            newDicts[key]=value

    return newDicts

def loopValue():
    newData = []

    # return [ newDict for info in  Hardware_Information.objects.all().values() getDictValues(info, newDict) ]
    for info in Hardware_Information.objects.all().values():
        newDict = {}
        newData.append(getDictValues(info, newDict))

    return newData