#include <stdio.h>
#include <gmp.h>

void fac(mpz_t res, unsigned x) {
	mpz_set_ui(res, 1);
	for (; x > 1; --x) {
		mpz_mul_ui(res, res, x);
	}
}

int main(void) {
	mpz_t f, res;
	mpz_inits(f, res, NULL);

	for (unsigned x = 1; x <= 3000; x++) {
		fac(f, x);
		mpz_add(res, res, f);
	}

	mpz_out_str(stdout, 10, res);
	mpz_clears(f, res, NULL);
	return 0;
}
