<?php

$cmd = escapeshellcmd("python3 /var/www/rvcg/generate_playlist_default_crate.py");
$out = shell_exec($cmd);

echo "<div>";
echo "$out";
echo "</div>";

?>

