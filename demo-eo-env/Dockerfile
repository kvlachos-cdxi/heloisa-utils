FROM ghcr.io/osgeo/gdal:ubuntu-small-latest
# FROM python:3.10-slim

WORKDIR /home/
# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3.10 and pip
RUN apt-get update && \
apt-get install -y python3.10 python3-venv python3-pip && \
rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default
RUN ln -sf /usr/bin/python3.10 /usr/bin/python

# Install Python dependencies in a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip inside the virtual environment
RUN pip install --upgrade pip
RUN pip install "dask[array]" xarray rioxarray jupyterlab matplotlib GDAL
# scikit-image pillow
# RUN pip install pymongo
# RUN pip install imblearn rasterstats ipympl folium
# RUN pip install eo-learn openpyxl
RUN jupyter lab --generate-config
COPY jupyter.py /root/.jupyter/jupyter_lab_config.py

#RUN cd /home/ && wget https://download.osgeo.org/proj/proj-8.0.0.tar.gz && tar -xf proj-8.0.0.tar.gz
#RUN cd /home/proj-8.0.0 && mkdir build && cd build && cmake .. && cmake --build . && cmake --build . --target install
#RUN cd /home/data/proj-8.0.0/build && ctest
#RUN cp /home/proj-8.0.0/bin/* /bin

#RUN pip install geoviews

#CMD ["tail", "-f", "/dev/null"]
ENTRYPOINT ["jupyter", "lab"]
