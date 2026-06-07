**LAMBDA FUNCTION IN PYTHON**


---
1. Lambda function is an anonymous fucntion to do small functional operations efficiently without definining any traditional fucntion or using unnecessary steps like extra intendation or return. Lambda function is generally used with **FILTER()**, **MAP()** and **REDUCE()**.

2. When we want our code should be in one line then we will use Lambda method.

3. We can also assign our lambda function to a variable to make the function variable.

`When we should not use this:`

* If our lambda function is getting complex such that someone has to stare at it for 30 second or more  to figureout what it does, we should stop and delete lambda and use logical **def** method step by step.

* lambda should not contain multiple lines

*Syntax:*

`lambda arguments: expression`


**Condtional statement in Lambda**
  
  ---
* Now another point, if we want to pass condition in Lambda function, then we have to remember, Python's lambdas are restricted to a single expression and don't support elif or multi-line logic.
* If we have to use multiple conditions, then after the if statement we have to merge all other conditions as a sub-condition into else clause
* The single expression syntax under Lambda is:
  `lambda arguments: value_if_true if condition else value_if_false`
* for multiple conditions: `lambda arguments: value_1 if condition_1 else (value_2 if condition_2 else value_3)`


