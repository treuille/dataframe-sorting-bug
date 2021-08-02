import streamlit as st
import pandas as pd

# Create a bunch of strings of different length.
some_letters = "abc"
some_strings = set(some_letters)
for length in range(1, 3):
    some_strings.update(
        {letter + string for letter in some_letters for string in some_strings}
    )

# Create a dataframe
df = pd.DataFrame(
    {
        "a": list(some_strings),
        "b": range(len(some_strings)),
        "c": reversed(range(len(some_strings))),
    }
)

"""
# :blush: Sorting a _string column_ works

Try sorting **column `a`** and check that it works properly.
"""
with st.echo():
    st.write(df)

"""
# :grimacing: ...but sorting a _string index_ doesn't work!

Try sorting **the index** here. It doesn't sort properly!
"""
with st.echo():
    st.write(df.set_index("a"))


st.write("---")
st.caption(f"Streamlit version `{st.__version__}`")
