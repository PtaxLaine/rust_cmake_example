cmake_minimum_required(VERSION 3.2)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
find_package(cargo "0.24" REQUIRED)
find_package(rustc "1.23" REQUIRED)
enable_testing()

project(example_cmake_rust C)
cargo_build_binary(
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/foobar
    TARGET_MODE release
    TARGET foobar_rust_main
    RESULT foobar_rust_main_path
    CARGO_ARGS --features bin_feature
    )

cargo_build_library(
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/foobar
    TARGET_MODE release
    TARGET_TYPE staticlib
    RESULT foobar_rust_lib
    CARGO_ARGS --features lib_feature
    )

add_executable(example_cmake_rust main.c)
target_link_libraries(example_cmake_rust ${foobar_rust_lib})

if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
	target_link_libraries(example_cmake_rust Ws2_32 Userenv)
else()
    target_link_libraries(example_cmake_rust pthread dl)
endif()

add_test(NAME test_all COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/test_all.py $<TARGET_FILE:example_cmake_rust> ${foobar_rust_main_path})
add_custom_command(
     TARGET example_cmake_rust
     POST_BUILD 
     COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_SOURCE_DIR}/test_all.py $<TARGET_FILE:example_cmake_rust> ${foobar_rust_main_path}
)
