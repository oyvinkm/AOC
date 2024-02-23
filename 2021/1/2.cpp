#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <numeric>




int main(int argc, char* argv[]) {
  // Check if the correct number of command-line arguments is provided
  if (argc != 2) {
      std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
      return 1; // Return error code
  }

  // Get the filename from the command-line arguments
  std::string filename = argv[1];

  // Open the file
  std::ifstream file(filename);

  // Check if the file is opened successfully
  if (!file.is_open()) 
  {
      std::cerr << "Error: Unable to open the file '" << filename << "'" << std::endl;
      return 1; // Return error code
  }
  // Read and output the content of the file
  std::string line;
  std::vector<int> v;
  while (std::getline(file, line)) 
  {
    v.push_back(std::stoi(line));
  }
  // Inner product applies a binary function between elements of two input ranges,
  // and then a binary function between the initial value and the result of the function.
  // The two input ranges are different views of the input, the first function returns 1 
  // if the second value is greater than the first, the other is just a plus.  
  int times = std::inner_product(v.begin(), v.end() - 3, 
                                v.begin() + 3, 0,
                                std::plus<>(),
                                [](auto l, auto r){ return r > l; }); 
  // Close the file
  file.close();
  printf("Result is %d times!\n", times);
  return 0; // Return success code
}