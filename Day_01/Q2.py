# create a function
"""Syntax for declaring functions
    def     name_of_the_function    (parameter01,parameter02):
    keyword name of the function    contains parameters
"""

def cleanlist_2(dirty_list:list[str]) -> list[float]:
    """
    CHatGPt masking -> explanation about the function
    """
    
    # new empty list
    clean_list=[]

    for item in dirty_list:
        try:
            val = float(item) #type-casting
            clean_list.append(val)
        except:
            print (f"case case meka wada na -> {item}")
            continue

    return clean_list

# given list
list_2 = ["19.3","10.4","5.3","oops","12.7","14.2"]
list_x = ["dumindu",12,['p','o']]

print(cleanlist_2(list_2))



# # create a function
# def function_cleanlist():
#     # new empty list
#     clean_list=[]

#     for item in list_2:
#         try:
#             val = float(item) #type-casting
#             clean_list.append(val)
#         except:
#             print (f"case case meka wada na -> {item}")
#             continue

#     return clean_list