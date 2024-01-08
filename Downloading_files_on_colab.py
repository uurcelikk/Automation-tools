# Create output folder
output_folder = '/content/output'
!mkdir $output_folder

# copy the folder you want to download to the output folder
!cp -r /content/...* $output_folder/


zip_filename = '/content/output.zip'
!zip -r $zip_filename $output_folder

from google.colab import files
files.download(zip_filename)