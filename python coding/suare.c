#include <stdio.h>

int main() {
    int size = 5; // You can change this size

    for (int row = 0; row < size; row++) {
        for (int col = 0; col < size; col++) {
            // Print star if it's the first/last row or first/last column
            if (row == 0 || row == size - 1 || col == 0 || col == size - 1) {
                printf("* ");
            } else {
                printf("  "); // Print space for hollow part
            }
        }
        printf("\n"); // Move to the next line
    }

    return 0;
}