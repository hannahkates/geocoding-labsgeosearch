# geocoding-labsgeosearch
Python script for batch geocoding using NYC Planning Labs' [Geosearch API](https://geosearch.planninglabs.nyc/)

# Instructions:
1. Create a folder on your computer where you save the python script.
2. Place the ungeocoded data csv file in the same folder as the python script.
3. Open your data csv to identify which column #s are relevant for the geocoding script. Begin counting from zero.
4. Update the column numbers for the house number, street name, and borough columns in the python script on lines [10](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch.py#L10), [12](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch.py#L12), and [14](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch.py#L14).
5. Via the command line, navigate inside the folder.
6. Run the script by running `python geosearch.py input.csv output.csv` in the command line, filling in the appropriate input csv file name and preferred output file name.

If the script is running correctly, you will see it printing the results in the terminal for each row it iterates through.
