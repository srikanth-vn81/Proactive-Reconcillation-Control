#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import streamlit as st
#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import matplotlib.pyplot as plt
import seaborn as sns
#from PIL import Image

#with st.sidebar.container():
	#image = Image.open("C:\\Users\\srikanthve\\Desktop\\Capture1.JPG")
	#st.image(image)

#from st_aggrid import AgGrid, GridOptionsBuilder
#from st_aggrid.shared import GridUpdateMode

uploaded_file = st.file_uploader(
        "",key="1",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",)

if uploaded_file is not None:
	file_container = st.expander("Check your uploaded .xlsx")
	shows = pd.read_excel(uploaded_file)
	
             
	uploaded_file.seek(0)
	shows_up= shows.loc[shows['Cut Qty'] > 0]
	shows_final=shows.loc[shows['Shipped Qty'] > 0]

#shows_up.head()
#st.write(shows_up)	
	#file_container.write(shows)
	#AgGrid(shows)
	gb = GridOptionsBuilder.from_dataframe(shows_final)
	gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
	gb.configure_side_bar() #Add a sidebar
	gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
	gridOptions = gb.build()
	gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
	
	grid_response = AgGrid(
    shows_final,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True)
	shows.style.applymap(lambda x: "background-color:red; font-size:1.5rem;",
						subset=["Total Pending Reconciliation"])
	

# In[4]:


else:
	st.info(
            f"""
                👆 Upload a .xlsx file first.""" 
        )

	st.stop()


data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected)

if st.button('Download'):
	shows_final.to_csv("C:\\Users\\srikanthve\\console.csv",index=False)
	st.success("Downloaded Successfully")
else:
	st.write()
	
value1=shows_final['Total Pending Reconciliation'].sum()
#st.write(value1)

#from functionforDownloadButtons import download_button
#CSVButton = download_button(df,
        #"File.xslx",
        #"Download to xlsx")

#st.expander("Explore your data .xlsx")

#unique_jobs = shows_final['Style'].unique().tolist()
#job_list = st.sidebar.multiselect("Style",unique_jobs,default=unique_jobs)



#sum_values=shows['Total Pending Reconciliation'].sum()
#st.subheader("Total Pending Reconcillation")
##st.write(sum_values)

#sum_values1=shows["Cut Qty"].sum()
#st.subheader("Total Cut Qty")
#st.write(sum_values1)

#sum_values2=shows(shows.Shipped Qty >0].sum()
#st.subheader("Total Shipped Qty")
#st.write(sum_values2)

menu = ["Graphical Summary","KPI"]
choice = st.sidebar.selectbox("Select",menu)

if choice == "Graphical Summary":
	with st.expander("Boxplot"):
		fig = plt.figure()
		shows_final.boxplot(column = ['Total Pending Reconciliation'], figsize = (5,5))
		st.pyplot(fig)
		
else : 
	choice == " "


if choice == "Graphical Summary":	
	with st.expander("Histogram"):
		fig = plt.figure()
		sns.distplot(shows_final['Total Pending Reconciliation'],hist_kws={"range": [100,1000]},bins=50)
		shows_final['Total Pending Reconciliation'].nlargest(n=5)
		st.pyplot(fig)


else : 
	choice == " "
	
if choice == "Graphical Summary":	
	with st.expander("Scatter Plot"):
		fig = plt.figure()
		sns.regplot("CO Qty", y="Total Pending Reconciliation", data=shows_final)	
		plt.xlim([500,5000])	
		st.pyplot(fig)
		
else : 
	choice == " "

unique_jobs = shows_final['Buyer Division'].unique().tolist()
Buyer_list= st.sidebar.multiselect("Buyer", unique_jobs, default=unique_jobs, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
mask = (shows_final['Buyer Division'].isin(Buyer_list))
selected_df = shows_final[mask]
value2=selected_df['Total Pending Reconciliation'].sum()
#st.write(value2)



#Style_list= st.sidebar.multiselect("Style", Styles, default=Styles, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
#mask1 = (shows_final['Style'].isin(Style_list))
#selected_df1 = shows_final[mask1]
#value3=selected_df1['Total Pending Reconciliation'].sum()
#st.write(value3)

#selected_unique_jobs = selected_df['Buyer Division'].unique().tolist()
#st.title('JobGrouping')
#st.write('Total selected columns : ',len(selected_unique_jobs))

###cols = st.columns(len(selected_unique_jobs))
#new = 0
#for job in selected_unique_jobs:
	#mask1 = (shows_final['Buyer Division'] == job)
	#cols[new].subheader('Selected date ::' + job)
	#cols[new].dataframe(df[mask1])
	#new += 1

unique_jobs1 = shows_final['Style '].unique().tolist()
Style_list=st.sidebar.multiselect("Style ", unique_jobs1, default=unique_jobs1, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
mask = (shows_final['Style '].isin(Style_list))
selected_df1 = shows_final[mask]
value3=selected_df1['Total Pending Reconciliation'].sum()
#st.write(value3)


unique_jobs2 = shows_final['Schedule '].unique().tolist()
Schedule_list=st.sidebar.multiselect("Schedule ", unique_jobs2, default=unique_jobs2, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
mask = (shows_final['Schedule '].isin(Schedule_list))
selected_df2 = shows_final[mask]
value4=selected_df2['Total Pending Reconciliation'].sum()
#st.write(value4)

if choice == "KPI":
	with st.expander("KPI"):
		kpi1, kpi2, kpi3, kpi4 = st.columns(4)
		kpi1.metric(
            label="Pending Reconciliation ⏳",
            value=round(value1))
			
		kpi2.metric(
            label="Selected Buyer Pending Reconciliation ⏳",
            value=round(value2))
			
		kpi3.metric(
            label="Selected Style Pending Reconciliation ⏳",
            value=round(value3))

		kpi4.metric(
            label="Selected Schedule Pending Reconciliation ⏳",
            value=round(value4))

else : 
	choice == " "

