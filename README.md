# Computer-Graphics-Algorithms
This repository contains Python implementations of fundamental computer graphics algorithms.The generated points are printed to the console and plotted for visualization using matplotlib.


**Implemented Algorithms**
-----------------------------------------

**Adaptive Decision Boundary Algorithm**  


* Draws a straight boundary line between two points using an incremental approach.

* Calculates decision points based on slope and direction.

* Minimizes computation by using integer-based operations.

* Adapts to both steep and shallow slopes efficiently.

* Outputs boundary points and visualizes them using matplotlib.



**Bresenham's Line Drawing Algorithm**


* Draws a straight line between two points using only integer calculations.

* Efficiently determines the next pixel position based on an error term.

* Works well for lines with different slopes and directions.

* Reduces computational cost compared to floating-point methods.

* Commonly used in raster graphics and computer display systems.



**Bresenham's Circle Drawing Algorithm**

* Draws a circle efficiently using integer-based calculations.

* Uses symmetry to generate all circle points from one octant.

* Updates pixel positions based on a decision parameter.

* Avoids floating-point operations for faster performance.

* Widely used in raster-based graphics systems.



**DDA (Digital Differential Analyzer) Line Algorithm**

* Draws a straight line by incrementally calculating pixel positions.

* Uses floating-point arithmetic to determine intermediate points.

* Determines step size based on the greater of dx or dy.

* Simple and easy to implement for basic line drawing.

* Less efficient than Bresenham’s algorithm due to floating-point operations.
