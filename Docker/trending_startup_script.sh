#!/bin/bash

res=6
while [ $res -eq 6 -o $res -eq 7 ]
do
	sleep 1
	curl -s $DATA_DATABASE_HOST:3306
	res=$?
done

python Product/Database/DBConn.py
python Product/Database/DBFillSmallSet.py
python Product/TrendManager/RunTrend.py
