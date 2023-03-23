import numpy as np
import matplotlib.pyplot as plt
import cmath
import streamlit as st

def quadratic_eq(coeff_a, coeff_b, coeff_c, start_x, end_x, num_steps):

	a = coeff_a
	b = coeff_b
	c = coeff_c

	x = np.linspace(start_x, end_x, num_steps)


	y = a*x**2 + b*x + c

	fig, ax = plt.subplots()
	plt.title("Quadratic equation")
	plt.xlabel("X")
	plt.ylabel("Y")
	ax.plot(x, y)

	


	delta = (b**2) - (4*a*c)

	if delta > 0 :
		solution1 = (-b - cmath.sqrt(delta))/(2*a) 
		solution2 = (-b + cmath.sqrt(delta))/(2*a)
    	
	return fig

if __name__ == '__main__':
 
 	st.title("Quadratic equation")
 	st.markdown("Plot the quadratic equation from the given below axis for the following equation:")
 	st.markdown("by Rohini Das")
 	st.markdown("ax^2 + b*x + c")

 	st.sidebar.markdown("Controls")


 	coeff_a = st.sidebar.number_input("Insert coeff_a", value=1)
 	coeff_b = st.sidebar.number_input("Insert coeff_b", value=2)
 	coeff_c = st.sidebar.number_input("Insert coeff_c", value=4)
 	start_x = st.sidebar.number_input('Insert a starting range', value=-10) 
 	end_x = st.sidebar.number_input('Insert a end range', value=10)
 	num_steps = st.sidebar.number_input('No. of points', value=10)
 	fig = quadratic_eq(coeff_a, coeff_b, coeff_c, start_x, end_x, num_steps)
 	st.pyplot(fig)

 	st.markdown("#Solutions")
