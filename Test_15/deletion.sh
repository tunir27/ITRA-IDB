rm /home/pi/Test_15/fold/merged.txt
rm /home/pi/Test_15/fold/date.txt
rm /home/pi/Test_15/fold/Statistics.csv
#rm /home/pi/Test_15/fold/clustermap.geojson
#rm /home/pi/Test_15/fold/media.txt
rm /home/pi/Test_15/fold/counter.json
rm -rf /home/pi/Test_15/fold/sync/*
rm /home/pi/Test_15/fold/fileDB.txt
rm /home/pi/Test_15/kmlFiles/tempDecrypt/*
rm /home/pi/Test_15/kmlFiles/*.kml
rm /home/pi/Test_15/PatchedKML/*

influx -execute 'drop measurement kml' -database="gis"
# influx -execute 'drop measurement tvalue' -database="gis"
# influx -execute 'drop measurement mapdata' -database="gis"
# influx -execute 'drop measurement auto_summary' -database="gis"
influx -execute 'drop measurement memory' -database="Merged"

