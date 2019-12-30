mainList = input().split()
num = int(input())


def recurs(resultList, deltaList):
    if len(resultList) == num:
        print(resultList)
    else:
        for i in range(0, len(deltaList)):
            nextResultList = resultList.copy()
            nextResultList.append(deltaList[i])
            recurs(nextResultList, deltaList[i + 1:len(deltaList)])


recurs([], mainList)
