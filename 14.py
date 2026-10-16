import matplotlib.pyplot as plt
def plot_profits():
	months=list(range(1,13))
	profits=[]
	print("Enter the profits for each 12 months:")
	for i in range(1,13):
		profit=float(input(f"profit for month {i}:"))
		profits.append(profit)
	plt.figure(figsize=(10,5))
	plt.plot(months,profits,marker='o')
