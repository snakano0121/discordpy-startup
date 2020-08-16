# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:57:20 2020

@author: User
"""

import requests

def makeID():
    CODE = """
<pref title="道北">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/01a.xml"/>
<city title="稚内" id="011000" source="http://weather.livedoor.com/forecast/rss/area/011000.xml"/>
<city title="旭川" id="012010" source="http://weather.livedoor.com/forecast/rss/area/012010.xml"/>
<city title="留萌" id="012020" source="http://weather.livedoor.com/forecast/rss/area/012020.xml"/>
</pref>
<pref title="道東">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/01c.xml"/>
<city title="網走" id="013010" source="http://weather.livedoor.com/forecast/rss/area/013010.xml"/>
<city title="北見" id="013020" source="http://weather.livedoor.com/forecast/rss/area/013020.xml"/>
<city title="紋別" id="013030" source="http://weather.livedoor.com/forecast/rss/area/013030.xml"/>
<city title="根室" id="014010" source="http://weather.livedoor.com/forecast/rss/area/014010.xml"/>
<city title="釧路" id="014020" source="http://weather.livedoor.com/forecast/rss/area/014020.xml"/>
<city title="帯広" id="014030" source="http://weather.livedoor.com/forecast/rss/area/014030.xml"/>
</pref>
<pref title="道南">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/01d.xml"/>
<city title="室蘭" id="015010" source="http://weather.livedoor.com/forecast/rss/area/015010.xml"/>
<city title="浦河" id="015020" source="http://weather.livedoor.com/forecast/rss/area/015020.xml"/>
<city title="函館" id="017010" source="http://weather.livedoor.com/forecast/rss/area/017010.xml"/>
<city title="江差" id="017020" source="http://weather.livedoor.com/forecast/rss/area/017020.xml"/>
</pref>
<pref title="道央">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/01b.xml"/>
<city title="札幌" id="016010" source="http://weather.livedoor.com/forecast/rss/area/016010.xml"/>
<city title="岩見沢" id="016020" source="http://weather.livedoor.com/forecast/rss/area/016020.xml"/>
<city title="倶知安" id="016030" source="http://weather.livedoor.com/forecast/rss/area/016030.xml"/>
</pref>
<pref title="青森県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/02.xml"/>
<city title="青森" id="020010" source="http://weather.livedoor.com/forecast/rss/area/020010.xml"/>
<city title="むつ" id="020020" source="http://weather.livedoor.com/forecast/rss/area/020020.xml"/>
<city title="八戸" id="020030" source="http://weather.livedoor.com/forecast/rss/area/020030.xml"/>
</pref>
<pref title="岩手県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/03.xml"/>
<city title="盛岡" id="030010" source="http://weather.livedoor.com/forecast/rss/area/030010.xml"/>
<city title="宮古" id="030020" source="http://weather.livedoor.com/forecast/rss/area/030020.xml"/>
<city title="大船渡" id="030030" source="http://weather.livedoor.com/forecast/rss/area/030030.xml"/>
</pref>
<pref title="宮城県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/04.xml"/>
<city title="仙台" id="040010" source="http://weather.livedoor.com/forecast/rss/area/040010.xml"/>
<city title="白石" id="040020" source="http://weather.livedoor.com/forecast/rss/area/040020.xml"/>
</pref>
<pref title="秋田県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/05.xml"/>
<city title="秋田" id="050010" source="http://weather.livedoor.com/forecast/rss/area/050010.xml"/>
<city title="横手" id="050020" source="http://weather.livedoor.com/forecast/rss/area/050020.xml"/>
</pref>
<pref title="山形県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/06.xml"/>
<city title="山形" id="060010" source="http://weather.livedoor.com/forecast/rss/area/060010.xml"/>
<city title="米沢" id="060020" source="http://weather.livedoor.com/forecast/rss/area/060020.xml"/>
<city title="酒田" id="060030" source="http://weather.livedoor.com/forecast/rss/area/060030.xml"/>
<city title="新庄" id="060040" source="http://weather.livedoor.com/forecast/rss/area/060040.xml"/>
</pref>
<pref title="福島県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/07.xml"/>
<city title="福島" id="070010" source="http://weather.livedoor.com/forecast/rss/area/070010.xml"/>
<city title="小名浜" id="070020" source="http://weather.livedoor.com/forecast/rss/area/070020.xml"/>
<city title="若松" id="070030" source="http://weather.livedoor.com/forecast/rss/area/070030.xml"/>
</pref>
<pref title="茨城県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/08.xml"/>
<city title="水戸" id="080010" source="http://weather.livedoor.com/forecast/rss/area/080010.xml"/>
<city title="土浦" id="080020" source="http://weather.livedoor.com/forecast/rss/area/080020.xml"/>
</pref>
<pref title="栃木県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/09.xml"/>
<city title="宇都宮" id="090010" source="http://weather.livedoor.com/forecast/rss/area/090010.xml"/>
<city title="大田原" id="090020" source="http://weather.livedoor.com/forecast/rss/area/090020.xml"/>
</pref>
<pref title="群馬県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/10.xml"/>
<city title="前橋" id="100010" source="http://weather.livedoor.com/forecast/rss/area/100010.xml"/>
<city title="みなかみ" id="100020" source="http://weather.livedoor.com/forecast/rss/area/100020.xml"/>
</pref>
<pref title="埼玉県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/11.xml"/>
<city title="さいたま" id="110010" source="http://weather.livedoor.com/forecast/rss/area/110010.xml"/>
<city title="熊谷" id="110020" source="http://weather.livedoor.com/forecast/rss/area/110020.xml"/>
<city title="秩父" id="110030" source="http://weather.livedoor.com/forecast/rss/area/110030.xml"/>
</pref>
<pref title="千葉県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/12.xml"/>
<city title="千葉" id="120010" source="http://weather.livedoor.com/forecast/rss/area/120010.xml"/>
<city title="銚子" id="120020" source="http://weather.livedoor.com/forecast/rss/area/120020.xml"/>
<city title="館山" id="120030" source="http://weather.livedoor.com/forecast/rss/area/120030.xml"/>
</pref>
<pref title="東京都">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/13.xml"/>
<city title="東京" id="130010" source="http://weather.livedoor.com/forecast/rss/area/130010.xml"/>
<city title="大島" id="130020" source="http://weather.livedoor.com/forecast/rss/area/130020.xml"/>
<city title="八丈島" id="130030" source="http://weather.livedoor.com/forecast/rss/area/130030.xml"/>
<city title="父島" id="130040" source="http://weather.livedoor.com/forecast/rss/area/130040.xml"/>
</pref>
<pref title="神奈川県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/14.xml"/>
<city title="横浜" id="140010" source="http://weather.livedoor.com/forecast/rss/area/140010.xml"/>
<city title="小田原" id="140020" source="http://weather.livedoor.com/forecast/rss/area/140020.xml"/>
</pref>
<pref title="新潟県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/15.xml"/>
<city title="新潟" id="150010" source="http://weather.livedoor.com/forecast/rss/area/150010.xml"/>
<city title="長岡" id="150020" source="http://weather.livedoor.com/forecast/rss/area/150020.xml"/>
<city title="高田" id="150030" source="http://weather.livedoor.com/forecast/rss/area/150030.xml"/>
<city title="相川" id="150040" source="http://weather.livedoor.com/forecast/rss/area/150040.xml"/>
</pref>
<pref title="富山県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/16.xml"/>
<city title="富山" id="160010" source="http://weather.livedoor.com/forecast/rss/area/160010.xml"/>
<city title="伏木" id="160020" source="http://weather.livedoor.com/forecast/rss/area/160020.xml"/>
</pref>
<pref title="石川県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/17.xml"/>
<city title="金沢" id="170010" source="http://weather.livedoor.com/forecast/rss/area/170010.xml"/>
<city title="輪島" id="170020" source="http://weather.livedoor.com/forecast/rss/area/170020.xml"/>
</pref>
<pref title="福井県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/18.xml"/>
<city title="福井" id="180010" source="http://weather.livedoor.com/forecast/rss/area/180010.xml"/>
<city title="敦賀" id="180020" source="http://weather.livedoor.com/forecast/rss/area/180020.xml"/>
</pref>
<pref title="山梨県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/19.xml"/>
<city title="甲府" id="190010" source="http://weather.livedoor.com/forecast/rss/area/190010.xml"/>
<city title="河口湖" id="190020" source="http://weather.livedoor.com/forecast/rss/area/190020.xml"/>
</pref>
<pref title="長野県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/20.xml"/>
<city title="長野" id="200010" source="http://weather.livedoor.com/forecast/rss/area/200010.xml"/>
<city title="松本" id="200020" source="http://weather.livedoor.com/forecast/rss/area/200020.xml"/>
<city title="飯田" id="200030" source="http://weather.livedoor.com/forecast/rss/area/200030.xml"/>
</pref>
<pref title="岐阜県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/21.xml"/>
<city title="岐阜" id="210010" source="http://weather.livedoor.com/forecast/rss/area/210010.xml"/>
<city title="高山" id="210020" source="http://weather.livedoor.com/forecast/rss/area/210020.xml"/>
</pref>
<pref title="静岡県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/22.xml"/>
<city title="静岡" id="220010" source="http://weather.livedoor.com/forecast/rss/area/220010.xml"/>
<city title="網代" id="220020" source="http://weather.livedoor.com/forecast/rss/area/220020.xml"/>
<city title="三島" id="220030" source="http://weather.livedoor.com/forecast/rss/area/220030.xml"/>
<city title="浜松" id="220040" source="http://weather.livedoor.com/forecast/rss/area/220040.xml"/>
</pref>
<pref title="愛知県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/23.xml"/>
<city title="名古屋" id="230010" source="http://weather.livedoor.com/forecast/rss/area/230010.xml"/>
<city title="豊橋" id="230020" source="http://weather.livedoor.com/forecast/rss/area/230020.xml"/>
</pref>
<pref title="三重県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/24.xml"/>
<city title="津" id="240010" source="http://weather.livedoor.com/forecast/rss/area/240010.xml"/>
<city title="尾鷲" id="240020" source="http://weather.livedoor.com/forecast/rss/area/240020.xml"/>
</pref>
<pref title="滋賀県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/25.xml"/>
<city title="大津" id="250010" source="http://weather.livedoor.com/forecast/rss/area/250010.xml"/>
<city title="彦根" id="250020" source="http://weather.livedoor.com/forecast/rss/area/250020.xml"/>
</pref>
<pref title="京都府">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/26.xml"/>
<city title="京都" id="260010" source="http://weather.livedoor.com/forecast/rss/area/260010.xml"/>
<city title="舞鶴" id="260020" source="http://weather.livedoor.com/forecast/rss/area/260020.xml"/>
</pref>
<pref title="大阪府">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/27.xml"/>
<city title="大阪" id="270000" source="http://weather.livedoor.com/forecast/rss/area/270000.xml"/>
</pref>
<pref title="兵庫県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/28.xml"/>
<city title="神戸" id="280010" source="http://weather.livedoor.com/forecast/rss/area/280010.xml"/>
<city title="豊岡" id="280020" source="http://weather.livedoor.com/forecast/rss/area/280020.xml"/>
</pref>
<pref title="奈良県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/29.xml"/>
<city title="奈良" id="290010" source="http://weather.livedoor.com/forecast/rss/area/290010.xml"/>
<city title="風屋" id="290020" source="http://weather.livedoor.com/forecast/rss/area/290020.xml"/>
</pref>
<pref title="和歌山県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/30.xml"/>
<city title="和歌山" id="300010" source="http://weather.livedoor.com/forecast/rss/area/300010.xml"/>
<city title="潮岬" id="300020" source="http://weather.livedoor.com/forecast/rss/area/300020.xml"/>
</pref>
<pref title="鳥取県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/31.xml"/>
<city title="鳥取" id="310010" source="http://weather.livedoor.com/forecast/rss/area/310010.xml"/>
<city title="米子" id="310020" source="http://weather.livedoor.com/forecast/rss/area/310020.xml"/>
</pref>
<pref title="島根県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/32.xml"/>
<city title="松江" id="320010" source="http://weather.livedoor.com/forecast/rss/area/320010.xml"/>
<city title="浜田" id="320020" source="http://weather.livedoor.com/forecast/rss/area/320020.xml"/>
<city title="西郷" id="320030" source="http://weather.livedoor.com/forecast/rss/area/320030.xml"/>
</pref>
<pref title="岡山県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/33.xml"/>
<city title="岡山" id="330010" source="http://weather.livedoor.com/forecast/rss/area/330010.xml"/>
<city title="津山" id="330020" source="http://weather.livedoor.com/forecast/rss/area/330020.xml"/>
</pref>
<pref title="広島県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/34.xml"/>
<city title="広島" id="340010" source="http://weather.livedoor.com/forecast/rss/area/340010.xml"/>
<city title="庄原" id="340020" source="http://weather.livedoor.com/forecast/rss/area/340020.xml"/>
</pref>
<pref title="山口県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/35.xml"/>
<city title="下関" id="350010" source="http://weather.livedoor.com/forecast/rss/area/350010.xml"/>
<city title="山口" id="350020" source="http://weather.livedoor.com/forecast/rss/area/350020.xml"/>
<city title="柳井" id="350030" source="http://weather.livedoor.com/forecast/rss/area/350030.xml"/>
<city title="萩" id="350040" source="http://weather.livedoor.com/forecast/rss/area/350040.xml"/>
</pref>
<pref title="徳島県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/36.xml"/>
<city title="徳島" id="360010" source="http://weather.livedoor.com/forecast/rss/area/360010.xml"/>
<city title="日和佐" id="360020" source="http://weather.livedoor.com/forecast/rss/area/360020.xml"/>
</pref>
<pref title="香川県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/37.xml"/>
<city title="高松" id="370000" source="http://weather.livedoor.com/forecast/rss/area/370000.xml"/>
</pref>
<pref title="愛媛県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/38.xml"/>
<city title="松山" id="380010" source="http://weather.livedoor.com/forecast/rss/area/380010.xml"/>
<city title="新居浜" id="380020" source="http://weather.livedoor.com/forecast/rss/area/380020.xml"/>
<city title="宇和島" id="380030" source="http://weather.livedoor.com/forecast/rss/area/380030.xml"/>
</pref>
<pref title="高知県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/39.xml"/>
<city title="高知" id="390010" source="http://weather.livedoor.com/forecast/rss/area/390010.xml"/>
<city title="室戸岬" id="390020" source="http://weather.livedoor.com/forecast/rss/area/390020.xml"/>
<city title="清水" id="390030" source="http://weather.livedoor.com/forecast/rss/area/390030.xml"/>
</pref>
<pref title="福岡県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/40.xml"/>
<city title="福岡" id="400010" source="http://weather.livedoor.com/forecast/rss/area/400010.xml"/>
<city title="八幡" id="400020" source="http://weather.livedoor.com/forecast/rss/area/400020.xml"/>
<city title="飯塚" id="400030" source="http://weather.livedoor.com/forecast/rss/area/400030.xml"/>
<city title="久留米" id="400040" source="http://weather.livedoor.com/forecast/rss/area/400040.xml"/>
</pref>
<pref title="佐賀県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/41.xml"/>
<city title="佐賀" id="410010" source="http://weather.livedoor.com/forecast/rss/area/410010.xml"/>
<city title="伊万里" id="410020" source="http://weather.livedoor.com/forecast/rss/area/410020.xml"/>
</pref>
<pref title="長崎県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/42.xml"/>
<city title="長崎" id="420010" source="http://weather.livedoor.com/forecast/rss/area/420010.xml"/>
<city title="佐世保" id="420020" source="http://weather.livedoor.com/forecast/rss/area/420020.xml"/>
<city title="厳原" id="420030" source="http://weather.livedoor.com/forecast/rss/area/420030.xml"/>
<city title="福江" id="420040" source="http://weather.livedoor.com/forecast/rss/area/420040.xml"/>
</pref>
<pref title="熊本県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/43.xml"/>
<city title="熊本" id="430010" source="http://weather.livedoor.com/forecast/rss/area/430010.xml"/>
<city title="阿蘇乙姫" id="430020" source="http://weather.livedoor.com/forecast/rss/area/430020.xml"/>
<city title="牛深" id="430030" source="http://weather.livedoor.com/forecast/rss/area/430030.xml"/>
<city title="人吉" id="430040" source="http://weather.livedoor.com/forecast/rss/area/430040.xml"/>
</pref>
<pref title="大分県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/44.xml"/>
<city title="大分" id="440010" source="http://weather.livedoor.com/forecast/rss/area/440010.xml"/>
<city title="中津" id="440020" source="http://weather.livedoor.com/forecast/rss/area/440020.xml"/>
<city title="日田" id="440030" source="http://weather.livedoor.com/forecast/rss/area/440030.xml"/>
<city title="佐伯" id="440040" source="http://weather.livedoor.com/forecast/rss/area/440040.xml"/>
</pref>
<pref title="宮崎県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/45.xml"/>
<city title="宮崎" id="450010" source="http://weather.livedoor.com/forecast/rss/area/450010.xml"/>
<city title="延岡" id="450020" source="http://weather.livedoor.com/forecast/rss/area/450020.xml"/>
<city title="都城" id="450030" source="http://weather.livedoor.com/forecast/rss/area/450030.xml"/>
<city title="高千穂" id="450040" source="http://weather.livedoor.com/forecast/rss/area/450040.xml"/>
</pref>
<pref title="鹿児島県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/46.xml"/>
<city title="鹿児島" id="460010" source="http://weather.livedoor.com/forecast/rss/area/460010.xml"/>
<city title="鹿屋" id="460020" source="http://weather.livedoor.com/forecast/rss/area/460020.xml"/>
<city title="種子島" id="460030" source="http://weather.livedoor.com/forecast/rss/area/460030.xml"/>
<city title="名瀬" id="460040" source="http://weather.livedoor.com/forecast/rss/area/460040.xml"/>
</pref>
<pref title="沖縄県">
<warn title="警報・注意報" source="http://weather.livedoor.com/forecast/rss/warn/47.xml"/>
<city title="那覇" id="471010" source="http://weather.livedoor.com/forecast/rss/area/471010.xml"/>
<city title="名護" id="471020" source="http://weather.livedoor.com/forecast/rss/area/471020.xml"/>
<city title="久米島" id="471030" source="http://weather.livedoor.com/forecast/rss/area/471030.xml"/>
<city title="南大東" id="472000" source="http://weather.livedoor.com/forecast/rss/area/472000.xml"/>
<city title="宮古島" id="473000" source="http://weather.livedoor.com/forecast/rss/area/473000.xml"/>
<city title="石垣島" id="474010" source="http://weather.livedoor.com/forecast/rss/area/474010.xml"/>
<city title="与那国島" id="474020" source="http://weather.livedoor.com/forecast/rss/area/474020.xml"/>
    """
    
    IDdic = {}
    Shichodic ={}
    
    
    li =CODE.split("</pref>")
    
    for Area in li:
        outlD = []
        outSHICHO = []

    
        Zone = Area.split("<pref title=")[-1].split('"')
#        print(Zone)
        count =0
        numID = 1
        numSHI = 1
        dickey = Zone[1]
        
        for i in Zone:
            count+=1
            
            
            outnum = 6*numSHI+2
            if count== outnum:
                outSHICHO.append(i)
                numSHI+=1
            else:
                pass            
            
            
            
            outnum = 6*numID+4
            if count== outnum:
                outlD.append(i)
                numID+=1
            else:
                pass
            
        IDdic[dickey] = outlD
        Shichodic[dickey] = outSHICHO


    return [IDdic,Shichodic]

def outWeather(ID):
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    payload = {"city":"%s"%ID}
    tenki_data = requests.get(url, params=payload).json()
    weatherinfo = tenki_data["description"]["text"]
    
    return weatherinfo

def analyzeWeather(message):
    IDlist = makeID()[0]
    SHIlist = makeID()[1]
    for KEN in list(IDlist.keys()):
        if KEN in message:
            shi_num = 0
            ID = IDlist[KEN][shi_num]
            NAME = SHIlist[KEN][shi_num]
            INFO = outWeather(ID)
            
            return INFO
        else:
            pass
    return 0

    
            


