# -------- PERCENT DIFFERENCE -------- #

def pd(new,old):
   if(old == 0): return 0
   else: return ((new-old)/old)*100

# -------- NON-ZERO DIVISION -------- #

def div(aa,bb):
   if(bb != 0): return aa/bb
   else: return 0

# -------- FORMAT -------- #

def format(any_num):
   num = float(any_num)
   if(num >= 10.0): return '%.2f'%(num) # 170.98
   if(num < 0.01):  return '%.8f'%(num) # 0.00894621
   if(num < 0.10):  return '%.6f'%(num) # 0.059314
   if(num < 10.00): return '%.4f'%(num) # 98.5632

# -------- -------- -------- #