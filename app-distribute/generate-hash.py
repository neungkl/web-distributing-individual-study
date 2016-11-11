import random
print ''.join('\n' if j == 0 else random.choice('0123456789abcdef') for i in xrange(1000) for j in xrange(100))
