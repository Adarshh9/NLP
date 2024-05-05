import streamlit as st
import datetime

# Initialize leave records in session state
if "leave_records" not in st.session_state:
    st.session_state.leave_records = {}

# Function to add staff
def add_staff(name):
    if name not in st.session_state.leave_records:
        st.session_state.leave_records[name] = {"leave_dates": []}
        st.success(f"{name} has been added to the staff list.")
    else:
        st.error(f"{name} is already in the staff list.")

# Function to record leave
def record_leave(name, start_date, end_date):
    if name in st.session_state.leave_records:
        st.session_state.leave_records[name]["leave_dates"].append((start_date, end_date))
        st.success(f"Leave for {name} from {start_date} to {end_date} has been recorded.")
    else:
        st.error(f"{name} is not in the staff list.")

# Function to view leave records
def view_leave_records():
    for name, details in st.session_state.leave_records.items():
        st.write(f"{name}:")
        for leave in details["leave_dates"]:
            st.write(f" From {leave[0]} to {leave[1]}")

# Streamlit UI
st.title("Staff Leave Management System")

option = st.selectbox("Choose an option", ["Add Staff", "Record Leave", "View Leave Records"])

if option == "Add Staff":
    name = st.text_input("Enter staff name")
    if st.button("Add Staff"):
        add_staff(name)

elif option == "Record Leave":
    name = st.text_input("Enter staff name")
    start_date = st.date_input("Enter start date", datetime.date.today())
    end_date = st.date_input("Enter end date", datetime.date.today())
    if st.button("Record Leave"):
        record_leave(name, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

elif option == "View Leave Records":
    view_leave_records()
