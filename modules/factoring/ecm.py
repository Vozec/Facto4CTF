import time
import threading
import ctypes

from modules.logger import logger,found_prime
from modules.utils import kill_sage

from sage.all import *

def ecm1(stop,n,args):
	try:
		t = KThread(stop,n,args)
		t.start()

		while(True):
			if(stop.is_cancelled):
				kill_sage()
			
			if not t.is_alive():
				if(t.found):
					stop.cancel()
				break

		return None

	except Exception as ex:
		logger('[+] Error: %s'%str(ex),'error',0,0)

class KThread(threading.Thread):
	def __init__(self, stop,n,args,**keywords):
		super(KThread, self).__init__()
		self.found 		= False
		self.stop  		= stop
		self.n 			= n
		self.args 		= args
	
	def run(this):
		try:
			fact = ecm.find_factor(this.n)
			if(len(fact) == 2 ):
				p = int(list(fact)[0])
				q = this.n//p
				if(not this.args.json):
					if(this.args.verbose):
						logger("[+] ecm1 attack found",'log',1,0)
					if not this.args.quiet:
						logger('[>] P=%s'%str(p),'flag',0,1)
						logger('[>] Q=%s'%str(q),'flag',0,1)
					else:
						print(str(p))
						print(str(q))
				else:
					print('{"method":"sage","factor":[%s,%s]}'%(str(p),str(q)))

				this.found = True
				return p,q

			else:
				res = '['+str(fact).replace(' *',',').replace("^","**")+'] '
				if(not args.json):
					if(args.verbose):
						logger("[+] Sage Factor found :",'log',1,0)
					if not args.quiet:
						logger('[>] Factors = %s'%str(res),'flag',0,1)
					else:
						print(str(res))
				else:
					print('{"method":"sage","factor":%s}'%(str(res)))

				this.found = True
				return res

				this.stop.cancel()
		except Exception as ex:
			logger('[+] Error: %s'%str(ex),'error',0,0)


# class KThread2(threading.Thread):
# 	def __init__(self, stop,n,args,**keywords):
# 		super(KThread, self).__init__()
# 		self.found 		= False
# 		self.stop  		= stop
# 		self.n 			= n
# 		self.args 		= args
	
# 	def run(this):
# 		try:
# 			fact = factor(this.n)
# 			if(len(fact) == 2 ):
# 				p = int(list(fact)[0])
# 				q = this.n//p
# 				if(not this.args.json):
# 					if(this.args.verbose):
# 						logger("[+] ecm1 attack found",'log',1,0)
# 					if not this.args.quiet:
# 						logger('[>] P=%s'%str(p),'flag',0,1)
# 						logger('[>] Q=%s'%str(q),'flag',0,1)
# 					else:
# 						print(str(p))
# 						print(str(q))
# 				else:
# 					print('{"method":"sage","factor":[%s,%s]}'%(str(p),str(q)))

# 				this.found = True
# 				return p,q

# 			else:
# 				res = '['+str(fact).replace(' *',',').replace("^","**")+'] '
# 				if(not args.json):
# 					if(args.verbose):
# 						logger("[+] Sage Factor found :",'log',1,0)
# 					if not args.quiet:
# 						logger('[>] Factors = %s'%str(res),'flag',0,1)
# 					else:
# 						print(str(res))
# 				else:
# 					print('{"method":"sage","factor":%s}'%(str(res)))

# 				this.found = True
# 				return res

# 				this.stop.cancel()
# 		except Exception as ex:
# 			logger('[+] Error: %s'%str(ex),'error',0,0)


# # def sage_search(n,args):
# 	try:
# 		if(args.verbose):logger("[+] Testing using Sage Fast Factorization :",'info',1,0)
# 		res = '['+str(factor(n)).replace(' *',',').replace("^","**")+'] '
# 		if(not args.json):
# 			if(args.verbose):
# 				logger("[+] Sage Factor found :",'log',1,0)
# 			if not args.quiet:
# 				logger('[>] Factors = %s'%str(res),'flag',0,1)
# 			else:
# 				print(str(res))
# 		else:
# 			print('{"method":"sage","factor":%s}'%(str(res)))
# 		return res
# 	except Exception as ex:
# 		print(ex)
# 		return None
