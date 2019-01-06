rm /home/pi/Test_15/fold/clustermap.geojson
rm /home/pi/Test_15/fold/smooth.txt
rm /home/pi/Test_15/fold/report.txt
rm /home/pi/Test_15/Final_output.txt
rm /home/pi/Test_15/output.pdf
rm /home/pi/Test_15/test.pdf

influx -execute 'drop measurement kml' -database="Test"
influx -execute 'drop measurement tvalue' -database="Test"
influx -execute 'drop measurement mapdata' -database="Test"
influx -execute 'drop measurement auto_summary' -database="Test"
#influx -execute 'drop measurement memory' -database="Merged"

