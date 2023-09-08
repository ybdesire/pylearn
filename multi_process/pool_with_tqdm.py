from multiprocessing import Pool
import tqdm
import time

def _foo(my_number):
   square = my_number * my_number
   time.sleep(1)
   return square 

if __name__ == '__main__':
   # 6 tasks for 2 processes
   with Pool(2) as p:
      r = list(tqdm.tqdm(p.imap(_foo, [1,2,3,4,5,6]), total=6))
      print(r)
