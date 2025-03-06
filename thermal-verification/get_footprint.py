import os
from pathlib import Path
import tempfile
import re
from datetime import datetime

import geopandas as gpd

def valid_to_zero(input_fpath, temp=True, no_data='65555'):
    """
    Args:
        input_fpath (pathlib.Path)
        temp (bool)
        no_data (str)
    """
    if temp:
        temp_dir = Path(tempfile.gettempdir())
        temp_fpath = temp_dir/'output.tif'
    else:
        add_suffix = '_valid'
        temp_fpath = input_fpath.with_name(input_fpath.stem + add_suffix + input_fpath.suffix)

    cmd = f"gdal_calc.py -A {input_fpath} --outfile={temp_fpath} --calc=\"A*0\" --NoDataValue={no_data} --overwrite"

    os.system(cmd)

    return temp_fpath

def raster_to_vector(input_fpath, output_fpath, temp=False,):
    """
    Args:
        input_fpath (pathlib.Path)
        output_fpath (pathlib.Path)
        temp (bool)

    """
    if temp:
        temp_dir = Path(tempfile.gettempdir())
        output_fpath = temp_dir/'output.shp'
    else:
        pass
        # output_fpath = output_fpath.with_suffix('.shp')
    
    # Convert raster to vector (polygonize)
    # vector_fname = output_fpath.name
    cmd = f"gdal_polygonize.py {input_fpath} -b 1 -f \"ESRI Shapefile\" {output_fpath} {output_fpath.stem} date"

    os.system(cmd)

    return output_fpath

def shp_intersection(input_shp_list, output_shp):
    """
    Args:
        shp_files (list): list of shapefile paths
    """
    # Load the two shapefiles
    shp1 = gpd.read_file(input_shp_list[0])
    shp2 = gpd.read_file(input_shp_list[1])

    # Ensure both shapefiles are using the same CRS (Coordinate Reference System)
    shp2 = shp2.to_crs(shp1.crs)

    # Perform intersection
    intersection = gpd.overlay(shp1, shp2, how='intersection')

    # Keep only the 'geometry' column (drop all existing fields)
    intersection = intersection[['geometry']]

    # extract datetime
    extracted_datetime = datetime_from_string(input_shp_list[0])
    intersection['datetime'] = extracted_datetime
    # merge records
    intersection = intersection.dissolve(by='datetime')

    # Save the result to a new shapefile
    intersection.to_file(output_shp)

    return None

def datetime_from_string(s):
    """
    """

    match = re.search(r"\d{4}-\d{2}-\d{2}T\d{6}\.\d+Z", s.stem)

    if match:
        extracted_datetime = match.group() #datetime.strptime(match.group(), "%Y-%m-%dT%H%M%S.%fZ")
    else:
        extracted_datetime = "Unknown" #datetime.today()

    return extracted_datetime

############################# BEGIN #############################

# Define path with images
parent_dir = Path('/media/kostageo/data/HELOISA/Inputs/Axis-1.1/ORORATECH/Forest-2_GR_082024')


for subdir in parent_dir.iterdir():
    
    print(subdir.name)

    if subdir.is_dir():
    
        tif_files = list(subdir.glob("*.tif")) + list(subdir.glob("*.tiff"))
        
        if tif_files: # Ensure there's one tif at least
            tif_files = [item for item in tif_files if ('LWIR2' in item.name) or ('MWIR' in item.name)]
        
        shp_file_list = []
        for raster_fname in tif_files:
            # raster_fname = tif_files[0]  # Pick the first

            # Apply band math and convert valid values to 0
            input_fpath = subdir/raster_fname
            temp_fpath = valid_to_zero(input_fpath)

            # Convert raster to vector (polygonize)
            shp_file_list.append(raster_to_vector(input_fpath=temp_fpath, output_fpath=input_fpath.with_suffix('.shp'), temp=False))

            # clean temp file explicitly
            if temp_fpath.exists():
                temp_fpath.unlink()
                # print("Temporary file deleted successfully.")
            else:
                pass
                # print("Temporary file not found.")
        
        output_shp = subdir/(subdir.name + '_LWIR2MWIR_intersection.shp')
        shp_intersection(input_shp_list=shp_file_list, output_shp=output_shp)

        # print("Intersection finished successfully.")
        # break