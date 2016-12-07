#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def universalNameToID(name):
    if name == "IOA" or name == "Islands of Adventure":
        return 10000
    elif name == "USF" or name == "Universal Studios Florida":
        return 10010
    elif name == "USH" or name == "Universal Studios Hollywood":
        return 13825
    else:
        return -1

def USJTranslate(name):
    if name == "ハローキティのカップケーキ・ドリーム":
        return "Hello Kitty's Cupcake Dream"
    elif name == "エルモのゴーゴー・スケートボード":
        return "Elmo's go-go skateboard"
    elif name == "モッピーのバルーン・トリップ":
        return "Mobi Balloon Trip"
    elif name == "フライング・スヌーピー":
        return "Flying Snoopy"
    elif name == "スヌーピーのグレートレース™":
        return "Snoopy's Great Race ™"
    elif name == "アメージング・アドベンチャー・オブ・スパイダーマン・ザ・ライド 4K3D":
        return "Amazing Adventure of Spider-Man The Ride 4K 3 D"
    else:
        return "No translation"