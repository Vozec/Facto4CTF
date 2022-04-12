from factordb.factordb import FactorDB
from modules.logger import logger,found_prime

def factordb_search(stop,n,timeout,args):
	try:
		f = FactorDB(n)
		f.connect()
		res = f.get_factor_list()
		if len(res) == 2:
			p = res[0]
			q = res[1]
			found_prime(p,q,stop,args,'factordb')
			return p,q
		else:
			return res
	except Exception as ex:
		print(ex)
		return None