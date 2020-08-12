#!/usr/bin/env php
<?php

$res = 0;
for($i = 1;$i <= 3000;$i++) {
    $res += gmp_fact($i);
}
echo $res;
