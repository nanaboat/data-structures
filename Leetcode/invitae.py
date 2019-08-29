from unittest import TestCase, main

def filter_solution_1(genome_data, filter_definition):
    # TODO fill this out for task #1
    results = []
    for filter in filter_definition:
        start, end = filter
        for i in range(start, end):
            val = _search(genome_data, i)
            if val:
                results.append(val)
    return results
    
    
def _search(data, item):
    '''
    Binary search implementation to find the position in the data
    Time complexity: O(log(n))
    '''
    start = 0
    stop = len(data) - 1
    
    while start <= stop:
      mid = (start + stop) // 2
      if data[mid][0] == item:
          return data[mid]
      else:
          if data[mid][0] > item:
              stop = mid - 1
          else:
              start = mid + 1
    return None

def filter_solution_2(genome_data, filter_definition):
    # TODO fill this out for task #2
    results = []
    for filter in filter_definition:
        start, end = filter
        for i in range(start, end):
            val = _search_2(genome_data, i)
            if val:
              results.append(val)
    return results

  
def _search_2(data, item):
    '''
    Binary search implementation to find the position in the data
    Time complexity: O(log(n))
    '''
    start = 0
    stop = len(data) - 1
    
    while start <= stop:
        mid = (start + stop) // 2
        if (data[mid][0] <= item)  and (item <= (data[mid][0] + len(data[mid][1]) - 1)):
            return data[mid]
        else:
            if data[mid][0] > item:
                stop = mid - 1
            else:
                start = mid + 1
    return None


def filter_solution_3(genome_data, filter_definition):
    # TODO fill this out for task #3
    data = filter_data(genome_data)
    results = []
    for filter in filter_definition:
        start, end = filter
        for i in range(start, end):
            val = data.get(i)
            if val:
              results.append([i, val])
    return results

def filter_data(data):
    '''
    modelling data into a hashmap for easy position lookups 
    '''
    new_data = {}
    for d in data:
        pos, base = d
        if len(base) > 1:
            for i in range(len(base)):
                new_data[pos+i] = base[i]
        else:
            new_data[pos] = base
    return new_data

def filter_solution_4(genome_data, filter_definition):
    # TODO fill this out for task #2
    results = []
    data = filter_data_1(genome_data)
    for filter in filter_definition:
        start, end = filter
        #import pdb; pdb.set_trace()
        for i in range(start, end):
            val = data.get(i)
            if val:
                for j in val:
                    results.append([i, j])
    return results

def filter_data_1(data):
    '''
    modelling data into a hashmap for easy position lookups 
    '''
    new_data = {}
    for d in data:
        pos, base = d
        if len(base) > 1:
            for i in range(len(base)):
                insert(new_data, base[i], pos+i)
        else:
            insert(new_data, base, pos)
        
    return new_data

def insert(h_map, astr, idx):
    if idx in h_map:
        h_map[idx].append(astr)
    else:
        h_map[idx] = [astr]

class test_tasks(TestCase):
    def test_task_1(self):
        data = [[5, "G"],[6, "A"],[7, "T"],[15, "G"],[19, "T"],[20, "C"],[22, "T"]]
        filters =  [[6, 7],[15, 20]]
        self.assertEqual(filter_solution_1(data, filters), [[6, "A"],[15, "G"],[19, "T"]])
    
    def test_task_2(self):
        data = [[5, "GAT"],[15, "G"],[19, "TC"],[22, "T"]]
        filters = [[6, 7],[15, 20]]
        self.assertEqual(filter_solution_2(data, filters), [[5, 'GAT'], [15, 'G'], [19, 'TC']])
    
    def test_task_3(self):
        data = [[5, "GAT"],[15, "G"],[19, "TC"],[22, "T"]]
        filters = [[6, 7],[15, 20]]
        self.assertEqual(filter_solution_3(data, filters), [[6, "A"],[15, "G"],[19, "T"]])

    def test_task4(self):
        data = [[5, "G"],[5, "T"],[10, "GTC"],[11, "AT"],[13, "ACA"]]
        filters = [[6, 7],[11, 13],[15, 20]]
        self.assertEqual(filter_solution_4(data, filters), [[11, 'T'], [11, 'A'], [12, 'C'], [12, 'T'], [15, 'A']])

if __name__ == "__main__":
    main()