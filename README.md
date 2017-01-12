# Python SDK for the TruSTAR Balerion 
  
## Installation

### Manual
1. Get the latest SDK by downloading as a [ZIP](https://github.com/trustar/trustar-balerion/archive/master.zip) and extract locally.  You can also clone the repository directly from [GitHub](https://github.com/trustar/trustar-balerion)

2. Install requirements

 Python 2.7+:
* py2neo V 2.0.8 python module

  ```shell
  $ pip install py2neo==2.0.8
  ``` 
  
 Python 3:
* py2neo V 2.0.8 python module

  ```shell
  $ pip3 install py2neo
  ``` 
  
 Python 2.7+:
* pandas 

  ```shell
  $ pip install pandas
  ``` 
  
 Python 3:
* pandas

  ```shell
  $ pip3 install pandas
  ``` 
  
3. Install SDK

  ```shell   
    $ cd trustar-balerion
    $ python setup.py install --force
   ```

4. You can download and install Neo4j from [here](https://neo4j.com/download/other-releases/). This code was tested on Neo4j V 2.3.8.

## Running examples and tests
- copy `application_properties.ini` in the `balerion` directory to the `scripts` directory
- To use a different Neo4j DataBase edit the file `application_properties.ini`. Currently it is setup to connect to a 
local Neo4j instance
- Inside the `scripts` directory you can find the script that you can run to compute the probabilities by giving an indicator as an input

```shell
    $ cd scripts
    $ python balerion_bayes.py -i f34d5f2d4577ed6d9ceec516c1f5a744
```
