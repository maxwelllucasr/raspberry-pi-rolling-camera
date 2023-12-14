
<!DOCTYPE html>
<html>
<head>
	<title>Pi Video Server</title>
</head>
<body>

<h1>Video Gallery</h1>
<hr>
<div id="video-container" style="display: grid; grid-template-columns: 100%; column-gap: 5%; row-gap: 10px;">
<?php 
$videos = glob("*.mp4");

function convert_url_string_to_timestamp($datetime) {
    list($date_part, $time_part) = explode("_", $datetime);
    $datetime_combined = str_replace('_', '-', $date_part . ' ' . $time_part);
    return strtotime($datetime_combined);
}

function sort_by_datetime($a, $b) {
    $a = substr($a, 7, strlen($a) - 4);
    $b = substr($b, 7, strlen($a) - 4);
    return convert_url_string_to_timestamp($a) > convert_url_string_to_timestamp($b);
}


usort($videos, "sort_by_datetime");

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
