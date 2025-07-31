<!DOCTYPE html>
<html>
<head>
  <title>Random Video Clip Generator</title>
</head>
<body>
  <h1>Random Video Clip Generator</h1>
  <div>
    <h2>Instructions (Windows):</h2>
    <ol>
      <li>Create folder structure on your computer: <code>C:\Videos\videos</code></li>
      <li>Download some music videos there (contact me for instructions: <a href="mailto:juancmarquina@gmail.com">juancmarquina@gmail.com</a>).</li>
      <li>Download the <a href="s3://TODO">PoweShell script</a>.</li>
      <li>Move it to <code>C:\Videos</code> folder.</li>
      <li>Run it:</li>
	<ol>
	  <li>Open an elevated PowerShell window by pressing <code>WIN+X</code> and selecting Windows PowerShell (Admin).</li>
	  <li>Change-directory into your Videos folder: <code>cd C:\Videos</code></li>
	  <li>Execute the script: <code>powershell.exe -executionpolicy bypass -File .\GenerateList.ps1</code></li>
	  <li>Contact me if you don't see this: <code>Script complete.</code></li>
	</ol>
      <li>Upload <code>list_videos.txt</code> here (see bellow).</li>
      <li>For now we all share a deault crate. After uploading your list of videos, click the <code>Generate Playlist</code> button.</li>
      <li>When you double-click the downloaded playlist, your video clips will appear on VLC media player. Press <code>f</code> key to toggle full-screen.</li>
    </ol>
  </div>
  <form method="post" enctype="multipart/form-data" action="upload.php">
    <label for="fileToUpload">Select video list text file</label>
    <input id="fileToUpload" name="fileToUpload" type="file" />
    <input value="Upload" name="submit" type="submit" />
  </form>
</body>
</html>

