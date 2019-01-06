#influx -execute 'drop measurement kml' -database="gis"
influx -execute 'drop measurement tvalue' -database="gis"
influx -execute 'drop measurement mapdata' -database="gis"
influx -execute 'drop measurement auto_summary' -database="gis"
#influx -execute 'drop measurement memory' -database="Merged"

