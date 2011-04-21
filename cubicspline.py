a1 = [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5]
x1 = [1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 10.0, 13.0, 17.0]

a2 = [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1]
x2 = [17.0, 20.0, 23.0, 24.0, 25.0, 27.0, 27.7]

a3 = [4.1, 4.3, 4.1, 3.0]
x3 = [27.7, 28.0, 29.0, 30.0]

def naturalCubicSpline(n,a=[],x=[], label=""):
	b = [0.0]*n
	d = [0.0]*n
	h = [0.0]*n
	alpha = [0.0]*n
	c = [0.0]*(n+1)
	l = [0.0]*(n+1)
	u = [0.0]*(n+1)
	z = [0.0]*(n+1)
	l[0] = 1
	u[0] = 0
	z[0] = 0
	adjust = 6

	for i in range(0,n):
		h[i] = (x[i+1] - x[i])

	for i in range(1,n):
		alpha[i] = ((3/h[i])*(a[i+1] - a[i]) - (3/(h[i-1]))*(a[i] - a[i-1]))

	for i in range(1,n):
		l[i] = (2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1])
		u[i] = (h[i]/l[i])
		z[i] = ((alpha[i] - h[i-1]*z[i-1])/l[i])

	l[n] = 1
	z[n] = 0
	c[n] = 0

	for i in range(1,n+1):
		j = n - i
		c[j] = (z[j] - u[j]*c[j+1])
		b[j] = (((a[j+1] - a[j])/h[j]) - (h[j]*(c[j+1] + 2*c[j]))/3 )
		d[j] = ((c[j+1] - c[j])/(3*h[j]))

	print "               ",label,"               "
	print "---------------------------------------"
	print "i".rjust(3), "x".rjust(adjust), "a".rjust(adjust), "b".rjust(adjust), "c".rjust(adjust), "d".rjust(adjust)

	for i in range(n):
		print repr(i).rjust(3), repr(x[i]).rjust(adjust), repr(a[i]).rjust(adjust), repr(round(b[i],3)).rjust(adjust), repr(round(c[i],3)).rjust(adjust), repr(round(d[i],3)).rjust(adjust)

	print repr(n).rjust(3), repr(x[n]).rjust(adjust), repr(a[n]).rjust(adjust)

def clampedCubicSpline(n,a=[],x=[],label="",FPO=0.0,FPN=0.0):
	h = [0.0]*n
	b = [0.0]*n
	d = [0.0]*n
	alpha = [0.0]*(n+1)
	c = [0.0]*(n+1)
	l = [0.0]*(n+1)
	u = [0.0]*(n+1)
	z = [0.0]*(n+1)
	adjust = 6

	# Step 1
	for i in range(0,n):
		h[i] = x[i+1] -x[i]

	# Step 2
	alpha[0] = 3*(a[1] - a[0])/h[0] - 3*(FPO)
	alpha[n] = 3*(FPN) - 3*(a[n] - a[n-1])/h[n-1]

	# Step 3
	for i in range(1,n):
		alpha[i] = (3/h[i])*(a[i+1] - a[i]) - (3/h[i-1])*(a[i] - a[i-1])

	# Step 4
	l[0] = 2*h[0]
	u[0] = 0.5
	z[0] = alpha[0]/l[0]

	# Step 5
	for i in range(1,n):
		l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*u[i-1]
		u[i] = h[i]/l[i]
		z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

	# Step 6
	l[n] = h[n-1]*(2 - u[n-1])
	z[n] = (alpha[n] - h[n-1]*z[n-1])/l[n]
	c[n] = z[n]

	# Step 7
	for i in range(1,n+1):
		j = n - i
		c[j] = z[j] - u[j]*c[j+1]
		b[j] = ((a[j+1] - a[j])/h[j]) - (h[j]*(c[j+1] + 2*c[j])/3)
		d[j] = (c[j+1] - c[j])/(3*h[j])

	print "               ",label,"               "
	print "---------------------------------------"
	print "i".rjust(3), "x".rjust(adjust), "a".rjust(adjust), "b".rjust(adjust), "c".rjust(adjust), "d".rjust(adjust)

	for i in range(n):
		print repr(i).rjust(3), repr(x[i]).rjust(adjust), repr(a[i]).rjust(adjust), repr(round(b[i],3)).rjust(adjust), repr(round(c[i],3)).rjust(adjust), repr(round(d[i],3)).rjust(adjust)

	print repr(n).rjust(3), repr(x[n]).rjust(adjust), repr(a[n]).rjust(adjust)



naturalCubicSpline(8, a1, x1, "Spline 1")
naturalCubicSpline(6, a2, x2, "Spline 2")
naturalCubicSpline(3, a3, x3, "Spline 3")

clampedCubicSpline(8, a1, x1, "Spline 1", 1.0, -0.67)
clampedCubicSpline(6, a2, x2, "Spline 2", 3.0, -4.0)
clampedCubicSpline(3, a3, x3, "SPline 3", 0.33, -1.5)
