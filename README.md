# Generator_20200324_simplified_regex
#### Simplified regex string generator
```  
by oran collins
20200324
```
----------

#### Example Generate random ip addresses
> \>python .\generator_cli.py "[1-255].[1-255].[1-255].[1-255]" 
=> 38.161.154.251

----

### How to install
>\>git clone https://github.com/wisehackermonkey/Generator_20200324_simplified_regex.git

> \>cd Generator_20200324_simplified_regex


### How to run Cli
> \>python .\generator_cli.py <Command string> 

#### Example Generate random ip address
> \>python .\generator_cli.py "[1-255].[1-255].[1-255].[1-255]"

##### returns

> Result: [1-255].[1-255].[1-255].[1-255] => 38.161.154.251
--------
### example strings can be generated using simplified regex*

```
combine multiple           : [acb][123][X-Z]                 => a2X
escaped , () and []        : [\,\(\[][123][X-Z]              => \3Z
IP address                 : [1-255].[1-255].[1-255].[1-255] => 252.249.168.79
```

##### *not really actually regex its just a few functions i created to mimic regex functionality

### TODO

#### fix phone number & imbeding
#### "([1-9][1-9][1-9])-([1-9][1-9][1-9])" does not work

```