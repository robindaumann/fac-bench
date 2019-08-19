#include <stdio.h>
#include <gmp.h>

void fac(mpz_t res, mpz_t x) {
    mpz_set_ui(res, 1);
    while(mpz_cmp_ui(x, 1)) {
        mpz_mul(res, res, x);
	mpz_sub_ui(x, x, 1);
    }
}

int main(void) {
	mpz_t count, in, out, res;
	mpz_init(in);
	mpz_init(out);
	mpz_init_set_ui(res, 0);
	mpz_init_set_ui(count, 1);

	while(mpz_cmp_ui(count, 3001)) {
		mpz_set(in, count);
		fac(out, in);
		mpz_add(res, res, out);
		mpz_add_ui(count, count, 1);
	}
	mpz_out_str(stdout, 10, res);
	mpz_clears(count, in, out, res, NULL);
	return 0;
}
