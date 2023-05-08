## **ACOSTP**

### *Ant Colony Optimization for Traveling Salesman Problem*

- Very minimal implementation of Ant Colony Optimization for TSP using vanilla Python with huge space for improvement
- Implemented as a small side project while bored

### **Usage**
- Requires graph in text file with line represeting one edge in format **{START} {DISTANCE} {END}**
- Edges are by default non-directional
- Number of iterations and ants can be specified with command line argument
```console
$ python ./main.py -i [--num-ants] [--num-iterations]
```

- For more help run
```console
$ python ./main.py --help
```

