setlocal
mkdir target
cd target
cmake .. -G "Visual Studio 15 2017 Win64" && cmake --build .