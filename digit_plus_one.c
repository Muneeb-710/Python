#include <stdio.h>

int main() {
    int num, new_num = 0, digit, place = 1;

    printf("Enter a five-digit number: ");
    scanf("%d", &num);

    while (num != 0) {
        digit = num % 10;
        digit = (digit + 1) % 10;
        new_num = new_num + digit * place;
        num = num / 10;
        place = place * 10;
    }

    printf("New number after adding 1 to each digit: %d\n", new_num);

    return 0;
}
