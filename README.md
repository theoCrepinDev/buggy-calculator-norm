# Calculator

Oh no! Someone pushed [a bad commit](https://github.com/dmerejkowsky/kata-buggy-calculator/commit/dd3cea773b6bb9ee73243a739820d094584f286f)  that introduced a regression ...

The tests are now failing on the main branch.

Add a GitHub Action workflow (or anything else) so that this is less
likely to happen in the future

If you do well, you should have a pull request that introduced a bug
triggering a failed pipeline with a test failing for the good reason.


## Going further

* You probably wrote your workflow so that `pytest` is installed everytime - can
  you speed things up by using a cache ?

* Add an other workflow that runs `black --check`

* Run the tests with Python 3.10, 3.11 and 3.12
 
* Run the tests on Linux, macOS, Windows
 
 * Install and setup `pre-commit` for running black locally - adapt CI workflows accordingly
