<?php

$cmd = escapeshellcmd("python3 /var/www/rvcg/empty_crate.py");
$out = shell_exec($cmd);
echo "$out";

// Go back to main page:
header('Location: ' . $_SERVER['HTTP_REFERER']);
exit;

?>
