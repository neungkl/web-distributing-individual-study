<?php
  require('connect.php');

  $conn->query("INSERT INTO comment(name,comment) VALUES(\"{$_POST['name']}\",\"{$_POST['comment']}\")");

  header("Location: index.php");
?>
