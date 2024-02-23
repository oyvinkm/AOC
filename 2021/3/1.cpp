#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>

int main(int argc, char* argv[]){
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << "<filename>" << std::endl;
    return 1;
  }
  std::string filename = argv[1];
  std::ifstream file(filename);

  if (!file.is_open()) {
    std::cerr << "Error: Unable to open file " << filename << std::endl;
  }
  std::string line;
  while (std::getline(file, line)) {
    std::vector<int> vec;
    for (auto c : line)
      std::cout << c;
      // x = c -'0';
      // std::cout << x;
      //vec.push_back(x);
    std::cout << std::endl;
  }
  std::cout << std::endl;
  return 0;
}