#include <iostream>

int main()
{
  int i;
  
  i = 0;
  while (i<10){
    std::cout << i << ", ";
    i=i+1;
  }
  std::cout << std::endl;

  std::string s = "hello";
  for (auto letter : s){//auto will allow c++ to try to figure out the code for you
                        //such as the type
    std::cout << letter << "-" ;
  }
  std::cout << "\n\n";
  // std::cout << "\n";
  // char go_again = 'y';
  // while (go_again == 'y'){
  //   std::cout << "Continue? ";
  //   std::cin >> go_again;
  // }

  for (int x=0;x<10;++x){
    std::cout << x << ", ";
    
  }
  std::cout << std::endl;

  return 0;
}
