#include <iostream>
#include <gmpxx.h>

int main(void) {
	mpz_class sum;

	for (auto x = 1; x <= 3000; x++) {
		sum += mpz_class::factorial(x);
	}

	std::cout << sum;
	return 0;
}
