#include <iostream>
#include <fstream>

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

  
  return 0;
}