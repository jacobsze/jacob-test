import csv
from pprint import pprint
from datetime import datetime

now = datetime.now()

rawdata = csv.DictReader(open('slamdunk.csv','rU'))
status = {
	'Done': {'class':'done','color':'#8ec685'},
	'In Progress': {'class':'inprogress','color':'#f9d663'},
	'Prioritized': {'class':'prioritized','color':'#c6c6c6'}
}

swimlanes = {
	'Growth': 'swimlane1',
	'Partnerships': 'swimlane2',
	'Other': 'swimlane3',
	'Pebbles': 'swimlane4'
}

data = {'swimlane1': {},'swimlane2': {},'swimlane3': {},'swimlane4': {}}
temp_jquery = ''
temp_sl1 = ''
temp_sl2 = ''
temp_sl3 = ''
temp_sl4 = ''
q1_min = 1
q1_max = 1
q2_min = 2
q2_max = 2
q3_min = 3
q3_max = 3
q4_min = 4
q4_max = 4

for i in rawdata:
	swimlane = swimlanes[str(i['swimlane'])]
	id = str(i['id'])
	if id not in data[swimlane]:
		data[swimlane][id] = {
			'analysis': str(i['analysis'])
			, 'analysis_url': str(i['analysis_url'])
			, 'business_case': str(i['business_case'])
			, 'description': str(i['description'])
			, 'icon': str(i['icon'])
			, 'position': int(i['position'])
			, 'quarter': str(i['quarter'])
			, 'status': str(i['status'])
			, 'title': str(i['title'])
			, 'wb1': str(i['wb1'])
			, 'wb2': str(i['wb2'])
			, 'wb3': str(i['wb3'])
			, 'wb4': str(i['wb4'])
			, 'wb5': str(i['wb5'])
			, 'wb6': str(i['wb6'])
			, 'what_success': str(i['what_success'])
			, 'class': status[str(i['status'])]['class']
			, 'color': status[str(i['status'])]['color']
			}

for j in data: # j = swimlane1
	for k in data[j]: # k = 3
		analysis = data[j][k]['analysis']
		if len(data[j][k]['analysis_url']) > 0:
			analysis_url = "<a href='%s'>Link</a>" % 	data[j][k]['analysis_url']
		else:
			analysis_url = ''
		
		business_case = data[j][k]['business_case']
		description = data[j][k]['description']
		icon = data[j][k]['icon']
		position = data[j][k]['position']
		if j == 'swimlane4':
			position2 = (((position - 1) * 150) + (position * 20))
		else:
			position2 = (((position - 1) * 300) + (position * 10))
		quarter = data[j][k]['quarter']
		if j != "swimlane4":
			if quarter == '1':
				q1_min = min(q1_min,position)
				q1_max = max(q1_max,position)
				q2_min = max(q1_max + 1,q2_min)
				q2_max = max(q2_min,q2_max)
				q3_min = max(q2_max + 1,q3_min)
				q3_max = max(q3_min,q3_max)
				q4_min = max(q3_max + 1,q4_min)
				q4_max = max(q4_min,q4_max)
			elif quarter == '2':
				q2_min = min(q2_min,position)
				q2_max = max(q2_max,position)
				q3_min = max(q2_max + 1,q3_min)
				q3_max = max(q3_min,q3_max)
				q4_min = max(q3_max + 1,q4_min)
				q4_max = max(q4_min,q4_max)
			elif quarter == '3':
				q3_min = min(q3_min,position)
				q3_max = max(q3_max,position)
				q4_min = max(q3_max + 1,q4_min)
				q4_max = max(q4_min,q4_max)
			elif quarter == '4':
				q4_min = min(q4_min,position)
				q4_max = max(q4_max,position)
		status = data[j][k]['status']
		title = data[j][k]['title']
		wb1 = data[j][k]['wb1']
		wb2 = data[j][k]['wb2']
		wb3 = data[j][k]['wb3']
		wb4 = data[j][k]['wb4']
		wb5 = data[j][k]['wb5']
		wb6 = data[j][k]['wb6']
		what_success = data[j][k]['what_success']
		the_class = data[j][k]['class']
		color = data[j][k]['color']

		temp_jquery += """
		$( "#%s" ).css("left","%ipx");
		$( "#%s_click" ).data({"info1":"%s","info2":"%s","info2_color":"%s","info3":"%s","info4":"%s","info5":"%s","info6":"%s"});
		""" % (k,position2,k,title,status,color,business_case,what_success,analysis,analysis_url)

		if j == "swimlane1" and len(data[j]) > 0:
			temp_sl1 += """
				<div id="%s" class="box %s">
					<div id="%s_click" class="box_click"></div>
					<div class="icon_%s"></div>
					<div class="title">%s</div>
					<div class="description">%s</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>	
				</div>""" % (k,the_class,k,icon,title,description
			,'whitebox' if len(wb1) > 0 else 'emptybox',wb1
			,'whitebox' if len(wb2) > 0 else 'emptybox',wb2
			,'whitebox' if len(wb3) > 0 else 'emptybox',wb3
			,'whitebox' if len(wb4) > 0 else 'emptybox',wb4
			,'whitebox' if len(wb5) > 0 else 'emptybox',wb5
			,'whitebox' if len(wb6) > 0 else 'emptybox',wb6)

		if j == "swimlane2" and len(data[j]) > 0:
			temp_sl2 += """
				<div id="%s" class="box %s">
					<div id="%s_click" class="box_click"></div>
					<div class="icon_%s"></div>
					<div class="title">%s</div>
					<div class="description">%s</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>	
				</div>""" % (k,the_class,k,icon,title,description
			,'whitebox' if len(wb1) > 0 else 'emptybox',wb1
			,'whitebox' if len(wb2) > 0 else 'emptybox',wb2
			,'whitebox' if len(wb3) > 0 else 'emptybox',wb3
			,'whitebox' if len(wb4) > 0 else 'emptybox',wb4
			,'whitebox' if len(wb5) > 0 else 'emptybox',wb5
			,'whitebox' if len(wb6) > 0 else 'emptybox',wb6)

		if j == "swimlane3" and len(data[j]) > 0:
			temp_sl3 += """
				<div id="%s" class="box %s">
					<div id="%s_click" class="box_click"></div>
					<div class="icon_%s"></div>
					<div class="title">%s</div>
					<div class="description">%s</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>
					<div class="whiteboxes">
						<div class="%s">%s</div>
						<div class="%s">%s</div>
						<div class="%s">%s</div>
					</div>	
				</div>""" % (k,the_class,k,icon,title,description
			,'whitebox' if len(wb1) > 0 else 'emptybox',wb1
			,'whitebox' if len(wb2) > 0 else 'emptybox',wb2
			,'whitebox' if len(wb3) > 0 else 'emptybox',wb3
			,'whitebox' if len(wb4) > 0 else 'emptybox',wb4
			,'whitebox' if len(wb5) > 0 else 'emptybox',wb5
			,'whitebox' if len(wb6) > 0 else 'emptybox',wb6)

		if j == "swimlane4" and len(data[j]) > 0:
			temp_sl4 += """
				<div id="%s" class="box4 %s">
					<div id="%s_click" class="box4_click"></div>
					<div class="icon_%s"></div>
					<div class="title4">%s</div>
					<div class="description4">%s</div>
				</div>""" % (k,the_class,k,icon,title,description)

q1_width = (((q1_max - q1_min + 1) * 300) + ((q1_max - q1_min) * 10))
q2_left = q1_width #+ 10
q2_width = (((q2_max - q2_min + 1) * 300) + ((q2_max - q2_min) * 10))
q3_left = q2_left + q2_width #+ 10
q3_width = (((q3_max - q3_min + 1) * 300) + ((q3_max - q3_min) * 10))
q4_left = q3_left + q3_width #+ 10
q4_width = (((q4_max - q4_min + 1) * 300) + ((q4_max - q4_min) * 10)) + 50
sl_width = q4_left + q4_width + 360

