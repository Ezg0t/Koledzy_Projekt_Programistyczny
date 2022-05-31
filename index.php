<!DOCTYPE html>
<html>
<head>
    <title>Smartwatches </title>
    <link rel="stylesheet" href="node_modules/bootstrap/dist/css/bootstrap.css">
</head>
<body>
<h1 style="text-align: center">Smartwatche dostępne na stronie zegarownia.pl</h1>
<br>
<center>
<div class="col-md-6" style="margin: auto" id="data-json">
    <input style="margin-left: 32px; width: 300px" id="search" placeholder="Wyszukaj zegarek po nazwie.." onkeyup="searchWatches()">
    <br></br>
    <label style="margin-left: 32px;" >Cena od: </label>
    <input id="price_1" type="number" style="width: 80px"  onkeyup="checkPrices()">
    <label>Cena do: </label>
    <input id="price_2" type="number" style="width: 80px"  onkeyup="checkPrices()">
    <label style="margin-left: 40px">Sortuj: </label>
    <select id="sort" onchange="sortList()">
        <option></option>
        <option value="1">Cena rosnąco</option>
        <option value="2"> Cena malejąco</option>
    </select>
    <br></br>
    <ul id="list-group" style="list-style: none">
<?php
$page=1;
        $pageSize=1;

        $filter = [];
        //Pagination display
        $options = [
            'skip'=>($page - 1) * $pageSize,
            'limit'=>$pageSize,
            'sort' => ['createTime' => -1],
            'projection'=>['_id'=> False, "modelXML"=> False],
        ];
require 'vendor/autoload.php';


$i=1;
try {
    $manager = new MongoDB\Driver\Manager("mongodb+srv://koledzy_projekt:u1mkLXkE4niiONPd@cluster0.hwii5.mongodb.net/?retryWrites=true&w=majority");
    $query = new MongoDB\Driver\Query([]);
    $result = $manager->executeQuery('zegarki.scrapy_items', $query);
    foreach ($result as $document) {
        $producent = $document->producent;
        $nazwa = $document->nazwa;
        $cena = $document->cena;
        $zdjecie = $document->zdjecie;
        $link = $document->link;
	echo $i;

        echo '<li>
<div class="list-group w-auto">
  <a href="' . $link . '" class="list-group-item list-group-item-action d-flex gap-3 py-3" aria-current="true">
    <img src="' . $zdjecie . '" width="80" height="80" class="flex-shrink-0">
    <div class="d-flex gap-2 w-100 justify-content-between">
      <div>
        <h4 class="mb-0">'. $nazwa .'</h4>
        <p class="mb-0 opacity-75">Producent: <b>' . $producent . '</b></p>
      </div>
      <small class=" text-nowrap">' . $cena . '<b>PLN</b> </small>
    </div>
  </a>
</div>
<br>
</li>';
$i++;
    }
} catch (MongoConnectionException $e) {
    var_dump($e); 
}

?>
    </ul>
</div>
<script src="js/script.js"></script>


</body>
