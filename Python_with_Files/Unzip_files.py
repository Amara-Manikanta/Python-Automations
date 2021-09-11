import glob
from zipfile import ZipFile

# opening the zip file in READ mode
zip_files = glob.glob(r"filepath/*.zip")
print(zip_files)
for i in zip_files:
        with ZipFile(i, 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()

            # extracting all the files

            print('Extracting all the files now...')
            zip.extractall(r'destination filepath')
            print('Done!')