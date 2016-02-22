FROM continuumio/miniconda:3.19.0
MAINTAINER Björn Dahlgren <bjodah@DELETEMEgmail.com>
ENV PATH /opt/miniconda2/bin:$PATH
RUN git clone https://github.com/bjodah/dummypkg.git && \
    cd dummypkg && \
    conda install conda-build pytest && \
    conda build conda-recipe && \
    conda install --use-local dummypkg
RUN cd /tmp && \
    python -c 'import dummypkg; print(dummypkg.__file__)' && \
    python -m pytest --pyargs dummypkg
