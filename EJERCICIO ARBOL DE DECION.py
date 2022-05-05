#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#IMPORTAR LIBRERIA KLEARN PARA EL ENTRENAMIENTO 


# In[1]:


from sklearn import tree
clf = tree.DecisionTreeClassifier()


# In[ ]:


#INGRESO DE DATOS PARA ENTRENAMIENTO


# In[2]:


x = [[1,1500,1,4000],[2,900,2,200],[1,1200,1,3500],[1,1010,1,2000],[2,1000,1,3500],[2,900,1,3000],[1,800,1,2000],[1,1000,1,1000],[2,2000,2,1000],[1,1100,1,2000]]
y = ['SI','NO','SI','SI','SI','SI','NO','NO','NO','SI']


# In[ ]:


#IDICAMOS LOS DATOS DE ENTRENAMIENTO, Y EN DATO1 COLOCAMOS NUESTRO DATO A REVISIAR


# In[9]:


clf=clf.fit(x, y)
dato1 =[1,2000,1,2000]
prediccion=clf.predict([dato1])


# In[10]:


#IMPRIMIMOS EL RESULTADO


# In[11]:


print(prediccion)
if prediccion=='SI':
    print("Ofrecer Articulo al cliente ingresado")
else:
    print("No se debe ofrecer el articulo al cliente ingresado")


# In[ ]:




