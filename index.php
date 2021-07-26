<?php
  

?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <link rel="stylesheet" href="style.css">

    <title>FAKE NEWS CLASSIFIER</title>
  </head>
  <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">fakeVsGood</a>

       
        </nav>

       <div class="container">
         <div class="row">
             
            
            <div class="col-sm-4">
                <div class="login_form">
                    <h2 class="text-center">Enter Details</h2>
                    <hr>
                    <form method="post" action="">
                        
                        <div class="form-group">
                            <label >User ID</label>
                            <input type="id" class="form-control" required="required" name="id" id="id" aria-describedby="id" placeholder="Enter User ID">
                            <label >User ID</label>
                            <input type="id" class="form-control" required="required" name="id" id="id" aria-describedby="id" placeholder="Enter User ID">
                            <label >User ID</label>
                            <input type="id" class="form-control" required="required" name="id" id="id" aria-describedby="id" placeholder="Enter User ID">
                            <label >User ID</label>
                            <input type="id" class="form-control" required="required" name="id" id="id" aria-describedby="id" placeholder="Enter User ID">
                            <label >User ID</label>
                            <input type="id" class="form-control" required="required" name="id" id="id" aria-describedby="id" placeholder="Enter User ID">
                        </div>
                        
                        <button type="submit" name="submit" id= "submit" class="form_btn btn btn-secondary">CHECK</button><br>
                        <p>
                          <br> 
                          <a href="enter.php">Add a new entry!</a>
                    </form>
                </div>
            </div>
            <div class="col-sm-4">
            
            </div>
        
        </div>

       </div>
    
  </body>
</html>
<!doctype html>
<html>
<style>
form {
    margin: auto;
    width: 35%;
}
.result {
    margin: auto;
    width: 35%;
    border: 1px solid #ccc;
}
</style>
<head>
    <title>Bike Usage Model</title>
</head>
<form action="{{ url_for('main') }}" method="POST">
    <fieldset>
        <legend>Input values:</legend>
        Temperature:
        <input name="temperature" type="number" required>
        <br>
        <br> Humidity:
        <input name="humidity" type="number" required>
        <br>
        <br> Windspeed:
        <input name="windspeed" type="number" required>
        <br>
        <br>
        <input type="submit">
    </fieldset>
</form>
<br>
<div class="result" align="center">
    {% if result %}
        {% for variable, value in original_input.items() %}
            <b>{{ variable }}</b> : {{ value }}
        {% endfor %}
        <br>
        <br> Predicted number of bikes in use:
           <p style="font-size:50px">{{ result }}</p>
    {% endif %}
</div>
</html>