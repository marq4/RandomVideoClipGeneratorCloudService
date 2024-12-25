<?php

$LIMIT = 1_000_000;
$target_dir = "/var/www/Uploads/";
$target_file = $target_dir . basename($_FILES["upload_list"]["name"]);
$uploadOk = 1;

// Check if file already exists
if (file_exists($target_file)) {
    echo "<p>File already exists. Not replacing. </p>";
    $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > $LIMIT) {
    echo "<p>Sorry, your file is too large.</p>";
    $uploadOk = 0;
}

// Only allow txt:
$file_type = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
if ($file_type != "txt") {
    echo "<p>Only text files allowed. </p>";
    $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error:
if ($uploadOk == 0) {
    echo "<p>Sorry, your file was not uploaded.</p>";
    // If everything is ok, try to upload file:
} else {
    if (move_uploaded_file($_FILES["upload_list"]["tmp_name"], $target_file)) {
      `$uploaded_file_name = htmlspecialchars(basename($_FILES["upload_list"]["name"]));
      echo "<p>The file ". $uploaded_file_name . " has been uploaded. </p>";
      // Call parse.py and pass the name of the file that has just been uploaded:
      $cmd = escapeshellcmd("python3 /var/www/html/hello/parse.py $target_file");
      $out = shell_exec($cmd);
      echo "<p>$out</p>";
    } else {
        echo "<p>Sorry, there was an error uploading your file. </p>";
    }
}

?>
