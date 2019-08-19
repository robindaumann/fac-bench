#!/usr/bin/env php
<?php

function fac($x) {
    $res = 1;
    for(;$x > 0;$x--) {
        $res = bcmul($res, $x);
    }
    return $res;
}

$res = 0;
for($i = 1;$i <= 3000;$i++) {
    $res = bcadd($res, fac($i)); 
}
echo $res;
