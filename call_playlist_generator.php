<?php

//echo "<p>Call generate_playlist.py!!!</p>"; //TMP

$filename = $_GET["jsonfilename"];

//echo "<p>Name of JSON file: "; //TMP
//echo $filename; //TMP
//echo "</p>"; //TMP

// Call generate_playlist.py passing name of json file that has been saved:
$cmd = escapeshellcmd("python3 /var/www/html/generate_playlist.py $filename");
$out = shell_exec($cmd);
//echo "<div>";
//echo "<h3>This is the XML playlist: </h3>"; //TMP
//echo "$out";
//echo "</div>";

?>

