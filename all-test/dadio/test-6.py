def zebulansNightmare(functionName):
    arr_fun=list(functionName)
    err_arr = []

    for (i, item) in zip(range(len(arr_fun)), [_item for _item in functionName]):
        if item == '_':
            err_arr.append(i+1)
    for item in err_arr:
        arr_fun[item]=str.upper(arr_fun[item])
    return (''.join(arr_fun).replace('_',''))

print(zebulansNightmare('mark_as_issue'))


