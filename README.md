Scalable database cluster for the spatial analysis and annotation of high-throughput brain imaging data called Neurodata Web Services(formerly called the Open Connectome Project).

[![Neurodata.io](https://img.shields.io/badge/Visit-neurodata.io-ff69b4.svg)](http://neurodata.io/)
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.19972.svg)](http://dx.doi.org/10.5281/zenodo.19972)
[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![Docs](https://img.shields.io/badge/Docs-latest-brightgreen.svg)](http://docs.neurodata.io/ndstore/)
[![Build Status](https://travis-ci.org/neurodata/ndstore.svg?branch=microns)](https://travis-ci.org/neurodata/ndstore.svg?branch=master)
[![Service Status](https://img.shields.io/badge/service-status-lightgrey.svg)](http://neurodata.statuspage.io/)


#### Major directories include:

  * spdb -- [Spatial Database submodule](https://github.com/neurodata/spdb)
  * ndingest -- [AWS Wrappers for Parallel Ingest submodule](https://github.com/neurodata/ndingest)
  * ndlib -- [Common library and Ctype accelerations submodule](https://github.com/neurodata/ndlib)
  * ingest-client -- [Ingest client and related services submodule](https://github.com/neurodata/ingest-client)
  * webservices -- Webservices module
  * ndproj -- Project Module
  * ramon -- RAMON and Annotation metadata module
  * django -- Django module
  * setup -- Install script, setup instructions and configurations
  * test -- Test module
  * examples -- How to use the service
  * admin -- Scripts to manage the databases
  * docs -- Sphinx documentation for the project
  * scripts -- Useful general purpose scripts

NOTE: git submodule init and git submodule update for all submodules

#### Architecture

![](./docs/images/neurodata_cluster.png)

#### Installation

* Use a fresh Ubuntu14.04 instance with sudo access.
```console
wget https://raw.githubusercontent.com/neurodata/ndstore/master/setup/ndstore_install.sh
sudo chmod 7000 ndstore_install.sh
sudo ./ndstore_install.sh
```
**Note:** *ndstore does not support Docker images because running custom systemd services needs some relaxation of security on the Docker engine leading to issues. We recommend using the install script used above*

#### Benchmarks

The benchmarks were performed on AWS EC2 instance type i2.8xlarge with a MySQL backend.

##### Read Throughput

![](./docs/images/neurodata_read_throughput.png)

##### Write Throughput

![](./docs/images/neurodata_write_throughput.png)
