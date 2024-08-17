Question 14: Difference Between a Module and a Package in Python


| Parameters  | Modules                           | Package                                    |
|-------------|-----------------------------------|--------------------------------------------|
| Definition: | Modules is a single python file   | A package is a collection of related Python|
|             | that has .py extension.           | modules organized into a hierarchical      |
|             |                                   | structure  along with an _init_.py file.   |
|-------------|-----------------------------------|--------------------------------------------|
| Purpose     | It serves as the basic unit of    | It is mainly used for code reuse and       |
|             | reusable code in Python and is    | code distribution.                         |
|             | used for code organization.       |                                            |
|-------------|-----------------------------------|--------------------------------------------|
| Sub-Modules | It doesn’t contain sub module but | It contain multiple sub-packages, as well  |
|             | it does contains multiple classes,| as sub-modules.                            |
|             | function definitions & statements.|                                            |
|-------------|-----------------------------------|--------------------------------------------|
| Purpose     | We can import modules using       | We can import package using                |
|             | import module_name.               \ import package_name.module_name.           |
|             |                                   |                                            |
|-------------|-----------------------------------|--------------------------------------------|
| Examples    | Examples of modules are random,   | Examples of packages include matplotlib,   |
|             | math, os, datetime etc.           | django, pandas, numpy etc.                 |
|             |                                   |                                            |
|-------------|-----------------------------------|--------------------------------------------|
