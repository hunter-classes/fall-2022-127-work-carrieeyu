//type this to run program:     ./a.out

#include <iostream>

int main() 
{
  int x = 21; //declaring varible with type and ";" at the end
  double d = 21;
  char c;
  bool tf = false;
  std::string s = "this is a string";

  std::cout << "Hello World!\n";
  std::cout << "the var x = " << x << "\n";

  std::cout << "Doubles: "<< d << " " << d/2 << std::endl;
  std::cout << "Ints: "<< x << " " << x/2 << std::endl;

  c = 'x'; // a SINGLE character 
  d = x/2.0;//to get the result of a double, you need to divide by a double
  std::cout<<c << "\n";

  std::cout << "A true value: " << tf << "\n";

  std::cout << s << "\n";
  return 0;
}
//c++ code needs a function; otherwise code will not run outside of function
//c++ doesn't care about indentation

/*
primitvies:
-int double(decimals), char(1 byte, 8 bits, bool)

*/