#!/bin/bash

# write url parameters zu variables

name=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

name1=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name1=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title1=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title1=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

name2=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name2=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title2=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title2=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

name3=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name3=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title3=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title3=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

name4=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name4=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title4=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title4=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

name5=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])name5=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g' )
title5=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])title5=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')

use=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])use=[^&]+" | cut -f 2 -d "=" | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e | sed 's/+/ /g')


# if preset given, set current variables to preset and save these to file

if [ "$use" = "1" ]
then
	name=$name1
	title=$title1
	echo $name > name.key
	echo $title > title.key
else
	nothing
fi
if [ "$use" = "2" ]
then
	name=$name2
	title=$title2
	echo $name > name.key
	echo $title > title.key
else
	nothing
fi
if [ "$use" = "3" ]
then
	name=$name3
	title=$title3
	echo $name > name.key
	echo $title > title.key
else
	nothing
fi
if [ "$use" = "4" ]
then
	name=$name4
	title=$title4
	echo $name > name.key
	echo $title > title.key
else
	nothing
fi
if [ "$use" = "5" ]
then
	name=$name5
	title=$title5
	echo $name > name.key
	echo $title > title.key
else
	nothing
fi


# write non-empty variables to files

if [ "$name" = "" ]
then
	nothing
else
	echo $name > name.key
fi

if [ "$title" = "" ]
then
	nothing
else
	echo $title > title.key
fi

if [ "$name1" = "" ]
then
	nothing
else
	echo $name1 > name1.key
fi

if [ "$title1" = "" ]
then
	nothing
else
	echo $title1 > title1.key
fi

if [ "$name2" = "" ]
then
	nothing
else
	echo $name2 > name2.key
fi

if [ "$title2" = "" ]
then
	nothing
else
	echo $title2 > title2.key
fi

if [ "$name3" = "" ]
then
	nothing
else
	echo $name3 > name3.key
fi

if [ "$title3" = "" ]
then
	nothing
else
	echo $title3 > title3.key
fi

if [ "$name4" = "" ]
then
	nothing
else
	echo $name4 > name4.key
fi

if [ "$title4" = "" ]
then
	nothing
else
	echo $title4 > title4.key
fi

if [ "$name5" = "" ]
then
	nothing
else
	echo $name5 > name5.key
fi

if [ "$title5" = "" ]
then
	nothing
else
	echo $title5 > title5.key
fi

echo "Content-type: text/html"
echo ""

# read files to display-variables

read namekey < name.key
read titlekey < title.key
read name1key < name1.key
read title1key < title1.key
read name2key < name2.key
read title2key < title2.key
read name3key < name3.key
read title3key < title3.key
read name4key < name4.key
read title4key < title4.key
read name5key < name5.key
read title5key < title5.key


/bin/cat << EOM
<!DOCTYPE html>
<html>
<head>
        <meta charset="utf-8">
	<title>Bauchbinden editor</title>
	<style>
	td.set {
		width: 80px;
		text-align: center;
	}
	td.descr {
		text-align: right;
	}
	tr.set {

	}
	h3 {
		margin-top: 5px;
		margin-bottom: 0px;
	}
	h4 {
		margin-top: 0px;
		margin-bottom: 0px;
	}
	input {
		margin-top: 0px;
		font-size:1.5em;
	}
	input.submit {
		font-size:1.2em;
		font-weight: bold;
		padding: 5px;
		margin-top: 10px;
	}
	hr {
		margin-top: 0px;
		margin-bottom: 0px;
		color: #aaa;
	}
	body {
		font-family: Ubuntu, sans-serif;
	}
	div.current {

		width: 50%;
		float: left;
	}
	div.current input {
		font-size: 2em;
	}
	div.current td.descr {
		padding-left: 2em;
	}

	div.presets {

		width: 50%;
		float: left;
	}
	</style>
</head>
<body>
	<form action="/cgi-bin/edit.cgi" method="get">
	<div class="current">
EOM



echo	"<h3>On air</h3>"

echo	"<table><td class="descr">Name:</td> <td><input type=\"text\" name=\"name\" value=\""$namekey"\"/></td></tr>"
echo	"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title\" value=\""$titlekey"\"/></td></tr></table>"

/bin/cat << EOM

	</div>

	<div class="presets">
	<h3>Presets</h3>
	<table>
EOM

echo		"<tr class="top"><td rowspan="2" class="set"><h4>Set 1</h4><input type="radio" name="use" value="1"></td>"
echo		"<td class="descr">Name:</td> <td><input type=\"text\" name=\"name1\" value=\""$name1key"\"/></td></tr>"
echo		"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title1\" value=\""$title1key"\"/></td></tr><tr><td colspan="3"><hr/></td></tr>"

echo		"<tr class="top"><td rowspan="2" class="set"><h4>Set 2</h4><input type="radio" name="use" value="2"></td>"
echo		"<td class="descr">Name:</td> <td><input type=\"text\" name=\"name2\" value=\""$name2key"\"/></td></tr>"
echo		"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title2\" value=\""$title2key"\"/></td></tr><tr><td colspan="3"><hr/></td></tr>"

echo		"<tr class="top"><td rowspan="2" class="set" ><h4>Set 3</h4><input type="radio" name="use" value="3"></td>"
echo		"<td class="descr">Name:</td> <td><input type=\"text\" name=\"name3\" value=\""$name3key"\"/></td></tr>"
echo		"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title3\" value=\""$title3key"\"/></td></tr><tr><td colspan="3"><hr/></td></tr>"

echo		"<tr class="top"><td rowspan="2" class="set"><h4>Set 4</h4><input type="radio" name="use" value="4"></td>"
echo		"<td class="descr">Name:</td> <td><input type=\"text\" name=\"name4\" value=\""$name4key"\"/></td></tr>"
echo		"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title4\" value=\""$title4key"\"/></td></tr><tr><td colspan="3"><hr/></td></tr>"

echo		"<tr class="top"><td rowspan="2" class="set"><h4>Set 5</h4><input type="radio" name="use" value="5"></td>"
echo		"<td class="descr">Name:</td> <td><input type=\"text\" name=\"name5\" value=\""$name5key"\"/></td></tr>"
echo		"<tr><td class="descr">Titel:</td> <td><input type=\"text\" name=\"title5\" value=\""$title5key"\"/></td></tr>"

/bin/cat << EOM
	 </table>
	</div>

	<center>
	<input type="submit" title="Submit" value="Ändern" class="submit"></input><br/>
	</center>
	</form>

Display: /display.html<br/>
Login: pi / raspberry<br/>
<br/>
Upstream Key Settings:<br/>
<ul>
<li>Mode: Chroma</li>
<li>Mask: top: 9, bottom: -9, left: -16, right: <b>15.98</b></li>
<li>Hue: 140 Grad</li>
<li>Gain: 57 %</li>
<li>Y Surpress: 52.1 %</li>
<li>Lift: 16.2 %</li>
</ul>
</body>
</html>
EOM


