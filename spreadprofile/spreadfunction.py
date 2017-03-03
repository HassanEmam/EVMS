def cumulative(data):
	result=[]
	for i in range(len(data)):
		sum =0
		for x in range(i+1):
			sum += data[x]
		result.append(sum)
	return result
	

def spread(profile, duration, budget):
	spread_dur_pct=[]
	cum_profile = cumulative(profile)
	for i in range(duration+1):
		cur = i * 100.0/duration
		spread_dur_pct.append(cur)
	mod_val = [x%5 for x in spread_dur_pct]
	real = [(x//5)*5 for x in spread_dur_pct]
	value1=[cum_profile[int(j/5)] for j in real]
	counter =0
	value2=[]
	for num in mod_val:
		if num >0:
			index_val = int(real[counter]//5)+1
			val = profile[index_val] * num/5.0
			value2.append(val)
		else:
			value2.append(0)
		counter +=1
	result =[v1+v2 for v1,v2 in zip(value1, value2)]
	return result


bellcurve =[0, 0.5, 0.5, 1.5, 1.5, 4, 4, 7.5, 7.5, 11.5, 11.5, 11.5, 11.5, 7.5, 7.5, 4, 4, 1.5, 1.5, 0.5, 0.5]
duration = 100
budget = 100000
print(spread(bellcurve, duration, budget))