FROM continuumio/miniconda:3.19.0
MAINTAINER Björn Dahlgren <bjodah@DELETEMEgmail.com>
ENV PATH /opt/miniconda2/bin:$PATH
RUN git clone https://github.com/bjodah/dummypkg.git && \
    cd dummypkg && \
    conda install conda-build  && \
    conda build conda-recipe && \
    conda create -c bjodah -n dummy2 python=2.7 dummypkg pytest
RUN bash -c "cd /tmp; source activate dummy2 && python -c 'import dummypkg; print(dummypkg.__file__)' && python -m pytest --pyargs dummypkg"
