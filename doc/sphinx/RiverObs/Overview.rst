RiverObs Packages Overview
========

This is a package written initially by `Ernesto
Rodriguez <mailto:ernesto.rodriguez@jpl.nasa.gov>`__ to estimate various
river parameters starting from remote sensing data.

Detailed installation instructions are in the Install.md file.

Summary of packages provided
----------------------------

**RiverObs**: This is the main package for associating data with river
reaches, and estimating hydrology parameters base on reach averaging (or
not...). In addition to the homegrown packages listed below, this
package requires the following open source packages:

-  `scipy <http://www.scipy.org/>`__: Science algorithms swiss army
   knife.
-  `numpy <http://www.scipy.org/>`__: Numerics swiss army knife.
-  `netCDF4 <code.google.com/p/netcdf4-python>`__: Reading netcdf4
   files, including SWOT L2 data files.
-  `StatsModels <http://statsmodels.sourceforge.net>`__: Fitting and
   estimation tools.
-  `pysal <http://pysal.org>`__: nice interface to shapefiles and
   shapely bridge.
-  `pyproj <http://code.google.com/p/pyproj>`__: Cartographic
   projections swiss army knife.
-  `pandas <http://pandas.pydata.org>`__: The Python Data Analysis
   Library for DataFrames and HDFStore.
-  `pytables <http://www.pytables.org>`__: easy HDF5 support, required
   for pandas HDFStore.

**Centerline**: Provides a class that can be used to project data or
refine a river center line. Requires the following packages:

-  `scipy <http://www.scipy.org/>`__: Science algorithms swiss army
   knife.
-  `numpy <http://www.scipy.org/>`__: Numerics swiss army knife.

**GeometryDataBase**: Find quickly which reach intersects with a
geometry of interest. The geometries are assumed to be stored in a
shapefile. Requires the following packages:

-  `Rtree <https://github.com/Toblerity/rtree>`__: Fast bounding box
   queries.
-  `libspatialindex <http://libspatialindex.github.io>`__: Required by
   Rtree.
-  `pysal <http://pysal.org>`__: nice interface to shapefiles and
   shapely bridge.
-  `shapely <https://github.com/sgillies/shapely>`__: geometry
   calculations.

**SWOTRiver**: This package contains classes that use the RiverObs
capabilities to produce hydrology outputs from SWOT (simulated) data.

-  `numpy <http://www.scipy.org/>`__: Numerics swiss army knife.
-  `netCDF4 <code.google.com/p/netcdf4-python>`__: Reading netcdf4
   files, including SWOT L2 data files.
-  `pyproj <http://code.google.com/p/pyproj>`__: Cartographic
   projections swiss army knife.
-  `pandas <http://pandas.pydata.org>`__: The Python Data Analysis
   Library for DataFrames and HDFStore.
-  `pytables <http://www.pytables.org>`__: easy HDF5 support, required
   for pandas HDFStore.

**GDALOGRUtilities**: Provides homegrown utilities for reading and
writing various GIS files. Requires the following packages:

-  `gdal <http://www.gdal.org>`__: GIS files swiss army knife.
-  `pyproj <http://code.google.com/p/pyproj>`__: Cartographic
   projections swiss army knife.

**GWDLR**: This is an optional package to convert Global Width
Database-Large Rivers raster data provided by `Dai
Yamazaki <mailto:bigasmountain1022@gmail.com>`__ to vectors that can be
used as centerlines. Requires:

-  `grass <http://grass.osgeo.org>`__: for raster to vector program.
-  `scikit-image <http://scikit-image.org>`__: for skeletonize.

