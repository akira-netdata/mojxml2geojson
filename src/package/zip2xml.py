# coding: utf-8

import os
import pathlib
import zipfile
import package.xml2geojson

def SaveGeoJson(src_file, exclude_flag):
    suffix = pathlib.PurePosixPath(src_file).suffix
    dir_name = os.path.dirname(src_file)
    # print('[Path]', dir_name)
    if suffix == ".xml":
        print(' [Convert]', src_file)
        package.xml2geojson.SaveGeoJson(src_file, exclude_flag)
    elif suffix == ".zip":
        # print('[Zip]', src_file)
        with zipfile.ZipFile(src_file) as zf:
            filelist = zf.namelist()
            for file in filelist:
                # print('[Extract]', file)
                inner_file = zf.extract(file, dir_name)
                SaveGeoJson(inner_file, exclude_flag)
                os.remove(inner_file)
    else:
        print('[Skip]', src_file)
