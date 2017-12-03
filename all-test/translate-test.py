from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn'])

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-cn')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
print('---')
# The quick brown fox  ->  빠른 갈색 여우
# jumps over  ->  이상 점프
# the lazy dog  ->  게으른 개