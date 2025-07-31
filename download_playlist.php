<?php


$file = basename($_GET['xml_path']);
//$file = $argv[1];
//$file = $_GET[''
$nice_name = $file;
//echo "<h1>$file</h1>"; //TMP

//$file = '/var/www/html' . $file;

//echo "<h1>FILE:::::$file</h1>"; //TMP. DISABLE THIS LINE for file download to work!

if ( ! file_exists($file) ) {
	http_response_code(404);
	exit('File not found. ');
} else {
	header("Cache-Control: public");
	header("Content-Description: File Transfer");
	header("Content-Disposition: attachment; filename=$nice_name");
	header("Content-Type: application/xml");
	header("Content-Transfer-Encoding: utf-8");
	readfile($file);
}


?>


