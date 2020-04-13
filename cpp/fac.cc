#include <iostream>
#include <gmpxx.h>

mpz_class fac(unsigned x) {
	mpz_class res(1);

	for (; x > 1; --x) {
		res *= x;
	}

	return res;
}

int main(void) {
	mpz_class sum;

	for (auto x = 1; x <= 3000; x++) {
		sum += fac(x);
	}

	std::cout << sum;
	return 0;
}
