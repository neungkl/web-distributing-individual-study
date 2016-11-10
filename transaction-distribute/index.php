<?php
  require('connect.php');
?>

<html>
<head>

</head>
<body>
  <form action="add.php" method="post">
    <div>
      Name : <input type="text" name="name">
    </div>
    <div>
      Comment : <textarea name="comment" rows="8" cols="40"></textarea>
    </div>
    <input type="submit" name="Submit">
  </form>
  <hr>
  <?php
    $result = $conn->query("SELECT * FROM comment");
    while($row = mysqli_fetch_assoc($result)) {
      print "<h1>{$row['name']}</h1><p>{$row['comment']}</p><hr>";
    }
  ?>
</body>
</html>
