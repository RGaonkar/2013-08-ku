Support example
===============

The goal: edit calculate-shared-counts.py and  calculate-95-percent-cutoff.py until the test script:

    $ sh run_tests.sh

completes without any failures.

When you accomplish that, running

    $ sh calc_support.sh 

should produce an answer for a large data set.

Use "git add" and "git commit" to save your changes into the git repository whenever you have made significant progress.


As you are writing the python scripts you'll probably
want to run them outside of the testing script. Here is how
you do that:

    $ python calculate-shared-counts.py tests/shared-counts/input/tiny 
    $ python calculate-95-percent-cutoff.py tests/cutoff/input/funky 


Some Links
==========

Parameteric Bootstrapping
-------------------------

If you want to look at the statistical background that 
was the inspiration for this example, you can look at

https://molevol.mbl.edu/wiki/index.php/ParametricBootstrappingLab

Note that that explanation is really geared toward people
who are interest in phylogenetic analyses.

