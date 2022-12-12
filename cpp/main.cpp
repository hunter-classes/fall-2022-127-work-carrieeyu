/*
Part 1: Basics; Print "Hello World!", followed by a new line (DONE)
Part 2: Use an if-statement and for-loop (DONE)
Part 3: Use a function with at least one parameter, that returns a value (DONE)
*/

#include <iostream>

int abs_value(int a, int b) //Part 3: function with parameters
{
  return abs(a*b); //Part 3: returning value
}

void organization() //just to separate the 3 tasks
{
  std:: cout << "------------------------------------------------------------------------------ \n";
}

int main()
{
  std::cout << "Hello World! \n"; //Part 1: basics
  std::cout << "I am very sad. \n"; // Part 1: basics
  organization();

  int num;
  int i;
  int sum = 0;

  std::cout << "The list of random numbers are: ";

  for(i = 1; i <= 10; i++){ //Part 2: for-loop that goes through 10 numbers
    num = rand() % 100;
    std::cout << num << ",\t";
    if (num > 50) //Part 2: if-statement for if the number is greater than 50
      sum = sum + num;
  }
  std::cout << std::endl;
  std::cout << sum << " is the sum of the numbers that have a value greater than 50. \n"; 
  organization();

  std::cout << "The absolute value of the product is " << abs_value(-2,5) << ". \n"; //utitlizing abs function 
  
  return 0;
}

