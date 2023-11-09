#!/bin/zsh

source ~/.zshrc

cd=$(pwd)

# if [ "$1" = "zr" ]
# then
#     echo $1
# else
# fi
python3 ~/apm/functions/apmDevCore.py $cd $1 $2 $3 $4 $5