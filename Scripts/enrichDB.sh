mysql -u root <<EOF
USE $1;
SOURCE ../DSW/Outputs/$1/$2;
exit
EOF
