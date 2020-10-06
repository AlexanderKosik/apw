Matrix
======

Wir können uns eine leere Matrix mit dem Modul `numpy` anlegen.

.. code-block:: python

   # import numpy nach Konvention
   import numpy as np

   m = np.empty((10, 10))

   # Zuweisung (assignment) an Position 0,0
   m[0, 0] = 5
