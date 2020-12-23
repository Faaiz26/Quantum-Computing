#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from iqx import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[2]:


from qiskit import *
#matplotlib inline
from qiskit.tools.visualization import plot_histogram


# In[11]:


secretnumber = input("Enter in 0s and 1s only i.e bits ")


# In[12]:


circuit = QuantumCircuit(len(secretnumber)+1,len(secretnumber))
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))


for ii,yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit.cx(ii,len(secretnumber))

circuit.barrier()
circuit.h(range(len(secretnumber)))        
circuit.barrier()
circuit.measure(range(len(secretnumber)),range(len(secretnumber)))


# In[13]:


circuit.draw(output="mpl")


# In[14]:


simulator = Aer.get_backend('qasm_simulator')


# In[17]:


result = execute(circuit,backend=simulator,shots=1).result()
counts = result.get_counts()
print(counts)


# In[ ]:




