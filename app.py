import streamlit as st
from datetime import datetime, date

def calculate_uk_taxable_portion(grant_date, vest_date, uk_arrival_date, uk_departure_date, income_gain):
    total_days = (vest_date - grant_date).days + 1

    if uk_departure_date:
        uk_days = min(vest_date, uk_departure_date) - max(grant_date, uk_arrival_date)
    else:
        uk_days = vest_date - max(grant_date, uk_arrival_date)

    uk_days = uk_days.days + 1
    uk_ratio = uk_days / total_days
    uk_taxable_portion = income_gain * uk_ratio

    return uk_taxable_portion

st.title('RSU Apportioner')
st.subheader('Calculate the UK taxable amount of worldwide Restricted Stock Unit (RSU) income')

grant_date = st.date_input("Grant Date", min_value=date(2000, 1, 1), max_value=date.today(), value=date.today())
vest_date = st.date_input("Vest Date", min_value=grant_date, max_value=date(2050, 12, 31), value=date.today())
uk_arrival_date = st.date_input("UK Arrival Date", min_value=date(2000, 1, 1), max_value=date.today(), value=date.today())
uk_departure_date = st.date_input("UK Departure Date (if applicable)", min_value=uk_arrival_date, max_value=date(2050, 12, 31), value=None)
income_gain = st.number_input("Income Gain at Vest (GBP)", min_value=0.0, value=0.0, step=0.01)

if st.button("Calculate"):
    if grant_date and vest_date and uk_arrival_date and income_gain > 0:
        uk_taxable_portion = calculate_uk_taxable_portion(grant_date, vest_date, uk_arrival_date, uk_departure_date, income_gain)
        st.success(f"UK Taxable Portion: £{uk_taxable_portion:.2f}")
    else:
        st.error("Please fill in all required fields and ensure Income Gain is greater than 0.")
