#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <tuple>




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
    if (!file.is_open()) {
        std::cerr << "Error: Unable to open the file '" << filename << "'" << std::endl;
        return 1; // Return error code
    }
    // Position : (horizontal, vertical)
    int horizontal = 0;
    int vertical = 0;
    std::string direction;
    int magnitude{};
    while (!file.eof()){
      file >> direction >> magnitude;
      switch (direction[0]) {
        // Forward
        case 'f': horizontal += magnitude; break;
        // Down
        case 'd': vertical += magnitude; break;
        // Up
        case 'u': vertical -= magnitude; break;
        default: break;
      }
    }
    // Close the file
    file.close();
    std::cout << "Final position: " << "(" << horizontal << "," << vertical << ")\n";
    std::cout << "Solution: " << (horizontal * vertical) << "\n";
    return 0; // Return success code
}
