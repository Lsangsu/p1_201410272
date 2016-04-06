def ComputeBmi(h,w):
   ...:     bmi=w/(h*h)
   ...:     if bmi<18.5:
   ...:         res='low weight'
   ...:     elif bmi>=18.5 and bmi<23:
   ...:         res='normal weight'
   ...:     elif bmi>=23 and bmi<25:
   ...:         res='over weight'
   ...:     elif bmi>=25 and bmi<30:
   ...:         res='obesity'
   ...:     elif bmi>=30:
   ...:         res='try exercise'
   ...:     return res
   ...: 


print ComputeBmi(1.6,55)
