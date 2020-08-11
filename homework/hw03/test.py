def count_change(n):
	"""Return the number of ways to make change for total.
    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def constrained_coin(value, smallest_coin):
    	if value<smallest_coin:
    		return 0
    	if value==0:
    		return 1
    	without_coin= constrained_coin(value, smallest_coin*2)
    	with_coin= constrained_coin(value-smallest_coin, smallest_coin)
    	return without_coin+with_coin
    return constrained_coin(n,1)


