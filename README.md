# Python SDK for TruSTAR Balerion 
  
## Installation

### Requirements
1. Get the latest SDK by downloading as a [ZIP](https://github.com/trustar/trustar-balerion/archive/master.zip) and extract locally.  You can also clone the repository directly from [GitHub](https://github.com/trustar/trustar-balerion)

2. Make sure you have Python 2.7+ installed

3. Install py2neo V 2.0.8

  Python 2.7
  ```shell
  $ pip install py2neo==2.0.8
  ``` 
  Python 3
  ```shell
  $ pip3 install py2neo
  ``` 
4. Install pandas module

  Python 2.7
  ```shell
  $ pip install pandas
  ``` 
  Python 3
  ```shell
  $ pip3 install pandas
  ``` 
5. Download and install Neo4j from [here](https://neo4j.com/download/other-releases/). This code was tested on Neo4j V 2.3.8.

6. Install Project Balerion

  ```shell   
    $ cd trustar-balerion
    $ python setup.py install --force
   ```

## Configuration
1. copy `application_properties.ini` in the `balerion` directory to the `scripts` directory
2. To use a different Neo4j database edit the file `application_properties.ini` and point it to the new location. Currently it is setup to connect to a local Neo4j instance

## Running the code
Inside the `scripts` directory you will find the script `balerion_bayes.py` that you can run to compute the probabilities. It takes an input indicator value and a classification indicator type as inputs. The classification indicator type can either be `malware`or `campaign`

```shell
    $ cd scripts
    $ python balerion_bayes.py -i f34d5f2d4577ed6d9ceec516c1f5a744 -c malware
```
## Using your own dataset
Inside the `scripts` directory you will find the script `balerion_ingest.py` . Use this to input your own data in the Neo4j db and persist it.

## For slackers
If you have any questions, you can also go to our project-balerion dedicated slack [channel](https://trustar-users.slack.com/archives/project-balerion).
