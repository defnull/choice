%import bottle
%version = bottle.__version__
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
  <head>
    <title>{{title}} - Choice Game</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    <link type="text/css" rel="stylesheet" href="/main.css" />
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript"></script>
  </head>
  <body>
    <h1>{{title}}</h1>
    <div style='text-align: center'><a href='/'>New game</a> | <a href='http://bottle.paws.de/page/contact'>Contact</a></div>

    %include

    <div id='footer'>
      <div>Powered by <a href="http://bottle.paws.de/"><img src="http://bottle.paws.de/bottle-sig.png" /></a> <small>(Version {{version}})</small></div> 
      <div>Browse sources at <a href="http://github.com/defnull/choice">GitHub</a></div>
    </div>
  </body>
</html>
