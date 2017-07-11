import csv
from yandex_translate import YandexTranslate #make sure this is imported
# this is your api key
translate = YandexTranslate('<YandexAPIKey>')
print('Languages:', translate.langs)

# read your csv, single col to be translated
with open('file.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print('Detect language:', translate.detect(your_list))
# detects the current language
trans= translate.detect(your_list)
print(trans)
print(len(your_list))
print(your_list[1])


# loop over your list, translate from detected language to english.
counter = 0
while counter < len(your_list):
    lang = translate.detect(your_list[counter]),
    print('Translate:', translate.translate(your_list[counter], '%s-en' %lang))
    counter = counter+1
