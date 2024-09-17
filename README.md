# Vehicle Routing Problem

This program solves a version of the Vehicle Routing Problem (VRP). It takes in a problem file
containing the loads to be deliver in the format of:

```
loadNumber pickup dropoff
1 (-50.1,80.0) (90.1,12.2)
2 (-24.5,-19.2) (98.5,1.8)
3 (0.3,8.9) (40.9,55.0)
4 (5.3,-61.1) (77.8,-5.4)
```

and will output a solution - a driver's list of loads - with each new line corresponding
to a new driver.

```
[1]
[4,2]
[3]
```

To run this program you will need Python 3.8 or later installed, and can run:

```console
python3 vrp.py <path_to_file>
```