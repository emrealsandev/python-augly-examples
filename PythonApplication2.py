import augly.text as textaugs


exampleText = "Beykent Universitesi Ogrencisi Emre Alsan AugLy'i begendi"
print(exampleText)
## yazým hatasý ekleme
print(textaugs.simulate_typos(exampleText))
## yazý fontu deðiþtirme
print(textaugs.replace_fun_fonts(exampleText,aug_p=0.3,aug_min=1,aug_max=10000,granularity='all',vary_fonts=True,n=2,priority_words=None,fonts_path='C:/Users/emrea/Desktop/emre/PythonAuglyExamples/PythonApplication6/webfonts/webfonts.json'))
print(exampleText)
## harf aralarýna noktalama iþareti ekleme
print(textaugs.insert_punctuation_chars(exampleText))
print(exampleText)
## Yazýyý 2 yönlü ters çevirme
print(textaugs.replace_bidirectional(exampleText))
print(exampleText)
## Yazýdaki benzer harfleri rakamlarla deðiþtirme
print(textaugs.replace_similar_chars(exampleText))
print(exampleText)