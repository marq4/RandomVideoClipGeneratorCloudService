<?php

$new_name = $_POST["new_name"];
//echo "<p>NEW NAME: $new_name</p>"; //TMP

$cmd = escapeshellcmd("python3 /var/www/rvcg/rename_crate.py '$new_name'");
$out = shell_exec($cmd);
//echo "$out";

// Go back to main page:
header('Location: ' . $_SERVER['HTTP_REFERER']);
exit;

?>

