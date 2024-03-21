import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import TextBox

def CalculateLeastSquares(X, Y):
	SumSquareX = sum([i * i for i in x])
	SumX = sum(x)
	SumY = sum(y)
	SumMultXY = sum([x[i] * y[i] for i in range(len(x))])

	a = (SumMultXY - SumX * SumY / PointsNumber) / (SumSquareX - SumX * SumX / PointsNumber)
	b = (SumY - SumX * a) / PointsNumber

	return a, b


mpl.rcParams['toolbar'] = 'None'

fig, ax = plt.subplots()

print("Ввод координат точек через консоль через пробел")
PointsNumber = int(input("Количиство точек: "))
x = list(map(float, input("X: ").split()))
y = list(map(float, input("Y: ").split()))

# SumSquareX = sum([i * i for i in x])
# SumX = sum(x)
# SumY = sum(y)
# SumMultXY = sum([x[i] * y[i] for i in range(len(x))])

# a = (SumMultXY - SumX * SumY / PointsNumber) / (SumSquareX - SumX * SumX / PointsNumber)
# b = (SumY - SumX * a) / PointsNumber

a, b = CalculateLeastSquares(x, y)

ax.plot(x, [a * i + b for i in x], label="Approximation")
ax.scatter(x, y, color="#F09D2C", label="Input points")

ax.legend()
ax.set_title("y = " + str(a) + "x + " + str(b))

plt.show()