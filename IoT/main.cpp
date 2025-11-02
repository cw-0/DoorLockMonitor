#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

const char *status = "Locked";

int main() {

  std::string DOOR_NAME;

  std::ifstream config;
  config.open("config.ini");
  if (!config.is_open()) {
    std::cout << "Failed to open config.ini\n";
    exit(EXIT_FAILURE);
  } else {
    if (std::getline(config, DOOR_NAME)) {
      std::cout << "DOOR: " << DOOR_NAME << '\n';
    } else {
      std::cout << "ERROR: Failed to get Door Name from config.ini\n";
      exit(EXIT_FAILURE);
    }
  }

  if (DOOR_NAME != "Front Door" && DOOR_NAME != "Master Bedroom Door" &&
      DOOR_NAME != "Patio Door" && DOOR_NAME != "Kitchen Door") {
    std::cout << "ERROR: Door Name - \"" << DOOR_NAME << "\""
              << " Does not match expectation\n\n";
    std::cout << "Valid Door Names:\nFront Door\nMaster Bedroom Door\nPatio "
                 "Door\nKitchen Door\n";
    exit(EXIT_FAILURE);
  }

  std::string command = "curl -X PUT http://127.0.0.1:5000/door-status "
                        "-H \"Content-Type: application/json\" "
                        "-d '{\"doorname\": \"" +
                        std::string(DOOR_NAME) +
                        "\", "
                        "\"status\": \"" +
                        status + "\"}'";

  std::system(command.c_str());
}

// TODO:
// Run in a while (true) loop
// Use Hall Sensor to get Status
// if status == prev_status:
//    goto(start of while loop)
// else:
//    send PUT request
// add sleep time between status_checks
//
