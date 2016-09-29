import keyword
kwlist = keyword.kwlist
for kw in kwlist[:]:
    if len(kw) < 8:
        kwlist.remove(kw)
print(kwlist)
