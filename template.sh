#!/bin/sh

template="template/my_template.py"

echo $1/$2
echo $template

mkdir $1/$2

cp ${template} "$1/$2/A_t.py" 
cp ${template} "$1/$2/B_t.py" 
cp ${template} "$1/$2/C_t.py" 
cp ${template} "$1/$2/D_t.py" 
cp ${template} "$1/$2/E_t.py" 
