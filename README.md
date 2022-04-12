<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/badge/Version-1.0-blue.svg">
</p>

#  Facto4CTF

# Description:

This tool is used to try out different factoring techniques (based on RsaCTFTool) . Mainly used in CTF.

## Commands :
```
usage: facto4ctf.py [-h] -n NUMBER [-a] [-m ALGORITHM] [-t TIMEOUT] [-v] [-q]

This tool is used to try out different factoring techniques. Mainly used in CTF.

optional arguments:
  -h, --help    show this help message and exit
  -n NUMBER     Number to factor
  -a            Try all algorithm
  -m ALGORITHM  Choose an algorithm : ['factordb', 'fermat', 'ecm', 'ecm2', 'pollard_rho',
                'pollard_p_1', 'z3', 'smallq', 'mersene_prime', 'mersenne_pm1_gcd', 'euler',
                'fibonacci_gcd', 'brent', 'smallfraction', 'roca', 'qicheng']
  -t TIMEOUT    Set Timeout (minutes) (default=5min)
  -v            Use verbose mode.
  -q            Use quiet mode.
```

## Usage:

```bash
python3 facto4ctf.py -n 116494485484276737265056867707564079277355622643710445921186078058108350067819908890379635482659796593831763584687113089573852770295651492307690383478101687323076624991486165778718257549416099776035451714559549671189631313045240181809169254865807076496196762757332143476724463538968420427013 -a -v
```

## Installation :
```bash
git https://github.com/Vozec/Facto4CTF.git
cd Facto4CTF
python3 -m pip install -r requirements.txt
```

## Options :
- **-t** : Set Timeout
- **-a** : Test all algorithm
- **-q** : Don't displays the header

## Démo :

![Alltext](./image/example.png)
