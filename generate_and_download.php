<?php

$xml_path = '/var/www/html/clips.xspf';
$nice_name = basename($xml_path);
$jsonfilename = $_GET["jsonfilename"];
$n = $_GET["num_clips"];
$m = $_GET["min_duration"];
$x = $_GET["max_duration"];

// Generate the playlist:
exec("python3 /var/www/html/generate_playlist.py $jsonfilename $n $m $x");

// Serve the file for download:
if ( file_exists($xml_path) ) {
	header("Cache-Control: public");
	header("Content-Description: File Transfer");
	header("Content-Disposition: attachment; filename=$nice_name");
	header("Content-Type: application/xml");
	header("Content-Transfer-Encoding: utf-8");
	readfile($xml_path);

} else {
	http_response_code(500);
	echo "Playlist generation failed. ";
}


?>

