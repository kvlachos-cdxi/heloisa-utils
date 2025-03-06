#!/bin/bash

# Define variables
PARENT_FOLDER="/media/kostageo/data/HELOISA/Inputs/Axis-1.1/ORORATECH/thermal-wildfire/ororatech_fire-danger-forecasting" # folder that contains subfolders
ZIP_NAME="fire-danger-forecasting.zip" # Name of the output ZIP file
SHAPEFILE_PATTERN="*_LWIR2MWIR_intersection.shp" # characteristic pattern of intersection file

# Navigate to the parent folder
cd "$PARENT_FOLDER" || exit

# Clear file list
> file_list.txt  

# Find shapefiles and add their related files
find . -type f -name "$SHAPEFILE_PATTERN" | while IFS= read -r shpfile; do
    dir=$(dirname "$shpfile")  # Extract directory
    base=$(basename "$shpfile" .shp)  # Extract filename w/o extension

    echo "Processing: $shpfile"

    # Find all SHP-related files and add them to file_list.txt
    find "$dir" -type f \( -name "$base.shp" -o -name "$base.shx" -o -name "$base.dbf" -o -name "$base.prj" -o -name "$base.cpg" -o -name "$base.sbn" -o -name "$base.sbx" \) >> file_list.txt
done

# Show files that were found
echo "Files to be zipped:"
cat file_list.txt

# Ensure file_list.txt is not empty before zipping
if [[ -s file_list.txt ]]; then
    zip -@ "$ZIP_NAME" < file_list.txt
    echo "Zipping completed: $ZIP_NAME"
else
    echo "Something went wrong. No files found."
fi

# Cleanup
# rm file_list.txt


echo "Zipping completed: $ZIP_NAME"
