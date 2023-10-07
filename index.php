
<!DOCTYPE html>
<html>
<head>
	<title>Pi Video Server</title>
</head>
<body>

<h1>Video Gallery</h1>
<hr>
<div id="video-container" style="display: grid; grid-template-columns: 20% 20% 20% 20%; column-gap: 5%; row-gap: 10px;">
<?php 
$videos = glob("*.mp4");

foreach ($videos as $video) {
	echo "<div style='display:block;margin:auto;'>";
	echo "<h2>".$video."</h2>";
	echo "<video controls preload='none'>";
	echo "<source src='".$video."' type='video/mp4'>";
	echo "</video>";
	echo "</div>";

} ?>
</div>
</body>
</html>
