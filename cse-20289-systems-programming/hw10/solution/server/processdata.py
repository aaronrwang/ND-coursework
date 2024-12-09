import re
import numpy

def filter_date(data, date):
    if date=='*':
        return data
    match = re.search(r'^(\*|[0-9]{4})-(\*|[0-9]{2})-(\*|[0-9]{2})$', date)
    if not match:
        print(f"Warning: Invalid date string: {date}")
        return []
    
    y = match[1]
    m = match[2]
    d = match[3]
    res = []
    for item in data:
        year=int(item['timestamp'][:4])
        month=int(item['timestamp'][5:7])
        day=int(item['timestamp'][8:10])
        if y == '*' or int(y) == year:
            if m == '*' or int(m) == month:
                if d == '*' or int(d) == day:
                    res.append(item)
    return res

def filter_time(data, time):
    if time=='*':
        return data

    if len(time) == 1:
        time = '0'+ time

    return [entry for entry in data if entry['timestamp'][11:13]==time]
def filter(data, filters):
    if filters == '*':
        return data

    filters = filters.split(';')
    filtered_data = data

    for filter_str in filters:
        try:
            key, value = filter_str.split('=')  #Try to split filter string
            new_filtered_data = []
            for entry in filtered_data:
                if key in entry and entry[key] == value:  #Check if key exists before accessing it
                    new_filtered_data.append(entry)
            filtered_data = new_filtered_data #update filtered data with the new data

        except ValueError:
            print(f"Warning: Invalid filter string: {filter_str}")
            return []
        except KeyError:
            print(f"Warning: Key '{key}' not found in at least one entry.")
            return []

    return filtered_data

#STRIEGEL SAID TO RETURN 0 AND PUT IT IN THE README
def stat(data, stat):
    #stat argument is sanity checked on the server
    def generator(data):
        for line in data:
            yield line
    if stat == "count":
        return len(data)
    elif stat == "list":
        return (len(data), generator(data))
    else:
        tputs = [entry["tput_mbps"] for entry in data]
        if not tputs:
            return 0
        if stat == "mean":
            return numpy.mean(tputs)
        elif stat == "median":
            return numpy.median(tputs)
        elif stat == "min":
            return min(tputs)
        elif stat == "max":
            return max(tputs)
        elif stat == "stddev":
            return numpy.std(tputs)  
