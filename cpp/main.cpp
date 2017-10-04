#include <stdio.h>
#include <unordered_map>
#include <random>

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Expected size in args");
    }
    int size = atoi(argv[1]);

    std::unordered_map<int, int> subject;
    srand(0);

    for (int i = 0; i < size; i++) {
        subject.insert(std::pair<int, int>(
                    i + (size * (rand() % size)),
                    i));
    }
}
