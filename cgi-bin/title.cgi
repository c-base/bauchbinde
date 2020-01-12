#!/bin/sh
echo Content-type: text/html
echo ""

read title < title.key

echo $title
