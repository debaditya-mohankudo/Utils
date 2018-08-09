
# coding: utf-8

# In[2]:


import gmpy2
from gmpy2 import mpz 
import random


# In[4]:


p = gmpy2.next_prime(2 ** 1024 + 2 ** 10)
print(p)
print('bit length ', len(str(bin(p))))


# In[5]:


q = gmpy2.next_prime(2 ** 1024 + 2 ** 100)
print(q)
print('bit length ', len(str(bin(q))))
print('is p equal to q:', p==q)


# In[6]:


modulus = p *q
print(modulus)
print('-' * 40)
print('bit length of modulus', len(str(bin(modulus))))


# ### Zm ( m is modulus)

# ### Note: modulus is the closed set of Zm ( m is the modulus)

# In[7]:


phi = (p-1) * (q-1)
print(phi)


# ### phi is the count of the elments in Zm which are relatively prime to m, gcd (element,m) = 1

# ### significance of phi : Eulers theorm ( a pow phi(n) = 1 mod n, given a and n are coprime)

# In[10]:


exponent = 65537
print('GCD of e and phi', gmpy2.gcd(mpz(exponent), mpz(phi)))
print(mpz(exponent), )
d =  gmpy2.invert(mpz(exponent), mpz(phi))
print(mpz(d))


# #### a valid exponent is one which is < phi and relatively prime to modulus   |65537 is a part of Standards and fixed for the public key exponent | It is set so small ?

# In[11]:


## convert rsa keys to pem format
import rsa
pkey = rsa.PrivateKey(modulus, exponent, d, p,q)
prvkeypem = pkey.save_pkcs1('PEM')
open('privatekepemeven_2048.txt', 'wb').write(prvkeypem)
import os
print(os.path.abspath('.'))
print(prvkeypem)


# #### verify e*d  = 1 (mod phi)

# In[12]:


mpz(d) * mpz(17) % mpz(phi)


# In[13]:


m = 1213


# In[14]:


print('Encrypt a message with private key')
c = gmpy2.powmod(m, exponent, modulus)
print(c)


# In[15]:


print('decrypt a message with public key')
decrypt = gmpy2.powmod(c, d, modulus)
print(decrypt)


# In[16]:


print ('decryption successful :', decrypt == m)


# ### proof - euler's phi (m pow e) pow d mod n m pow (e*d) mod n m pow ( 1 + k*phi) mod n m pow 1 * m pow (k*phi) mod n m * (m pow phi) mod n ( pow k) mod n m * 1 pow k
