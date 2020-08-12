#include <stdio.h>
#include <gmp.h>

int main(void) {
	mpz_t fac, res;
	mpz_inits(fac, res, NULL); /* fac = res = 0 */

	for (unsigned x = 1; x <= 3000; x++) {
		mpz_fac_ui(fac, x);
		mpz_add(res, res, fac);
	}

	mpz_out_str(stdout, 10, res);
	mpz_clears(fac, res, NULL);
	return 0;
}
