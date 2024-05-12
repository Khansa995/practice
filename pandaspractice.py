import pandas as pd
df_titanic=pd.read_csv('titanic3.csv')
print(df_titanic)
people={
    'name':['rauf','arif','maaz','hadeed'],
    'age':[52,51,26,22 ],
    'address':['lahore','karachi','lahore','islambad'],
    'cell':['321-123','320-431','321-567','321-999'],
    'bg':['b+','A-','B+','O+']
}
print(people)
df_people=pd.read_csv('people.csv')
print(df_people)
x=people.get('name')
print(x)
mylist=people['name']
print(mylist)
import pandas as pd
x=df_people[' age']
print(x)
import pandas as pd
data={
    'Name':['alice','bob','charlie','david','eva'],
    'Math':[95,88,76,92,89],
    'science':[78,98,77,66,55],
    'History':[45,87,67,54,27]
}
df=pd.DataFrame(data)
print(df)
import numpy as np
import pandas as pd
arr=np.random.randint(10,100,size=(6,5))
print('numpy array:\n',arr)
df=pd.DataFrame(data=arr)
print('pandas Dtaframe:\n',df)
#row label of our choice
df=pd.DataFrame(data=arr,index=['Row0','Row1','Row2','Row3','Row4','Row5'])
print(df)
#col  label of our choice
row_label=['row0','row1','row2','row3','row4','row5']
col_label=['col0','col1','col2','col3','col4',]
df=pd.DataFrame(data=arr,index=row_label,columns=col_label)
print(df)
import pandas as pd
list1=['arif','rauf','maaz','','hadeed']
s=pd.Series(data=list1)
print(s)
print(type(s))
list1=['arif','rauf','maaz','haded']
indices=['MS01','MS02','','MS03']
s=pd.Series(data=list1,index=indices)
print(s)
list1=['arif','rauf','maaz','hadeed']
indices=[2.1,2.2,2.3,2.4]
s=pd.Series(data=list1,index=indices)
print(s)
import pandas as pd
import numpy as np
list1=[1,2.7,np.nan,54]
s=pd.Series(data=list1)
print(s)
print(type(s))
list1=[27,33,19]
s=pd.Series(data=list1,dtype=np.uint8)
print(s) 
import pandas as pd
import numpy as np
s=pd.Series(data=np.arange(4))
print(s)
import pandas as pd
import numpy as np
arr1=np.array([22.3,33.6,98.44])
s=pd.Series(data=arr1,dtype='float64')
print(s)
import pandas as pd
import numpy as np
my_dict={
    'name':'arif',
    'gender':'male',
    'role':'teacher',
    'subject':'data science'
}
s=pd.Series(data=my_dict)
print(s)
import pandas as pd
import numpy as np
s=pd.Series(data=25)
print(s)
import pandas as pd
import numpy as np
s=pd.Series(dtype='float64')
print(s)
import pandas as pd
import numpy as np
my_dict={0:'Rauf',1:np.nan,2:'Mazz',3:'hadeed',4:'Mujahid',5:'ali',6:'jamil'}
s=pd.Series(my_dict,name='myseries1')
print(s)
import pandas as pd
import numpy as np
list1=['rauf','arif','maaz','mujahid','ali']
s=pd.Series(data=list1)
print(s)
import numpy as np
import pandas as pd
list1=['Rauf','arif','maaz','hadeed','mujahid']
s=pd.Series(data=list1)
print(s)
arr1=np.random.randint(low=100,high=200,size=5)
s.index=arr1
print(s)
print(s.index)
import pandas as pd
import numpy as np
list1=['rauf','arif','hadeed','maaz','mujahid']
indices=[5,10,15,20,25]
s=pd.Series(data=list1,index=indices)
print(s)
print(s[25])
print(s.loc[20])
print(s.iloc[3])
print(s[[20,5]])
print(s[[20,5,10]])
print(s.iloc[-1])
print(s[1:4])
print(s.loc[5:15])
print(s.iloc[1:4])
import pandas as pd
import numpy as np
list1=[1,3,5,7,9]
list2=[2,4,6,8,0]
s1=pd.Series(data=list1)
s2=pd.Series(data=list2)
print(s1)
print(s1.index)
print(s2)
print(s2.index)
import pandas as pd
import pandas as pd
import numpy as np
list1=[1,3,5,7,9]
list2=[2,4,6,8,0]
s1=pd.Series(data=list1)
s2=pd.Series(data=list2)
s3=s1+s2
print(s3)
print(s3.index)