html_str = """<html>
<head>
	<title>Slam Dunk Roadmap</title>
	<link rel="icon" href="https://raw.githubusercontent.com/jacobsze/jacob-test/master/favicon.ico" type="image/x-icon"/>
	<link rel="stylesheet" type="text/css" href="https://rawgit.com/jacobsze/jacob-test/master/slamdunk.css">
</head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>

<script>
$( document ).ready(function() {
	"""

html_str += temp_jquery

html_str += """
		$( ".box_click, .box4_click" ).on("click", function(e) {
			$( ".infopanel" ).css("display","inline")
			var idclicked = e.target.id;
			info1 = $( "#" + idclicked ).data("info1");
			info2 = $( "#" + idclicked ).data("info2");
			info2_color = $( "#" + idclicked ).data("info2_color");
			info3 = $( "#" + idclicked ).data("info3");
			info4 = $( "#" + idclicked ).data("info4");
			info5 = $( "#" + idclicked ).data("info5");
			info6 = $( "#" + idclicked ).data("info6");
			$( "#info1" ).html(info1);
			$( "#info2" ).html(info2);
			$( "#info2" ).css("background-color",info2_color);
			$( "#info3" ).html(info3);
			$( "#info4" ).html(info4);
			$( "#info5" ).html(info5);
			$( "#info6" ).html(info6);
		});
		
		$(document).click(function (event) {            
   			if(!$(event.target).closest( '.box_click, .box4_click, .infopanel').length) {
   				if($('.infopanel').is(":visible")) {
            		$('.infopanel').hide();
        		}
   			}
		});

		$( ".q1" ).css({"width":"%ipx","left":"5px"});
		$( ".q2" ).css({"width":"%ipx","left":"%ipx"});
		$( ".q3" ).css({"width":"%ipx","left":"%ipx"});
		$( ".q4" ).css({"width":"%ipx","left":"%ipx"});
		$( ".swimlane1" ).css("width","%ipx");
		$( ".swimlane2" ).css("width","%ipx");
		$( ".swimlane3" ).css("width","%ipx");
		$( ".swimlane4" ).css("width","%ipx");

	});
</script>
<body>
	<div class="leftbar">
		<div style="height:45px;font-size:70%%;">Last Update:<br>%s<br>%s EST</div>
		<div class="categories">Growth<p style="font-size:75%%;font-weight:normal;">Improve New User payback period thru CPA improvements</p></div>
		<div class="categories">Partnership Revenue<p style="font-size:75%%;font-weight:normal;">Generate Revenue by enabling Sponsorships and 3rd party branding</p></div>
		<div class="categories">Other Revenue<p style="font-size:75%%;font-weight:normal;">Generate Revenue by better monetizing our users</p></div>
		<div class="categories4">Pebbles</div>
	</div>
	<div class="timeline">
		<div class="quarter q1">Quarter 1</div>
		<div class="quarter q2">Quarter 2</div>
		<div class="quarter q3">Short Term Priorities</div>
		<div class="quarter q4">Future Items</div>
	</div>
	<div class="swimlane1" id="growth">
	""" % (q1_width,q2_width,q2_left,q3_width,q3_left,q4_width,q4_left,sl_width,sl_width,sl_width,sl_width,now.strftime("%b %d, %Y"),now.strftime("%I:%M%p"))

html_str += temp_sl1

html_str += """
</div>	
<div class="swimlane2" id="partnership">
"""

html_str += temp_sl2

html_str += """
</div>
<div class="swimlane3" id="other">"""

html_str += temp_sl3

html_str += """
</div>
<div class="swimlane4" id="pebbles">"""

html_str += temp_sl4

html_str += """
	</div>	
	<div class="infopanel">
		<div class="info1" id="info1">Title</div>
		<div class="info2" id="info2"></div>
		<div class="info_title">Business Case</div>
		<div class="info3" id="info3"></div>
		<div class="info_title">What does success look like?</div>
		<div class="info3" id="info4"></div>
		<div class="info_title">Analysis</div>
		<div class="info3" id="info5"></div>
		<div class="info3" id="info6"></div>
	</div>

</body>
</html>
"""

html_file = open('slamdunk.html','wb')
html_file.write(html_str)
html_file.close()


