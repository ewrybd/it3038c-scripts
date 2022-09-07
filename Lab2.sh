#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')
DEATHS=$(echo $DATA | jq '.[0].death')
VENTILATOR=$( echo $DATA | jq '.[0].onVentilatorCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, and $TOTALTESTRESULTS total test results. There were also $DEATHS total deaths and $VENTILATOR people are on a ventilator currently."
