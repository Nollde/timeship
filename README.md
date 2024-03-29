# Timeship

The timeship lets you easily and transparently time execution times within your python code.

Its concept is that you set anchors in your code specifying timing routes. The timeship module will time the specified routes and transparently inform you about their execution time.

## installation
Timeship can be installed using `pip` via:
```bash
pip install timeship
```

## demo
Simply execute the following python snippet to see the timeship on sea!
```python
import time
from timeship import timeship


with timeship.Anchor("BuildShip"):
    with timeship.Anchor("CollectMaterial"):
        time.sleep(0.2)
    with timeship.Anchor("CarftHull"):
        time.sleep(0.3)
    with timeship.Anchor("CraftMast"):
        time.sleep(0.4)
        with timeship.Anchor("HoistSail"):
            time.sleep(0.1)

with timeship.Anchor("Sail"):
    time.sleep(0.6)

timeship.plot("timeship_demo")

```

## usage
You have two basic different options to set anchors

### the anchor function
The fist option is using timeships anchor function as follows:
```python
# set anchor Arrr
timeship.anchor("Arrr")
# execute code
time.sleep(0.1)
# release anchor Arrr
timeship.anchor("Arrr", release=True)

# set anchor Orrr
timeship.anchor("Orrr")
# execute some code
time.sleep(0.4)
# additionally set anchor Errr
timeship.anchor("Errr")
# execute some other code
time.sleep(0.4)
# release all active anchors by not specifying a name
timeship.anchor()
```

### contexts
The second option is to use contexts

```python
with timeship.Anchor("setup"):
    time.sleep(0.1)
```

### nesting
The timeship also supports nested contexts.
Nested timing context can be specified using a slashy (`context/subcontext`) notation:
```python
timeship.anchor("xdata/load")
time.sleep(0.1)
timeship.anchor()
timeship.anchor("xdata/augment")
```

or by nesting contexts:
```python
with timeship.Anchor("ydata"):
    with timeship.Anchor("load"):
        # execute ydata loading code
        time.sleep(0.2)
    with timeship.Anchor("augment"):
        # execute ydata augmentation code
        time.sleep(0.3)
```

or equivalently:
```python
with timeship.Anchor("zdata/load"):
    # execute zdata loading code
    time.sleep(0.2)
with timeship.Anchor("zdata/augment"):
    # execute zdata augmentation code
    time.sleep(0.3)
```

## plotting timing data
At the end of your code, plot the results by by using the `plot` function. Timeships plotting function (`timeship.plot()`) creates a directory (specified by the `dir` argument) with an index.html containing an interactive (go ahead and click it) d3 sunburst plot with the timing data which can be viewed through a webbrowser.

```python
timeship.plot(dir="timeship")
```
This will create a new directory (in this case called "timeship") and store an html page, which contains a clear visualization of the timing data.

Sail on through space and time, Arrr!


