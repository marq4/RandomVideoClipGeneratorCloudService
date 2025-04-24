<!DOCTYPE html>
<html>
<head>
    <title>Video list upload</title>
</head>

<body>
<?php


//echo "<h1>Hello!</h1>"; //TMP



$LIMIT = 5_000_000; // 5 MB. 
$target_dir = "/var/www/Uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);


//echo "<p>Limit => $LIMIT</p>"; //TMP
//echo "<p>Target File => $target_file</p>"; //TMP


// Check if file looks like text and get its size:
if ( isset($_POST["submit"]) ) {
    $size = filesize($_FILES["fileToUpload"]["tmp_name"]);
    //echo "<p>Filesize => $size</p>"; //TMP 
    if ($size < 1) {
        echo "<p>That does not look like a text file. </p>";
        exit(1);
    }
}


// Check if file already exists:
if (file_exists($target_file)) {
    echo "<p>File already exists. Not replacing. </p>";
    exit(2);
}



// Only allow txt:
$file_type = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
if ($file_type != "txt") {
    echo "<p>Only text files allowed. </p>";
    exit(3);
}



if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    $uploaded_file_name = htmlspecialchars(basename($_FILES["fileToUpload"]["name"]));
    echo "<p>The file ". $uploaded_file_name . " has been uploaded. </p>";
    // Call parse.py and pass the name of the file that has just been uploaded:
    $cmd = escapeshellcmd("python3 /var/www/rvcg/parse.py $target_file");
    $out = shell_exec($cmd);
    echo "$out";
} else {
    echo "<p>Sorry, there was an error uploading your file. </p>";
    exit(2);
}



//echo "<p>END!!!</p>"; //TMP


?>


</body>
</html>

