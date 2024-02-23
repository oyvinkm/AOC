#include <iostream>
#include <fstream>
#include <vector>



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

    // Read and output the content of the file
    std::string line;
    int last = std::numeric_limits<int>::max();
    int times = 0;
    while (std::getline(file, line)) {
        int curr = std::stoi(line);
        if (curr > last)
          times++;
        last = curr;
    }
    // Close the file
    file.close();
    printf("Result is %d times!\n", times);
    return 0; // Return success code
}



