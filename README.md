![Tarantulla Twitter: a module for Twitter data extraction](./tarantulla-twitter-post.png)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg?style=for-the-badge) 
![LINUX](https://img.shields.io/badge/PLATFORM-LINUX-blue.svg?style=for-the-badge) 
![CRAN](https://img.shields.io/badge/LICENSE-GPLv3-blue.svg?style=for-the-badge) 
![LOVE](https://img.shields.io/badge/BUILT%20WITH-LOVE-red.svg?style=for-the-badge)
[![TWITTER](https://img.shields.io/badge/BY-@oncase-lightgrey.svg?style=for-the-badge)](https://twitter.com/oncase) 


## **"Tarantulla-Twitter: the solution to gather Twitter data from publishers of your interest."**  

If you want to know more, check out Tarantulla's [landing page](http://tarantulla.io/) and our [post](https://medium.com/oncase/extracting-data-from-twitter-with-tarantulla-c25f3a0a26d5) in Medium.
 
On this document you will find information about:
 
- [Requirements](#requirements)  
- [Installation](#installation)   
- [How to Run](#how-to-run)  
- [Running with PDI - Database Integration](#running-with-pdi---database-integration)


## Requirements 
- [Python 3.x (>=3.4)](https://www.python.org/getit/)
- [Tweepy](http://www.tweepy.org/)  
```Attention! You can install Tweepy with pip3```  
```sh
   $ sudo apt-get install python3-pip  
   $ pip3 install tweepy
```

## Installation

First things first: *git clone* this project. Prefer to clone in folder `/opt/git`.

## How to Run

### Configuration

1 - Edit `config-timeline.json`

All publishers and information such as output folders and python call should be defined on this file, according to the example:

```json
{
	"temp_output": "../data/",
	"python-command":"python3",	
	"publishers" :
	[
		{
		  "_twitter_screen": "AndroidPITcom",
		  "name": "AndroidPIT US"
		}
	]
}
```

with fields:

- temp_output = output folder used to store files created during execution  
  ```Attention! Folder path specified is relative to project's folder `/core` ```
- python-command = command that calls Python 3.x
- publishers =
    - _twitter_screen = user screen name to be queried (it comes after the `@`, for instance the screen name of `@oncase` is `oncase`)
    - name = user full name


The `_twitter_screen` is **fixed**, defined by Twitter, whereas `name` is **not fixed**, what means you can choose any `name` you think is representative for you. Additionaly, you can add more fields in case you need other information for any further application development. 

2 - Edit `api-keys.json`

All Twitter API access keys should be specified on this file. The script will require the following access keys:

```json
{
	"ACSSTK":"[YOUR ACCESS TOKEN]",
	"ACSSTKSCRT":"[YOUR ACCESS TOKEN SECRET]",
	"CONSMKEY":"[YOUR CONSUMER KEY]",
	"CONSMKEYSCRT":" [YOUR CONSUMER KEY SECRET]"
}
```
You can obtain the API keys for your project following these [steps](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html).

### Execution

Execute the script `user_timeline_api.py`, in the folder `/core`, with the **Python 3** command set on your machine. The API returns tweets from the most recent one backwards. 

```bash
$ python3 user_timeline_api.py
```

The **output** is a JSON file containing the fields:

- twitter id
- timestamp
- publication date
- publisher screen name
- publisher full name
- tweet content
- hashtags
- language
- locale
- category
- tweet url
- number of retweets
- number of favorites
- engagement


## Running with PDI - Database Integration

PDI or *Pentaho Data Integration* is a platform to accelerate data pipeline, providing visual tools to reduce complexity. In this project PDI was used to integrate the results into a database such as PostgreSQL. If you want to organize your data in a database as well, follow the next steps. 

To know more about PDI, check out the [documentation](https://help.pentaho.com/Documentation/8.1). It is worth remember that PDI requires JAVA installed on your machine.

### Configuration

Steps 1 and 2 are the same as above, what means you must configure both files: `config-timeline.json` and `api-keys.json`. Additionaly, in order to run Tarantulla-Twitter with PDI you should perform 2 more steps:

3- Edit file `config-db.json` - Set JDBC connection, Database and Table.

```json
{  
	"database_config" :  
   {
		"database_name" : "postgres",
		"database_url" : "jdbc:postgresql://localhost:5432/",
		"database_driver" : "org.postgresql.Driver",
		"database_username" : "postgres",
		"database_password" : "[YOUR PASSWORD]",
		"database_schema" : "staging",
		"database_table" : "stg_twitter"  
	}
}
```

The above JSON is an example and you can change the fields' values according to your database configurations. 

4- Execute DDL

Execute the script `tarantulla-twitter/scripts/ddl.sql` with the appropriate changes for your environment/database. Remember to change `<yourSCHEMA>` and `<yourTABLE>` names in the script, according to the variables set in `config-db.json`.

``` Attention! If the schema does not already exist, you should create it before execute the SQL script. ```

``` Attention! In order to establish a connection to the database, PDI must have the correspondent database driver in the folder `<YOURPENTAHO>/design-tools/data-integration/lib`. ```

### Execution

When all is set, you can execute `main.kjb` directly from Pentaho `kitchen.sh` script. You should locate the **folder with PDI files** (PDI_HOME) and run:

```bash
$ <PDI_HOME>/./kitchen.sh  -file="<YOUR TARANTULLA TWITTER FOLDER>/etl/main.kjb"    
```

Alternatively, if your **PDI_HOME** is set to `/opt/Pentaho/design-tools/data-integration`, you can directly run the `etl.sh` script. 

```bash
$ <YOUR TARANTULLA TWITTER FOLDER>/scripts/etl.sh job ../etl/main.kjb    
```

Please, note that in order to execute `etl.sh`, the script must have the appropriate execution permissions in your system.

## License

Tarantulla-Twitter is released under the GPLv3 license.