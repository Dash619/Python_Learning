import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
 incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
  ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
  in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
   non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Id donec ultrices tincidunt 
   arcu non sodales neque. Vitae turpis massa sed elementum tempus egestas sed. Faucibus in ornare quam viverra. 
   Diam quam nulla porttitor massa id neque aliquam vestibulum. Mi sit amet mauris commodo quis imperdiet. 
   Amet aliquam id diam maecenas ultricies. Libero justo laoreet sit amet cursus sit amet. Mauris commodo 
   quis imperdiet massa. Lorem mollis aliquam ut porttitor. Phasellus vestibulum lorem sed risus ultricies 
   tristique nulla aliquet enim. Non sodales neque sodales ut etiam sit. Odio euismod lacinia at quis risus sed. 
   Dictum varius duis at consectetur lorem donec massa sapien faucibus. Tincidunt vitae semper quis lectus nulla."""
st.write(content)
st.subheader("Our Team")

df = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize() +' '+ row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image(f"Images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize() +' '+ row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image(f"Images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize() +' '+ row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image(f"Images/{row['image']}")