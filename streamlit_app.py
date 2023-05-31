import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena\'s Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.write(df)

color_list = df[0].values.tolist()
option = streamlit.selectbox("Pick a sweatsuit color or style:", list(color_list))


