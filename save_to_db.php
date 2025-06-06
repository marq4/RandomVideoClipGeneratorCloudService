<?php

$filename = $_POST["jsonfilename"];

echo "<p>Name of JSON file: "; //TMP
echo $filename; //TMP
echo "</p>"; //TMP

// Call generate_playlist.py passing name of json file that has been saved:
$cmd = escapeshellcmd("python3 /var/www/rvcg/persist_crate_to_db.py $filename");
$out = shell_exec($cmd);
echo "<div>";
echo "$out";
echo "</div>";

?>

