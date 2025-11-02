CXX := g++ 
CXXFLAGS := -std=c++20 -Wall -Wextra -O0


DLLS := libatomic-1.dll libgcc_s_seh-1.dll libssp-0.dll libwinpthread-1.dll
DLL_PATH := /usr/x86_64-w64-mingw32/sys-root/mingw/bin/
WINDOWS_CXX := x86_64-w64-mingw32-g++

TARGET := main
SRC := main.cpp



.PHONY: all debug clean valgrind windows

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

windows:
	@mkdir -p windows_version
	$(WINDOWS_CXX) $(CXXFLAGS) -o windows_version/$(TARGET).exe $(SRC)

dlls:
	@mkdir -p windows_version
	@echo "Copying MinGW DLLs..."
	@for dll in $(DLLS); do \
		cp "$(DLL_PATH)/$$dll" ./windows_version/ ; \
	done
	@echo "Done"


debug:
	$(CXX) -g $(CXXFLAGS) $(SRC) -o debugged

valgrind: $(TARGET)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(TARGET)

clean:
	rm -f $(TARGET) debugged $(TARGET).exe
