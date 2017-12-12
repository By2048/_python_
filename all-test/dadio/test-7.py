# 公共子字符串

def substring_test(str1, str2):

    # str1=str.upper(str1)
    # str2=str.upper(str2)

    lstr1 = len(str1)
    lstr2 = len(str2)
    record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)]  # 多一位
    maxNum = 0          # 最长匹配长度
    p = 0               # 匹配的起始位

    # print(str1)
    # print(str2)

    for i in range(lstr1):
        for j in range(lstr2):
            if str1[i] == str2[j]:
                # 相同则累加
                record[i+1][j+1] = record[i][j] + 1
                if record[i+1][j+1] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i+1][j+1]
                    # 记录最大匹配长度的终止位置
                    p = i + 1
    # print(str1[p-maxNum:p])
    # print(maxNum)


    if maxNum>=2:
        return True
    else:
        return False


substring_test("Something", "Home")
substring_test("Something", "Fun")
substring_test("Something", "")
substring_test("", "Something")
print(substring_test("BANANA", "banana"))
substring_test("test", "lllt")
substring_test("", "")
substring_test("1234567", "541265")
print(substring_test(
    "LoremipsumdolorsitametconsecteturadipiscingelitAeneannonaliquetligulautplaceratorciSuspendissepotentiMorbivolutpatauctoripsumegetaliquamPhasellusidmagnaelitNullamerostellustemporquismolestieaornarevitaediamNullaaliquamrisusnonviverrasagittisInlaoreetultricespretiumVestibulumegetnullatinciduntsempersemacrutrumfelisPraesentpurusarcutempusnecvariusidultricesaduiPellentesqueultriciesjustolobortisrhoncusdignissimNuncviverraconsequatblanditUtbibendumatlacusactristiqueAliquamimperdietnuncsempertortorefficiturviverra",
    "thisisalongstringtest"))


