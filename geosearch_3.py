from sys import argv
import urllib.request as req
import csv
import json

# Run script by running: `python geosearch.py input.csv output.csv` in the command line, filling in the correct file names

# Important variables: In which column number (starting from zero) is the...
# house number?
col_street_num = 6
# street name?
col_street_name = 7
# borough?
col_boro = 2


script, infile, outfile = argv

print("opening file: %s" % infile)
with open(infile, 'r') as i:

    reader = csv.reader(i)

    print("opening file: %s" % outfile)
    with open(outfile, 'w') as o:

        writer = csv.writer(o, lineterminator='\n')
        all = []
        row = next(reader, None)
        row.extend(['latitude', 'longitude', 'bbl', 'bin'])
        all.append(row)

        index = 1
        try:
            for row in reader:

                input_address = row[col_street_num] + ' ' + row[col_street_name] + ' ' + row[col_boro]

                url = ('http://geosearch.planninglabs.nyc/v1/search?text=' + input_address + '&size=1')
                response = req.urlopen(url)
                data = json.load(response)
                row_lat = data['features'][0]['geometry']['coordinates'][1]
                row_long = data['features'][0]['geometry']['coordinates'][0]
                row_bbl = data['features'][0]['properties']['pad_bbl']
                row_bin = data['features'][0]['properties']['pad_bin']

                print("%s, Address: %s, BBL: %s, BIN: %s" % (index, input_address, row_bbl, row_bin))
                row.extend([row_lat, row_long, row_bbl, row_bin])
                all.append(row)

                index += 1

            writer.writerows(all)

        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (infile, reader.line_num, e))
