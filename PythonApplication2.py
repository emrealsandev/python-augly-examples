import augly.text as textaugs


exampleText = "Beykent Universitesi Ogrencisi Emre Alsan AugLy'i begendi"
print(exampleText)
## yaz�m hatas� ekleme
print(textaugs.simulate_typos(exampleText))
## yaz� fontu de�i�tirme
print(textaugs.replace_fun_fonts(exampleText,aug_p=0.3,aug_min=1,aug_max=10000,granularity='all',vary_fonts=True,n=2,priority_words=None,fonts_path='C:/Users/emrea/Desktop/emre/PythonAuglyExamples/PythonApplication6/webfonts/webfonts.json'))
print(exampleText)
## harf aralar�na noktalama i�areti ekleme
print(textaugs.insert_punctuation_chars(exampleText))
print(exampleText)
## Yaz�y� 2 y�nl� ters �evirme
print(textaugs.replace_bidirectional(exampleText))
print(exampleText)
## Yaz�daki benzer harfleri rakamlarla de�i�tirme
print(textaugs.replace_similar_chars(exampleText))
print(exampleText)