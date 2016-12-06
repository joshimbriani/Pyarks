# Pyarks
Python API for getting wait time data from Amusement Parks

## Example Uaage
```python
  import pyarks
  
  # Get all of the rides at Unicersal Studios in Orlando
  rides = pyarks.getPark(pyarks.UniversalStudiosOrlando)
  
  # For each ride, print out the name and wait time
  for ride in rides:
    print ride.name, " has a wait time of ", ride.waitTime
```
