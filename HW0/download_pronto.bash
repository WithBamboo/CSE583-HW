mkdir pronto
echo "Pronto includes bike data for 2015." > pronto/README.txt  
mkdir data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip ./open_data_year_one.zip
head *.csv
