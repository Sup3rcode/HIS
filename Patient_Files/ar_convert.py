buck2uni = {"'": u"\u0621", # hamza-on-the-line
            "a": u"\u0622", # madda
            ">": u"\u0623", # hamza-on-'alif
            "&": u"\u0624", # hamza-on-waaw
            "<": u"\u0625", # hamza-under-'alif
            "}": u"\u0626", # hamza-on-yaa'
            "a": u"\u0627", # bare 'alif
            "b": u"\u0628", # baa'
            "at": u"\u0629", # taa' marbuuTa
            "t": u"\u062A", # taa'
            "tha": u"\u062B", # thaa'
            "j": u"\u062C", # jiim
            "ha": u"\u062D", # Haa'
            "kh": u"\u062E", # khaa'
            "d": u"\u062F", # daal
            "th": u"\u0630", # dhaal
            "r": u"\u0631", # raa'
            "z": u"\u0632", # zaay
            "s": u"\u0633", # siin
            "sh": u"\u0634", # shiin
            "sa": u"\u0635", # Saad
            "da": u"\u0636", # Daad
            "dth": u"\u0637", # Taa'
            "tha": u"\u0638", # Zaa' (DHaa')
            "aa": u"\u0639" ,
            "ota": u"\u0639""\u062A", # cayn
            "ga": u"\u063A", # ghayn
            "_": u"\u0640", # taTwiil
            "f": u"\u0641", # faa'
            "q": u"\u0642", # qaaf
            "ka": u"\u0643", # kaaf
            "l": u"\u0644", # laam
            "m": u"\u0645", # miim
            "n": u"\u0646", # nuun
            "h": u"\u0647", # haa'
            "w": u"\u0648", # waaw
            "ea": u"\u0649", # 'alif maqSuura
            "y": u"\u064A", # yaa'
            "F": u"\u064B", # fatHatayn
            "N": u"\u064C", # Dammatayn
            "K": u"\u064D", # kasratayn
            "ٌ": u"\u064E", # fatHa
            "u": u"\u064F", # Damma
            "i": u"\u0650", # kasra
            "~": u"\u0651", # shaddah
            "o": u"\u0652", # sukuun
            "`": u"\u0670", # dagger 'alif
            "{": u"\u0671", # waSla
}

def transString(string, reverse=0):
    '''Given a Unicode string, transliterate into Buckwalter. To go from
    Buckwalter back to Unicode, set reverse=1'''

    for k, v in buck2uni.items():
      if not reverse:
            string = string.replace(v, k)
      else:
            string = string.replace(k, v)

    return string

print(transString(u'العتيبي'))

