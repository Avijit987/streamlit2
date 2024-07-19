import streamlit as st
with st.container():
        st.text('interesting content')
        st.text('in a potentially ')
        st.text('very stylish container')

    col1, col2, col3 = st.columns(3)
    col1.write('cool column box 1')
    col2.write('cool column box 2')
    col3.write('cool column box 3')
st.markdown(
    """
<style>
/* Style columns */
[data-testid="column"] {
    box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    border-radius: 15px;
    padding: 5% 5% 5% 10%;
} 

/* Style containers */
[data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
    border: 20px groove red;
}

</style>
""",
    unsafe_allow_html=True,
    )