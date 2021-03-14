import sys
from IPython import embed
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#plt.style.use('seaborn-paper')

def animate(i, vals):
    ax.clear()
    ax.set_title('Frequency in π digits')
    ax.set_xlabel('Digits')
    ax.set_ylabel('Occurrences')
    ax.bar(list(range(10)), vals[i])
    return vals

def calcPi(how_many):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    for i in range(how_many):
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr

pi_digits = calcPi(4000)
vals = [[0]*10]
counter = 0
for d in pi_digits:
    temp = vals[-1].copy()
    temp[d] += 1
    vals.append(temp)
    counter += 1

print(counter)

fig = plt.figure(figsize=[6.4*1.8, 4.8*1.8])
ax = fig.add_subplot(1, 1, 1)
ani = anim.FuncAnimation(fig, animate, fargs=(vals, ), interval=50, save_count=800)

# Save the animation
anim.Animation.save(ani, 'pi_digits.mp4')

# Show the animation
#plt.show()
