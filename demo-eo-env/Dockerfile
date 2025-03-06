FROM python:3.9

RUN pip3 install --upgrade pip
RUN pip install jupyterlab matplotlib scikit-image pillow
RUN pip install "dask[array]"
RUN pip install pymongo
RUN pip install imblearn rasterstats ipympl folium
RUN pip install eo-learn==0.8.0 openpyxl
RUN jupyter lab --generate-config
COPY jupyter.py /root/.jupyter/jupyter_lab_config.py
#RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -O /home/miniconda.sh && \
#bash /home/miniconda.sh -b -p $HOME/miniconda

#RUN source ~/miniconda/bin/activate && conda init
#RUN conda update -n base -c defaults conda -y
#RUN apt update && apt install -y libgeos-dev \
#cmake \
#sqlite3 \
#curl \
#libcurl4-openssl-dev

#RUN cd /home/ && wget https://download.osgeo.org/proj/proj-8.0.0.tar.gz && tar -xf proj-8.0.0.tar.gz
#RUN cd /home/proj-8.0.0 && mkdir build && cd build && cmake .. && cmake --build . && cmake --build . --target install
#RUN cd /home/data/proj-8.0.0/build && ctest
#RUN cp /home/proj-8.0.0/bin/* /bin

#RUN pip install geoviews

#CMD ["tail", "-f", "/dev/null"]
ENTRYPOINT ["jupyter", "lab"]
