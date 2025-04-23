# arr = [80, 90, 120, 40, 30, 20]
# sort_num = []


# for i in range(len(arr)):
#     higest = arr[0]
#     for e in arr:
#         if e > higest:
#             higest = e
#     sort_num.append(higest)
#     arr.remove(higest)

# print(sort_num)


# arr = ["gjsgs", "njsagnjsngjs", "jasgjs", "sgs", "sgnjksg", "sjgkskgskg"]
# sort_num = []


# for i in range(len(arr)):
#     higest = arr[0]
#     for e in arr:
#         if len(e) > len(higest):
#             higest = e
#     sort_num.append(higest)
#     arr.remove(higest)

# print(sort_num)

arr = [80, 20, 90, 70, 8, 10, 26, 5]
sorted_arr = []
if len(arr) > 0:
    for i in range(len(arr)):
        highest_value = arr[0]
        lowest_value = arr[0]
        for e in arr:
            if e > highest_value:
                highest_value = e
            if e < lowest_value:
                lowest_value = e
        print(highest_value, lowest_value)

        sorted_arr.append(highest_value)
        arr.remove(highest_value)
        sorted_arr.append(lowest_value)


print(sorted_arr)
