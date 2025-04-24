<?php


$file = basename($_GET['xml_path']);
$nice_name = $file;
//echo "<h1>$file</h1>"; //TMP

$file = '/var/www/rvcg/' . $file;

//echo "<h1>$file</h1>"; //TMP

if ( ! file_exists($file) ) {
	die('File not found. ');
} else {
	header("Cache-Control: public");
	header("Content-Description: File Transfer");
	header("Content-Disposition: attachment; filename=$nice_name");
	header("Content-Type: application/xml");
	header("Content-Transfer-Encoding: utf-8");
	readfile($file);
}

?>
