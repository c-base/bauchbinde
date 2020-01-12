#!/bin/sh
echo Content-type: text/html
echo ""

read name < name.key

echo $name
