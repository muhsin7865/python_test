def ffindstring(fname, s):
    with open(fname, "r") as F:
        for line in F.readlines():
            if s in line:
                return True
            return s
print(ffindstring('requirements.txt', '6\nz'))


# class NotAvailable(Exception):
#     pass

# def breakdown(amt, denominations):
#     deno = denominations.copy()
#     res_dict = {}
#     for i in denominations:
#         if amt >= i:
#             if denominations[i]>0:
#                 denominations[i]-=(amt//i)
#                 res_dict[i] = amt//i
#                 amt-=i*(amt//i)
#     if(amt!=0):
#         raise NotAvailable(deno)
#     else:
#         return res_dict
   
# print(breakdown(750, {1000: 2, 500:4}))