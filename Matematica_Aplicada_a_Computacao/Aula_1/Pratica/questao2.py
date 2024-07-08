"""  
  2. É possível resolver problemas relacionados a expressões lógicas por meio do Python. Considerando as proposições p, q e r onde V(p)=V, V(q)=V e V(r)=F, utilize o Python para obter o valor lógico das seguintes proposições:
  
  a) p+q
  b) p+r 
  c) q.r
  d) (q.r)’
  e) q+r
  f) p’
  g) (p.r)’
"""

p = True;
q = True;
r = False;

print("p + q = ", p or q); # true
print("p + r = ", p or r); # true
print("q . r = ", p and r); # false
print("(q . r)' = ", not(p and r)); # true
print("(q + r)' = ", q or r); # true
print("p' = ", not(p)); # false
print("(p . r)' = ", not(p and r)); # true