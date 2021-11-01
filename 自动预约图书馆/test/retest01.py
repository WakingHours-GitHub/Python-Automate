import re


txt = '{"id":6091,"no":"011","name":"011","area":30,"category":12,"point_x":19.58333,"point_x2":null,"point_x3":null,"point_x4":null,"point_y":22.40741,"point_y2":null,"point_y3":null,"point_y4":null,"width":2.1875,"height":3.981482,"status":1,"status_name":"空闲","area_name":"北侧自习区A","area_levels":1,"area_type":1,"area_color":null}'

print(re.search(r'"status_name":"(?P<state>.*?)"', txt).group("state"))
# "status_name":"空闲"
# <li class="seat using-icon" style="background-size:751px;background-position:-79px -144px;left:79px;top:144px;width:16px;height:16px;" data-no="6145" data-data="{&quot;id&quot;:6145,&quot;no&quot;:&quot;065&quot;,&quot;name&quot;:&quot;065&quot;,&quot;area&quot;:30,&quot;category&quot;:12,&quot;point_x&quot;:10.52083,&quot;point_x2&quot;:null,&quot;point_x3&quot;:null,&quot;point_x4&quot;:null,&quot;point_y&quot;:34.07407,&quot;point_y2&quot;:null,&quot;point_y3&quot;:null,&quot;point_y4&quot;:null,&quot;width&quot;:2.083333,&quot;height&quot;:3.888889,&quot;status&quot;:6,&quot;status_name&quot;:&quot;使用中&quot;,&quot;area_name&quot;:&quot;北侧自习区A&quot;,&quot;area_levels&quot;:1,&quot;area_type&quot;:1,&quot;area_color&quot;:null}"></li>

txt = '<li class="seat using-icon" style="background-size:751px;background-position:-79px -144px;left:79px;top:144px;width:16px;height:16px;" data-no="6145" data-data="{&quot;id&quot;:6145,&quot;no&quot;:&quot;065&quot;,&quot;name&quot;:&quot;065&quot;,&quot;area&quot;:30,&quot;category&quot;:12,&quot;point_x&quot;:10.52083,&quot;point_x2&quot;:null,&quot;point_x3&quot;:null,&quot;point_x4&quot;:null,&quot;point_y&quot;:34.07407,&quot;point_y2&quot;:null,&quot;point_y3&quot;:null,&quot;point_y4&quot;:null,&quot;width&quot;:2.083333,&quot;height&quot;:3.888889,&quot;status&quot;:6,' \
      '&quot;status_name&quot;:&quot;使用中&quot;' \
      ',&quot;area_name&quot;:&quot;北侧自习区A&quot;,&quot;area_levels&quot;:1,&quot;area_type&quot;:1,&quot;area_color&quot;:null}"></li>'
txt = str(txt)
print(re.search(r"&quot;status_name&quot;:&quot;(?P<state>.*?)&quot;", txt).group("state"))