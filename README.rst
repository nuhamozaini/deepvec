===============
DeepVec
===============

Tensorflow wrapper for classification


-------------
Requirements
-------------

* Python +3.x

--------------
Installation
--------------

.. code-block:: bash

    pip install deepvec

-------
Notes
-------
* The library is for classification datasets (labeled).
* The library accepts CSV of two columns, text (sentences) column and label column (numeric data only).
* The library transforms text to vector, extracts features from vectors then classifies.

-------
Usage
-------


.. code-block:: python

    from deepvec.deep_vec import DeepVec

    obj = DeepVec(path='/path/to/file.csv', feature='text_col', label='label_col')
    data_frame = obj.prepare()
    obj.proceed(data_frame)

-------------
Contributing
-------------

You are welcome.


--------
License
--------


The library is available as open source under the terms of the `MIT License. <https://opensource.org/licenses/MIT>`_
