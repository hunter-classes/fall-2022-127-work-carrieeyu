#include <iostream>

// this is a single line comment

/*
this is a multiline comment
*/ 

/*
to compile:
  g++ intro.cpp 
  or 
  g++ -o intor intro.cpp

to run:
  ./a.out
  or
  ./intro.cpp
 */

//always include a main function in c++ program
int main()  // here to end of line is a comment 
{
  std::cout << "Hello World!" << std::endl; //will print Hello World when with "/a.out" as input in replt
  std::cout << "is this working?" << std::endl;
  return 0;
}

