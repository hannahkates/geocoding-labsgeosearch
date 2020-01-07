# geocoding-labsgeosearch
Python script for batch geocoding using NYC Planning Labs' [Geosearch API](https://geosearch.planninglabs.nyc/)

# Instructions:
1. Create a folder on your computer where you save the python script for your version of Python. Use [`geosearch_2.py`](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch_2.py) if you're using Python 2. Alternately, use [`geosearch_3.py`](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch_3.py) if you're using Python 3.
2. Place the ungeocoded data csv file in the same folder as the python script.
3. Open your data csv to identify which column #s are relevant for the geocoding script. Begin counting from zero.
4. Update the column numbers for the house number, street name, and borough columns in the python script on lines [10-14](https://github.com/hannahkates/geocoding-labsgeosearch/blob/master/geosearch_3.py#L10).
5. Via the command line, navigate inside the folder.
6. Run the script by running `python geosearch_v.py input.csv output.csv` in the command line, filling in the appropriate vairables:
     - `_v` version for your Python version
     - input csv file name
     - preferred output file name

If the script is running correctly, you will see it printing the results in the terminal for each row it iterates through.
