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
?>
  <form method="post" enctype="mutlipart/form-data" action="empty_crate.php">
    <input value="Empty crate" type="submit" name="empty_crate" />
  </form>
</body>
</html>

