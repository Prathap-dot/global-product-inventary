#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # ABOUT DATASET:
# 
#     This dataset provides a detailed snapshot of product inventory, perfect for logistics optimization, e-commerce analysis, or supply chain research. It includes key details like product names, categories, prices, stock quantities, and more—sourced from a hypothetical global supplier database. I compiled this while working on a shipment logistics optimization project, and I hope it’s useful for others exploring similar challenges!
#    " sku is stock keeping unit"

# # Key Features:
# 
#    * 14 columns covering product specs, pricing, stock, and tags.
#    * Sample data includes diverse categories like Home Appliances.
#    * Ideal for data cleaning practice, visualizations, or predictive modeling (e.g., stock depletion).

# # Potential Use Cases:
# 
#    * Optimize shipment logistics based on stock and expiration dates.
#    * Analyze pricing trends across product categories.
#    * Build recommendation systems using tags and ratings.

# # Notes:
# 
#    * Dates range from manufacturing to expiration (e.g., 2023-2026).
#    * Some fields (e.g., Product Description) may need refinement—feel free to enhance it!
#    * Suggestions for additional data or improvements are welcome.

# ![warehouse-management-solution-1024x610.jpg](attachment:warehouse-management-solution-1024x610.jpg)

# In[13]:


df=pd.read_csv(r"C:\Users\boddu\Downloads\archive (1)\products.csv")
df


# In[14]:


df.info()


# In[15]:


df.isna()


# In[16]:


df.isna().sum()


# In[17]:


df.iloc[:,1]


# In[18]:


df.duplicated()


# In[19]:


m=df.head(20)
m


# In[20]:


plt.plot(m['Product Name'],color='r')

plt.show()


# In[23]:


plt.plot(m['Product Category'],color='yellow')
plt.show()


# In[16]:


plt.scatter(m['Product Name'],m['Price'],marker='^',s=50,color='g')
plt.grid(axis='x')
plt.grid(axis='y')
plt.xlabel('Product Name')
plt.ylabel('Price')
plt.show()


# In[15]:


plt.bar(x=m['Product Category'],height=m['Stock Quantity'])
plt.show()


# In[18]:


z=m['Product Category'].value_counts()
z


# In[19]:


plt.pie(z,labels=z.index,autopct='%1.1f%%')
plt.show()


# In[20]:


x=m['Product Ratings'].value_counts()
plt.pie(x,labels=x.index,autopct='%1.1f%%')
plt.show()


# In[21]:


c=m['Color/Size Variations'].value_counts()
c


# In[22]:


plt.pie(c,labels=c.index,autopct='%1.1f%%')
plt.show()


# In[23]:


plt.bar(m['Product Name'],m['Manufacturing Date'],color=['r','g'])
plt.show()


# In[24]:


plt.bar(m['Product Name'],m['Expiration Date'],color=['r','g'])
plt.show()


# In[21]:


import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


product_name = ['Laptop', 'SmartPhones', 'HeadPhones','Monitor']
manufacturing_date = [datetime(2023,1,1), datetime(2023, 3, 15), datetime(2023, 5, 10),datetime(2023,4,14)]
expiration_date = [datetime(2026, 1, 1), datetime(2024, 3, 15), datetime(2024, 5, 10),datetime(2024,4,14)]


manufacturing_date_ord = [date.toordinal() for date in manufacturing_date]
expiration_date_ord = [date.toordinal() for date in expiration_date]


xpos = np.arange(len(product_name))


plt.bar(xpos - 0.2, manufacturing_date_ord, width=0.4, label='Manufacturing Date')
plt.bar(xpos + 0.2, expiration_date_ord, width=0.4, label='Expiration Date')


plt.xticks(xpos, product_name)
plt.ylabel('Date (Ordinal Format)')
plt.legend()
plt.title('Product Manufacturing and Expiration Dates')
plt.show()


# In[31]:


sns.relplot(x='Manufacturing Date',y='Expiration Date',data=m,hue='Product Name')
plt.show()


# In[101]:


m[['Price']].mean()


# In[102]:


m[['Price']].median()


# In[103]:


m[['Price']].mode()


# In[32]:


m[['Price']].std()


# In[33]:


m[['Price']].var()


# In[105]:


m[['Price',]].min()


# In[106]:


m[['Price']].max()


# In[108]:


m[['Price']].max() - m[['Price']].min()


# In[104]:


m.describe()


# # Report:   

# # Supply Chain Recovery:
# Post-pandemic, global supply chains have largely stabilized, but challenges persist due to geopolitical tensions, fluctuating raw material costs, and labor shortages in key manufacturing hubs. Companies are increasingly adopting digital tools like AI and IoT to optimize inventory management.
# 
# # Regional Variations:
# North America & Europe: 
# Inventory levels are steady, with a focus on nearshoring to reduce dependency on distant suppliers.
# Asia-Pacific: High production output, but some regions face overstocking due to reduced global demand in certain sectors like electronics.
# Africa & Latin America: Emerging markets are improving inventory systems but still face logistical bottlenecks.
# Trends in Inventory Management:
# 
# # Sustainability:
# Businesses are reducing excess inventory to minimize waste and environmental impact.
# Automation: Widespread adoption of automated warehouses and predictive analytics to balance supply and demand.
# Resilience: Companies are diversifying suppliers and maintaining safety stock to mitigate risks.
# Sector-Specific Insights:
# 
# # Technology:
# Semiconductor shortages have eased, but demand fluctuations remain a concern.
# Retail: E-commerce growth has led to higher inventory turnover, with a focus on last-mile delivery efficiency.
# Automotive: Inventory levels are improving as chip availability stabilizes, but EV components remain a bottleneck.

# # Conclusion:
#     The Global Product Inventory dataset provides a comprehensive overview of product availability, stock levels, and distribution across various regions and categories. By analyzing this dataset, businesses can identify supply chain efficiencies, regional demand patterns, and potential stock imbalances. In conclusion, this dataset is a valuable resource for optimizing inventory management, improving demand forecasting, and making informed decisions in global product distribution.

# In[ ]:




