File sorter by type
===================

sort.py is the python script which sorts all files in the specified path into their respective folders according to the specifications in the list.lst file
Pattern for list.lst file:
every word should be followed by a space
The type should be written first followed by an equal to (=) sign, again followed by the list of extensions of files to be placed in the specified folder
For example: If all rpm , deb, jar files have to be placed in  a folder named applications they should be done as follows:


Applications = rpm deb jar 

Every other specification should start from a different line


Known Issues:
If the specified folder already contains the file with the same name as the file yet to be copied inside it would give up an error in copying


The application hasn't been fully tested yet. USE WITH CAUTION
