#!/bin/bash

# Define variables
PARENT_FOLDER="/media/kostageo/data/HELOISA/Inputs/Axis-1.1/ORORATECH/thermal-wildfire/ororatech_fire-danger-forecasting"   # folder that contains subfolders
DEST_FOLDER="/media/kostageo/data/HELOISA/Inputs/Axis-1.1/ORORATECH/thermal-wildfire/ororatech_fire-danger-forecasting/intersection" # Destination for the copied files
SHAPEFILE_PATTERN="*_LWIR2MWIR_intersection.shp" # characteristic pattern of intersection file

# Create destination folder if it doesn't exist
mkdir -p "$DEST_FOLDER"

# Navigate to the parent folder
cd "$PARENT_FOLDER" || exit

# Process each matching shapefile
find . -type f -name "$SHAPEFILE_PATTERN" | while IFS= read -r shpfile; do
    dir=$(dirname "$shpfile")  # Get the directory of the shapefile
    base=$(basename "$shpfile" .shp)  # Get the base name without extension

    echo "Processing: $shpfile"

    # Find all related files and copy them to the destination folder
    find "$dir" -type f \( -name "$base.shp" -o -name "$base.shx" -o -name "$base.dbf" -o -name "$base.prj" -o -name "$base.cpg" -o -name "$base.sbn" -o -name "$base.sbx" \) | while IFS= read -r file; do
        cp --parents "$file" "$DEST_FOLDER"  # Copy file with relative path
    done
done

echo "Files copied to $DEST_FOLDER"
