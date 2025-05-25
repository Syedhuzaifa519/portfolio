# # import streamlit as st
# import pandas as pd
# from io import BytesIO

# # st.set_page_config(page_title="file uploder",layout="wide")
# # st.title("file uploder")
# # st.write("upload your file and clean your data") 

# st.set_page_config(page_title="File Uploader", layout="wide")
# st.title("File Uploader")
# st.write("Upload your file and clean your data")

# # files = st.file_uploader("upload scv or xlsx", type=["csv","pdf"], accept_multiple_files=True)


# # if files:
# #     for file in files:
# #         ext= file.name.split(".")[-1]
# #         file.seek(0)
# #     df=pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
# #     st.subheader(f"{file.name} - preview")
# #     st.dataframe(df.head()) #first five raws ko lelega.

# files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

# if files:
#     for file in files:
#         ext = file.name.split(".")[-1].lower()
#         file.seek(0)

#         # Read the file
#         df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

#         st.subheader(f"{file.name} - Preview")
#         st.dataframe(df.head())


# if st.checkbox(f"fill missing values in {file.name}", key=f"fill_{file.name}"):
#     df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
# st.dataframe(df.head)

# st.write(df.head())

#         # .mean ye karyga k jisko koi nuber m value ni di hi usko ye autometic value dedega
#         # fillna pandas ka bana banaya function h

#         # Select columns
# select_columns = st.multiselect(
#             f"Select columns from {file.name}", df.columns.tolist(), default=df.columns.tolist(), key=f"cols_{file.name}"
#         )
        
# df = df[select_columns]
# st.dataframe(df.head())  
# # selectet_columns = st.multiselect(f"selected columns,{file.name}" , df.columns,default=df.columns)
#     #select column sy ye hoga k user apni marzi s select krlega column ko
# df =df[select_columns]
# st.dataframe (df.head())

# #         # Show chart
# numeric_df = df.select_dtypes(include="number")
# if st.checkbox(f"Show chart for {file.name}", key=f"chart_{file.name}") and not numeric_df.empty:st.bar_chart(numeric_df.iloc[:, :2]) 
# # if st.checkbox (f"show cart, {file.name}")and not df.select_dtypes(inclued="number").empty:
# #     st.bar_chart(df.select_dtypes(inclued="number").iloc[:,:2]) 
# format_choice = st.radio(f"Convert {file.name} to:", ["csv", "excel"], key=f"format_{file.name}")
# output = BytesIO()

        
# if format_choice == "csv":
#             df.to_csv(output, index=False)
#             mime = "text/csv"
#             new_filename = file.name.replace(f".{ext}", ".csv")
# else:
#             df.to_excel(output, index=False, engine='openpyxl')
#             mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             new_filename = file.name.replace(f".{ext}", ".xlsx")

# # format_choice = st.radio(f"convert {file.name} to:",["csv","excel"], key=file.name)
# # if st.button(f"download {file.name} as{format_choice}"):
# #  output = BytesIO()

# # if format_choice == "csv":
# #     df.to_csv(output, index=False)
# #     mime ="application/vnd.openxmlformats-officedocument.spreadsheetml.sheeet"
# #     new_name= file.name.replace(ext,"xlsx")
# # output.seek(0)
# st.download_button("download file")
# label=f"Download{file.name}",
# data=output,
# file_name=new_filename,mime=mime,
# key=f"download_{file.name}"

import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Uploader", layout="wide")
st.title("File Uploader")
st.write("Upload your file and clean your data")

files = st.file_uploader("Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()
        file.seek(0)

        # Read the file
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"{file.name} - Preview")
        st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"Fill missing values in {file.name}", key=f"fill_{file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Missing values filled.")

        # Select columns
        selected_columns = st.multiselect(
            f"Select columns from {file.name}", df.columns.tolist(), default=df.columns.tolist(), key=f"cols_{file.name}"
        )
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart
        numeric_df = df.select_dtypes(include="number")
        if st.checkbox(f"Show chart for {file.name}", key=f"chart_{file.name}") and not numeric_df.empty:
            st.bar_chart(numeric_df.iloc[:, :2])

        # File export
        format_choice = st.radio(f"Convert {file.name} to:", ["csv", "excel"], key=f"format_{file.name}")
        output = BytesIO()

        if format_choice == "csv":
            df.to_csv(output, index=False)
            mime = "text/csv"
            new_filename = file.name.replace(f".{ext}", ".csv")
        else:
            df.to_excel(output, index=False, engine='openpyxl')
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            new_filename = file.name.replace(f".{ext}", ".xlsx")

        output.seek(0)
        st.download_button(
            label=f"Download {new_filename}",
            data=output,
            file_name=new_filename,
            mime=mime,
            key=f"download_{file.name}"
        )
