# Import python packages
import streamlit as st

# Write directly to the app
st.title(" :cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your Smoothie!   
    """
)

#from snowflake.snowpark.functions import col

cnx = st.connection("snowflake-connector-python")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(session.col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list = st.multiselect("Choose upto 5 ingredients :",my_dataframe)

if ingredient_list:
    ingredient_string = ''
    for x in ingredient_list:
        ingredient_string += x + ' '
    st.write(ingredient_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredient_string + """')"""

    #st.write(my_insert_stmt)
    time_to_insert = st.button("submit order")
    if time_to_insert:
        if ingredient_string:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered!', icon="✅")
     
