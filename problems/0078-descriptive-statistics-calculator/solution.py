import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # mean
    sum =0
    for i in range(len(data)):
        sum += data[i]
        mean = sum/len(data)
    # median
    sorted_data = sorted(data)
    middle = len(sorted_data)//2
    if len(data)%2 == 1:
        median = float(sorted_data[middle])
    else:
        median = float((sorted_data[middle] + sorted_data[middle - 1])/2)
    # mode
    count = {}
    for num in sorted_data:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    mode = max(count, key=count.get)
    # variance
    sq_deviation = 0
    for i in range(len(data)):
        sq_deviation += (data[i]-mean)**2
        variance = sq_deviation/len(data)
    # standard deviation
    std_dev = float(np.sqrt(variance))
    #percentiles
    p25 = int(0.25 * (len(data)-1)+1)
    p50 = int(0.50 * (len(data)-1)+ 1)
    p75 = int(0.75 * (len(data)-1)+ 1)
    Q1 = float(data[p25 - 1])
    Q2 = median
    Q3 = float(data[p75 - 1])
    IQR = Q3-Q1
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std_dev,
        "25th_percentile": Q1,
        "50th_percentile": Q2,
        "75th_percentile": Q3,
        "interquartile_range": IQR,     
    }
    pass