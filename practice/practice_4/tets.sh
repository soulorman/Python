#!/bin/bash

#test.sh --config 'client.conf' restart
#test.sh --config 'client.conf' --gpu 0,1 restart
#test.sh --config 'client.conf' --gpu 0,1 develop restart
#test.sh --config 'client.conf' --gpu 0,1 develop restart log-service
#test.sh restart

postion=()
ARGS=''

while [[ $# -gt 0 ]]
do
    KEY=$1
    if [[ $KEY == --* ]]
    then
       ARGS="${ARGS} ${KEY} $2"
       shift
       shift
    else
       postion+=("$1")
       shift
    fi
done

ENV=${postion[0]}
OPTION=${postion[1]}
SERVER=${postion[2]}

ARGS_STR="--env ${ENV} --option ${OPTION} ${ARGS}"
echo $ARGS_STR



