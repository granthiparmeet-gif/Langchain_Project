#include <expected>  // C++23 feature — added in libc++ 17

#include <iostream>
#include <string>

// Demonstrates usage of std::expected, a feature introduced in C++23 and first supported in libc++ 17
std::expected<int, std::string> parse_number(const std::string& input) {
    if (input == "42") return 42;
    return std::unexpected("Not a valid number: " + input);
}

int main() {
    auto result = parse_number("foo");
    if (result) {
        std::cout << "Unexpectedly Parsed: " << *result << "\n";
    } else {
        std::cout << "Expected Error: " << result.error() << "\n";
    }
}