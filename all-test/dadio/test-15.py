
# 提取文件名

import re


class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        # re_ip_rule = (r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        re_rule = r'(\d)+(_)+'
        re_rule_1 = r'(\.)(\w)+'
        re_rule_2 = r'(_)(\w)+(\.)'
        # print(dirty_file_name)
        # print(re.search(re_rule, dirty_file_name).group())

        out_str_1=re.search(re_rule_1, dirty_file_name).group()
        out_str_2=re.search(re_rule_2, dirty_file_name).group()
        # print(out_str_1)
        # print(out_str_2)
        # print('------')
        return out_str_2[1:-1]+out_str_1




FileNameExtractor.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")  # ,"FILE_NAME.EXTENSION")
FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34")