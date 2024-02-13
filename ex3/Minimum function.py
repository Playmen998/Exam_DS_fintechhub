from scipy.optimize import minimize_scalar

# lst = input()
# bounds = [float(i) for i in lst.split(" ")]

"Введем данные для примера"
def f(x):
    return 2*x**2 + 2*x + 2

x_1 = -9999
x_2 = 9999

def ternal_search(f, x_1, x_2):
  result = minimize_scalar(f, bounds=(x_1, x_2), method='bounded')
  x_min = result.x
  return x_min

print(ternal_search(f, x_1, x_2))