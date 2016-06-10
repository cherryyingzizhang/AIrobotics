__author__ = 'Cherry_Zhang'

# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].
print [mu, sig]

# Insert code here
def localize(measurements, motion, measurements_sig, motion_sig, initialMu, initialSig):
    p = [0, 0]
    for i in range(len(measurements)):
        if i == 0:
            p = update(initialMu, initialSig, measurements[i], measurements_sig)
        else:
            p = update(p[0], p[1], measurements[i], measurements_sig)

        print p

        p = predict(p[0], p[1], motion[i], motion_sig)
        print p

localize(measurements, motion, measurement_sig, motion_sig, mu, sig)