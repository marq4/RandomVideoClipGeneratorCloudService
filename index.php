<!DOCTYPE html>
<html>
<head>
  <title>Random Video Clip Generator</title>
</head>
<body>
  <h1>Random Video Clip Generator</h1>
  <div></div>
  <h2>Upload a list of videos to replace default crate:</h2>
  <form method="post" enctype="multipart/form-data" action="upload.php">
    <label for="fileToUpload">Select video list text file</label>
    <input id="fileToUpload" name="fileToUpload" type="file" />
    <input value="Upload" name="submit" type="submit" />
  </form>
<?php
	$cmd = escapeshellcmd("python3 /var/www/rvcg/getcrate.py");
	$out = shell_exec($cmd);
	echo "$out";

	$cmd = escapeshellcmd("python3 /var/www/rvcg/is_default_crate_empty.py");
	$out = shell_exec($cmd);
	if (trim($out) == "EMPTY") {
		$grayed_out = True;
	}
?>
  <form method="post" enctype="mutlipart/form-data" action="empty_crate.php">
    <input value="Empty crate" type="submit" name="empty_crate" 
    	<?php if ($grayed_out) { echo "disabled"; } ?> />
  </form>
  <form method="get" enctype="multipart/form-data" action="call_playlist_generator_default_crate.php">
    <input value="Generate Playlist" name="submit" type="submit" 
	<?php if ($grayed_out) { echo "disabled"; } ?> />
  </form>
  <form method="post" enctype="multipart/form-data" action="rename_crate_page.html">
    <input value="Rename crate" name="rename" type="submit" />
  </form>
</body>
</html>

