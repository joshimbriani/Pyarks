# Pyarks
Python API for getting wait time data from Amusement Parks

## APIs

### `getPark(parkName)`
Gets the specified park given a park name (suuported parks listed later in the document). Returns a park object.

### `Park` (object)
Park object

#### `Park.name`
Returns the name of the park

### `UniversalPark` (object)
The specific Universal object

#### `UniversalPark.parkID`
ID given to each specific Universal Park

#### `UniversalPark.rides`
List of Ride objects correspondfing to all rides at a given park. 

### `Ride`
Base ride class

#### `Ride.park`
Park object that each Ride is part of

#### `Ride.name`
Name of the ride

#### `Ride.waitTime`
Wait time for the ride. Returns a negative value if the ride is closed or is a non-queueable ride

#### `Ride.closed`
Is the ride closed or open?

#### `Ride.isQueueable`
Is the ride queueable? (Typically is false when the ride is a play area or walk through attraction)

#### `Ride.description`
Description for the ride

## Example Usage
```python
  import pyarks
  
  # Get all of the rides at Unicersal Studios in Orlando
  usf = pyarks.getPark("USF")
  
  # For each ride, print out the name and wait time
  for ride in usf.rides:
    print(ride.name, " has a wait time of ", ride.waitTime)
```
