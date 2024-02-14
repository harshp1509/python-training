def removeduplicate(l1):
    return list(set(l1))

def addition(l3):
    return sum(l3)

l=[1,2,3,8,5,6,4,2,68,2,5,2,4]
print(removeduplicate(l))
l.sort()
print(l)
print(addition(l))


cnty=("india","pakistan","canada","sri-lanka","nepal")
print(len(cnty))
res=False
c="nepal"
for x in cnty:
    if c==x:
        res=True
        break
if res:
    print("given country is present in given list")
else:
    print("given country name is not present in the given list")

cnty2=("USA","UAE","Russia","iran","london")
rcnty=cnty+cnty2
print(rcnty)
lcnty=list(rcnty)
lcnty[2]="iceland"
rcnty=list(lcnty)
print(rcnty)


ditems={"pencil":38,"pen":30,"books":56,"campassbox":10,"graphs":53,"erasers":40}
ditems["schoolbag"]=20
print(ditems)
ditems["books"]=26
print(ditems)
del ditems["campassbox"]
print(ditems)

print(sorted(ditems.items(),key=lambda ditems:ditems[0]))

listcom=[]

for i in range(2,20,2):
    listcom.append(i*i)

print(listcom)

citypop={"ahmedabad":52516556,"surat":50624274,"jamnagar":3591296,"gandhinagar":6542632,"nadiad":25481926}

print(max(citypop,key=lambda x:citypop[x]))

def check(x, y,z):
    if(x== y == z):
        print("Equilateral Triangle")
    elif(x==y or y==z or z==x):
        print("isosceles triangle")
    else:
        print("scalene traiangle")

check(8,7,9)

studentinfo=[("jay",85),("yash",95),("kishan",75),("dipak",46),("harsh",83),("krupa",78),("janvi",62)]
studentinfo.sort(key=lambda x:x[-1],reverse=True)
print(studentinfo)

for i  in range(0,3):
    print(studentinfo[i][0])

def filter_items_by_price(items, threshold):
    print(items.items())
    filtered_items = {item: price for item, price in items.items() if price >= threshold}
    return filtered_items

item_prices = {
    'apple': 150,
    'banana': 75,
    'orange': 200,
    'grapes': 350,
    'bread': 250,
    'milk': 180
}

th_price = 200

filtered_items = filter_items_by_price(item_prices, th_price)

print(f"Items with prices greater than or equal to {th_price}:")
for item, price in filtered_items.items():
    print(f"{item}: {price}")



def list_operations(list1, list2):
    intersection = list(set(list1) & set(list2))

    union = list(set(list1) | set(list2))

    difference_in_list1 = list(set(list1) - set(list2))

    return intersection, union, difference_in_list1

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection_result, union_result, difference_result = list_operations(list1, list2)

print(f"Intersection of the two lists: {intersection_result}")
print(f"Union of the two lists: {union_result}")
print(f"Elements present in the first list but not in the second list: {difference_result}")



def find_oldest_and_youngest(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))

    oldest_person = min(dictionary, key=lambda k: dictionary[k])
    youngest_person = max(dictionary, key=lambda k: dictionary[k])

    return oldest_person, youngest_person

age_dictionary = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 22,
    'David': 35,
    'Eve': 28
}

oldest, youngest = find_oldest_and_youngest(age_dictionary)

print(f"The oldest person is: {oldest} with age {age_dictionary[oldest]}")
print(f"The youngest person is: {youngest} with age {age_dictionary[youngest]}")
