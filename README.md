# Remix
> Collection of minute scripts/programs/applications

[![Build Status](https://api.travis-ci.org/samar-agrawal/remix.svg?branch=master)](https://travis-ci.com/samar-agrawal/remix)

<img align="right"  width=200 height=90  src="http://enstino.com/images/remix.png">

Some random tasks etc that i came across, some years back, during interviews or life in general.

### Installation
```
python setup.py develop
python3 setup.py develop
```

### Tests
```
tox
```

### Run
Each task has its run command in its own makefile. for eg to run rpn-calculator:

```
cd remix/rpn_calculator
make run
```

## Tasks
Each task is independently located in its own folder, with a small brief in README, a make file with run and test command.

#### [Flatten Array](https://github.com/samar-agrawal/remix/blob/master/remix/flatten_array)
Given an array of nested data lists, convert it into flat structured array.

#### [RPN Calculator](https://github.com/samar-agrawal/remix/blob/master/remix/rpn_calculator)
RPN is a polish mathematical notation in which every operator follows all of its operands. Calculate results for valid RPN expressions.

#### [Invite:Distance Calculator](https://github.com/samar-agrawal/remix/tree/master/remix/invite)
Calculate distance using geographical co-ordinates, for listing eligible attendes located at various co-ordinates using great-circle distance formula.
