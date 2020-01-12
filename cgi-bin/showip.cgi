#!/bin/bash

/bin/cat << EOM

<html>
<head>
        <meta charset="utf-8">
	<meta http-equiv="refresh" content="15; URL=/display.html">
	<title>IP < BauchbindenViewer</title>
	<script src="jquery-1.5.1.min.js"></script>

	<style type="text/css">

	body { 
		background: #000; 
		font-family: 'DIN-Bold', sans-serif;
		color: #FFFFFF;
	}
	#name {
		position: absolute;
		top: 300px;
		font-size: 64px;
		margin-left: 100px;
	}
	#title {
		font-family: 'DIN-Medium', sans-serif;
		position: absolute;
		top: 450px;
		font-size: 36px;
		margin-left: 100px;
	}
	</style>
</head>
<body>
	<div id="name">
EOM

ifconfeth=$(ifconfig eth0 | head -n2 | tail -n1 | awk 'BEGIN{FS=" "}{print $2}')
ifconfwlan=$(ifconfig wlan0 | head -n2 | tail -n1 | awk 'BEGIN{FS=" "}{print $2}')
#echo $SERVER_ADDR
echo "eth0" $ifconfeth
echo "<br/>"
echo "wlan0" $ifconfwlan

/bin/cat << EOM
	</div>
	<div id="title">
	BauchbindenEditor: /cgi-bin/edit.cgi
	</div>
</body>
</html>

EOM
