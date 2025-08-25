import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load dataset 
data = pd.read_csv("./data/salaries.csv")

X = data[["yearsExperience"]]  # Use double brackets to get DataFrame (2D)
Y = data["salaries"]  # This is fine as Series (1D)

model = LinearRegression()
model.fit(X, Y)

st.title("Salary Predictor Based on Experience")
st.write("Enter your experience to predict your salary ")
years_input = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

# Fixing the error by removing the parentheses
if years_input:
    predicted_salary = model.predict([[years_input]])
    st.write(f"Predicted Salary: ${predicted_salary[0]:,.2f}")

st.subheader("Regression Line")
fig,ax=plt.subplots()
ax.plot(X,model.predict(X),color="red",label="Regression Line")
ax.scatter(X,Y,color="blue",label="Actual Data")
ax.set_xlabel("years of experience")
ax.set_ylabel("salary")
ax.set_title("salary vs experience")
ax.legend()
st.pyplot(fig)